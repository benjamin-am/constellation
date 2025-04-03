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
        new note:
        {current_text.lower()}

        RELEVANT PAST NOTES:
        {old_notes}

        You are an advanced note synthesis and knowledge extraction assistant. Given the NEW NOTE on a specific topic, your task is to:

        1. Understand the key concepts, ideas, and themes presented in the new note.
        2. Identify 2 connections in the relevant past notes that are related to this new topic, focusing on similarities in content, concepts, or underlying themes.
        3. For each connection:
            - Prompt a question to the user that may hint at how the current and past notes share a topic.
            - Provide the questions and how the relevant past notes connect to the questions.PLEASE PROVIDE SOME DETAIL.
            - Do not force a connection.

          IMPORTANT: Return your response in the following plain text format, using clear labels. Do not use JSON or markdown formatting. Use the following structure:

            Intro: <brief overview or contextual summary>

            Connection Title: <title for the first connection>
            Insight: <insight text>
            Question: <reflective question>

            Connection Title: <title for the second connection>
            Insight: <insight text>
            Question: <reflective question>
    """
    start_time = time.time()
    response = ollama.generate(model="llama3.2", prompt=prompt)
    end_time = time.time()

    print(f"\nLLM Response (took {end_time - start_time:.2f} seconds):\n")

    return response["response"]
