from django.http import JsonResponse
import json

# Hardcoded sample notes
SAMPLE_NOTES = [
    {
        "id": "123",
        "title": "AI Concepts",
        "content": "This is a note about AI and machine learning concepts",
        "created_at": 1679580000,
        "updated_at": 1679580000,
    },
    {
        "id": "456",
        "title": "Psychology Notes",
        "content": "Notes about cognitive biases and decision-making processes",
        "created_at": 1679580100,
        "updated_at": 1679580100,
    },
]


def notes_api(request):
    """Simple view that returns hardcoded notes"""
    if request.method == "GET":
        return JsonResponse(SAMPLE_NOTES[1], safe=False)
    elif request.method == "POST":
        # Just return a hardcoded response for testing
        return JsonResponse(SAMPLE_NOTES[0], status=201)


def similar_notes_api(request):
    """Return hardcoded similar notes"""
    return JsonResponse({"query": "Sample query", "results": SAMPLE_NOTES})


def synthesize_api(request):
    """Return hardcoded synthesis"""
    return JsonResponse(
        {
            "synthesis": "This is a sample synthesis connecting your notes on AI and Psychology.",
            "similar_notes": SAMPLE_NOTES,
        }
    )
