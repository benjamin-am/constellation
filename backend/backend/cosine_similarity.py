import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
from django.db import connection


class DatabaseSimilarityEngine:
    """
    A similarity engine that works with embeddings already stored in the database.
    """

    def __init__(self):
        self.embeddings_cache = {}

    def compute_similarity(self, query_embedding, stored_embedding):
        """
        Compute cosine similarity between two embedding vectors

        Args:
            query_embedding: Query embedding vector
            stored_embedding: Stored embedding vector

        Returns:
            Cosine similarity score (float between -1 and 1)
        """
        # Reshape embeddings to 2D arrays for sklearn
        query_embedding = np.array(query_embedding).reshape(1, -1)
        stored_embedding = np.array(stored_embedding).reshape(1, -1)

        # Calculate cosine similarity
        similarity = cosine_similarity(query_embedding, stored_embedding)[0][0]
        return float(similarity)

    def find_similar_notes(self, query_embedding, top_n=5):
        """
        Find the most similar notes to the query embedding

        Args:
            query_embedding: The embedding vector to compare against
            top_n: Number of similar notes to return

        Returns:
            List of (note_id, similarity_score) tuples
        """
        similarities = []

        # Get notes with embeddings from the database
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, embedding
                FROM notes_note
                WHERE embedding IS NOT NULL
                """
            )

            # Process each note
            for note_id, embedding_json in cursor.fetchall():
                # Parse the stored embedding
                stored_embedding = json.loads(embedding_json)

                # Compute similarity
                similarity = self.compute_similarity(query_embedding, stored_embedding)

                # Store result
                similarities.append((note_id, similarity))

        # Sort by similarity (highest first)
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Return top N results
        return similarities[:top_n]
