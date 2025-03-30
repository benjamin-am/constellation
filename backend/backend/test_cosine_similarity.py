import os
import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time
import ollama

# Add the nlp directory to the Python path so we can import from it
nlp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "nlp"))
sys.path.append(nlp_path)

from nlp.markdown_parser import MarkdownParser


def compute_similarity(query_embedding, stored_embedding):
    """
    Compute cosine similarity between two embedding vectors

    Args:
        query_embedding: Query embedding vector
        stored_embedding: Stored embedding vector

    Returns:
        Cosine similarity score (float between -1 and 1)
    """

    # Reshape embeddings to 2D arrays for sklearn from 1D arrays
    query_embedding = np.array(query_embedding).reshape(1, -1)
    stored_embedding = np.array(stored_embedding).reshape(1, -1)

    similarity = cosine_similarity(query_embedding, stored_embedding)[0][0]
    return float(similarity)


def test_with_word_embeddings(parser, folder_path):
    """Test using the word-weighted embeddings approach"""

    file_embeddings = parser.get_weighted_embeddings()

    if not file_embeddings:
        print("No weighted_embeddings found.")
        return

    # Get the first file to use as our query
    files = list(file_embeddings.keys())
    if not files:
        print("No files found in the embeddings dictionary.")
        return

    print(files)
    query_file = files[0]
    print(f"Using {query_file} as the query file")

    # For word-weighted embeddings, we need to average the embeddings of all words
    # to get a single embedding vector for the file
    query_embeddings = file_embeddings[query_file]

    if not query_embeddings:
        print(f"No embeddings found for {query_file}")
        return

    avg_query_embedding = np.mean([emb for emb in query_embeddings.values()], axis=0)
    print(f"Query embedding shape: {avg_query_embedding.shape}")

    similarities = []
    for file, embeddings in file_embeddings.items():
        if embeddings:
            avg_embedding = np.mean([emb for emb in embeddings.values()], axis=0)
            similarity = compute_similarity(avg_query_embedding, avg_embedding)
            similarities.append((file, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)

    print("\nSimilar notes (using word-weighted embeddings):")
    for i, (file, similarity) in enumerate(similarities):
        print(f"{i+1}. {file} (Similarity: {similarity:.4f})")

    top_similar_files = [file for file, _ in similarities if file != query_file][:3]

    test_note_connections_with_top_similar_notes(
        query_file, top_similar_files, folder_path
    )


def test_with_ollama_embeddings(parser, folder_path):
    """Test using the Ollama embeddings approach"""

    parser.calculate_ollama_embeddings()
    file_embeddings_ollama = parser.get_ollama_embeddings()

    if not file_embeddings_ollama:
        print("No Ollama embeddings found. Please check")
        return

    # Get the first file to use as query
    files = list(file_embeddings_ollama.keys())
    if not files:
        print("No files found in the Ollama embeddings dictionary.")
        return

    query_file = files[0]
    print(f"Using {query_file} as the query file")

    # Get the query embedding
    query_embedding = file_embeddings_ollama[query_file]

    # Compare with every other file
    similarities = []
    for file, embedding in file_embeddings_ollama.items():
        similarity = compute_similarity(query_embedding, embedding)
        similarities.append((file, similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)

    print("\nSimilar notes (using Ollama embeddings):")
    for i, (file, similarity) in enumerate(similarities):
        print(f"{i+1}. {file} (Similarity: {similarity:.4f})")

    top_similar_files = [file for file, _ in similarities if file != query_file][:3]

    test_note_connections_with_top_similar_notes(
        query_file, top_similar_files, folder_path
    )


def test_similarity_between_files():
    """
    Test the similarity between the first note and all other notes in the test folder.
    This test uses the actual embeddings generated from the markdown files.
    """

    # UPDATE THIS PATH TO YOUR FOLDER
    folder_path = "/Users/jasminezou/Documents/BCS/Hackathons/bcs-hacks-roots/resources/sample-notes-markdown/testData-us"

    if not os.path.exists(folder_path):
        print(f"Error: Folder not found at {folder_path}")
        return

    # Initialize the parser
    parser = MarkdownParser(folder_path)

    print(
        "\n=== Testing with word-weighted embeddings (AVERAGE ACROSS WORD-BASED EMBEDDINGS) ==="
    )
    test_with_word_embeddings(parser, folder_path)

    # print("\n=== Testing with Ollama embeddings (WHOLE FILE EMBEDDINGS) ===")
    # test_with_ollama_embeddings(parser, folder_path)


def test_note_connections_with_top_similar_notes(
    query_file, top_similar_files, folder_path
):
    """Test finding connections between a query note and top similar notes"""

    print("\n=== Testing note connections with LLM ===")

    def read_file_content(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    query_path = os.path.join(folder_path, query_file)
    new_note = read_file_content(query_path)

    old_notes = ""
    for filename in top_similar_files:
        file_path = os.path.join(folder_path, filename)
        content = read_file_content(file_path)
        old_notes += f"\n---\nNote: {filename}\n{content}\n"

    prompt = f"""
    NEW NOTE:
    {new_note}
    
    RELEVANT PAST NOTES:
    {old_notes}
    
    TASK: Identify 2-3 meaningful connections between the new note and the past notes.
    How do these concepts relate to each other? What insights might emerge from connecting these ideas?

    Please optimize for brevity and clarity.
    """

    start_time = time.time()
    response = ollama.generate(model="llama3.2", prompt=prompt)
    end_time = time.time()

    print(f"\nLLM Response (took {end_time - start_time:.2f} seconds):\n")
    print(response["response"])


if __name__ == "__main__":
    test_similarity_between_files()
