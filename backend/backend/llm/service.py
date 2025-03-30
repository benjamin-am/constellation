import ollama
import time


def get_text_embeddings_llama(text: str) -> str:
    """Get text embeddings using the Llama model"""
    return ollama.embeddings(model="llama3.2", prompt=text)["embedding"]


def generate_note_connections_with_llm(
    current_text: str, top_similar_notes: list[dict]
) -> str:
    """
    Use an LLM to generate insights by comparing the current note
    to top similar past notes.

    Args:
        current_text (str): The content of the new note
        top_similar_notes (list): A list of dicts with 'title' and 'content' keys

    Returns:
        str: LLM-generated insight text
    """

    old_notes = ""
    for note in top_similar_notes:
        title = note.get("title", "Untitled")
        content = note.get("content", "")
        old_notes += f"\n---\nTitle: {title}\n{content}\n"

    prompt = f"""
    NEW NOTE:
    {current_text}
    
    RELEVANT PAST NOTES:
    {old_notes}
    
    TASK: Identify 2–3 meaningful connections between the new note and the past notes.
    How do these concepts relate to each other? What insights might emerge from connecting these ideas?

    Please optimize for brevity and clarity.
    """
    start_time = time.time()
    response = ollama.generate(model="llama3.2", prompt=prompt)
    end_time = time.time()

    print(f"\nLLM Response (took {end_time - start_time:.2f} seconds):\n")

    return response["response"]
