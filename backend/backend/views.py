from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from django.db import connection
from django.utils import timezone
from .llm.service import get_text_embeddings_llama, generate_note_connections_with_llm
from .cosine_similarity import compute_similarity
from django.shortcuts import get_object_or_404


@require_POST
@csrf_exempt
def notes_api(request):
    try:
        data = json.loads(request.body)
        title = "Jasmine Test"
        # title = data["title"].strip()
        content = data.get("content", "").strip()
        if not title:
            return JsonResponse({"error": "Title is required"}, status=400)
        # TODO: try ben's function
        embeddings = get_text_embeddings_llama(content)
        created_at = updated_at = timezone.now().date()

        with connection.cursor() as cursor:
            cursor.execute(
                """
                    INSERT INTO note_data (title, content, created_at, updated_at, embeddings)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                [title, content, created_at, updated_at, embeddings],
            )
        return JsonResponse({"status": "success"}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_GET
def get_note_by_id(request, note_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, title, content, created_at, updated_at FROM note_data WHERE id = %s",
                [note_id],
            )
            row = cursor.fetchone()

        if not row:
            return JsonResponse(
                {"error": f"Note with ID {note_id} not found"}, status=404
            )

        note = {
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "created_at": row[3],
            "updated_at": row[4],
        }
        return JsonResponse(note)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_GET
def get_all_notes_preview(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, content FROM note_data")
            rows = cursor.fetchall()

        preview_notes = []
        for row in rows:
            note_id, title, content = row
            preview = " ".join(content.split()[:10])
            preview_notes.append({"id": note_id, "title": title, "preview": preview})

        return JsonResponse({"notes": preview_notes})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def analyze_note_api(request):
    if request.method == "GET":
        try:
            # Step 1: Fetch all notes
            with connection.cursor() as cursor:
                cursor.execute("SELECT title, content, embeddings FROM note_data")
                notes = cursor.fetchall()

            if len(notes) < 2:
                return JsonResponse({"error": "Need at least 2 notes"}, status=400)

            # Step 2: Extract query (latest) note
            query_title, query_content, query_embedding = notes[-1]

            # Step 3: Compute similarity with previous notes
            similarities = []
            for title, content, embedding in notes[:-1]:
                score = compute_similarity(query_embedding, embedding)
                similarities.append((score, title, content))

            similarities.sort(reverse=True)
            top_notes = similarities[:3]

            # Step 4: Prepare similar_notes result
            similar_notes_result = [
                {
                    "title": title,
                    "content": content,
                    "similarity": round(score, 3),
                }
                for score, title, content in top_notes
            ]

            # Step 5: Build LLM prompt using top similar notes
            synthesis = generate_note_connections_with_llm(
                query_content, similar_notes_result
            )

            # Step 6: Return both results
            return JsonResponse(
                {
                    "query_note": {"title": query_title, "content": query_content},
                    "similar_notes": similar_notes_result,
                    "synthesis": synthesis,
                }
            )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
