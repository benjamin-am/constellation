from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from django.db import connection
from django.utils import timezone
from .llm.service import get_text_embeddings_llama, generate_note_connections_with_llm
from .cosine_similarity import compute_similarity
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404


# @csrf_exempt
# def notes_api(request):
#     if request.method == "GET":
#         try:
#             data = json.loads(request.body)
#             # TODO: change this to actual title
#             title = "Jasmine Test"
#             # title = data["title"].strip()
#             content = data.get("content", "").strip()
#             if not title:
#                 return JsonResponse({"error": "Title is required"}, status=400)
#             if not content:
#                 return JsonResponse({"error": "Content is required"}, status=400)
#             # TODO: try ben's function

#             try:
#                 embeddings = get_text_embeddings_llama(content)
#             except Exception as e:
#                 return JsonResponse(
#                     {"error": f"Failed to generate embeddings: {str(e)}"}, status=500
#                 )

#             created_at = updated_at = timezone.now().date()

#             with connection.cursor() as cursor:
#                 cursor.execute(
#                     """
#                         INSERT INTO note_data (title, content, created_at, updated_at, embeddings)
#                         VALUES (%s, %s, %s, %s, %s)
#                         """,
#                     [title, content, created_at, updated_at, embeddings],
#                 )
#             return JsonResponse({"status": "success"}, status=201)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)


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


@csrf_exempt
@require_POST
def save_note(request):
    """
    Endpoint to save a note to the database.
    """
    try:
        data = json.loads(request.body)
        title = data.get("title", "").strip()
        content = data.get("content", "").strip()

        # Validate input
        if not title:
            return JsonResponse({"error": "Title is required"}, status=400)
        if not content:
            return JsonResponse({"error": "Content is required"}, status=400)

        # Generate embeddings
        try:
            embeddings = get_text_embeddings_llama(content)
        except Exception as e:
            return JsonResponse(
                {"error": f"Failed to generate embeddings: {str(e)}"}, status=500
            )

        # Set timestamps
        created_at = updated_at = timezone.now().date()

        # Save to database
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO note_data (title, content, created_at, updated_at, embeddings)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                [title, content, created_at, updated_at, embeddings],
            )
            note_id = cursor.fetchone()[0]

        return JsonResponse({"status": "success", "note_id": note_id}, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


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
@require_POST
def analyze_note_draft(request):
    """
    Analyze a note draft without saving it to the database.
    Used when user types more than 30 words or clicks 'Analyze'.
    """
    try:
        data = json.loads(request.body)
        title = data.get("title", "").strip() or "Untitled"
        content = data.get("content", "").strip()

        if not content or not title:
            return JsonResponse({"error": "Content and title are required"}, status=400)

        # TODO: try ben's function
        try:
            query_embedding = get_text_embeddings_llama(content)
        except Exception as e:
            return JsonResponse(
                {"error": f"Failed to generate embeddings: {str(e)}"}, status=500
            )

        # Fetch all stored notes
        with connection.cursor() as cursor:
            cursor.execute("SELECT title, content, embeddings FROM note_data")
            notes = cursor.fetchall()

        if len(notes) < 1:
            return JsonResponse(
                {"error": "No stored notes to compare against."}, status=400
            )

        # Compute similarity
        similarities = []
        for title_db, content_db, embedding_db in notes:
            score = compute_similarity(query_embedding, embedding_db)
            similarities.append((score, title_db, content_db))

        similarities.sort(reverse=True)
        top_notes = similarities[:3]

        similar_notes_result = [
            {
                "title": t,
                "content": c,
                "similarity": round(s, 3),
            }
            for s, t, c in top_notes
        ]

        synthesis = generate_note_connections_with_llm(content, similar_notes_result)

        return JsonResponse(
            {
                "query_note": {"title": title, "content": content},
                "similar_notes": similar_notes_result,
                "synthesis": synthesis,
            }
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


# @csrf_exempt
# def analyze_note_api(request):
#     if request.method == "GET":
#         try:
#             # Step 1: Fetch all notes
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT title, content, embeddings FROM note_data")
#                 notes = cursor.fetchall()

#             if len(notes) < 2:
#                 return JsonResponse({"error": "Need at least 2 notes"}, status=400)

#             # Step 2: Extract query (latest) note
#             query_title, query_content, query_embedding = notes[-1]

#             # Step 3: Compute similarity with previous notes
#             similarities = []
#             for title, content, embedding in notes[:-1]:
#                 score = compute_similarity(query_embedding, embedding)
#                 similarities.append((score, title, content))

#             similarities.sort(reverse=True)
#             top_notes = similarities[:3]

#             # Step 4: Prepare similar_notes result
#             similar_notes_result = [
#                 {
#                     "title": title,
#                     "content": content,
#                     "similarity": round(score, 3),
#                 }
#                 for score, title, content in top_notes
#             ]

#             # Step 5: Build LLM prompt using top similar notes
#             synthesis = generate_note_connections_with_llm(
#                 query_content, similar_notes_result
#             )

#             # Step 6: Return both results
#             return JsonResponse(
#                 {
#                     "query_note": {"title": query_title, "content": query_content},
#                     "similar_notes": similar_notes_result,
#                     "synthesis": synthesis,
#                 }
#             )

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
#     else:
#         return JsonResponse({"error": "Method not allowed"}, status=405)
