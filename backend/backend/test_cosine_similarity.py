import os
import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

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

    print("\n=== Testing with Ollama embeddings (WHOLE FILE EMBEDDINGS) ===")
    test_with_ollama_embeddings(parser, folder_path)


if __name__ == "__main__":
    test_similarity_between_files()
