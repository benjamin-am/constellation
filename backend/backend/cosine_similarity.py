import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(query_embedding, stored_embedding):
    query_embedding = np.array(query_embedding).reshape(1, -1)
    stored_embedding = np.array(stored_embedding).reshape(1, -1)
    return float(cosine_similarity(query_embedding, stored_embedding)[0][0])
