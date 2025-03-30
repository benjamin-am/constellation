import os
import re
from collections import Counter
import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer
import ollama
from typing import Dict, List, Counter as CounterType


# Download required NLTK resources
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
stop_words = set(stopwords.words("english"))


def content_counter(content) -> CounterType[str]:
    word_freq = Counter()  # Word frequency counter

    for line in content:
        line = line.strip()
        is_heading = line.startswith("#")  # Check if line is a heading

        # Remove Markdown "#" symbols
        clean_line = re.sub(r"^#+\s*", "", line).lower()

        # Remove punctuation and tokenize
        clean_line = re.sub(r"[^\w\s]", "", clean_line)
        words = word_tokenize(clean_line)

        # Remove stopwords
        filtered_words = [word for word in words if word not in stop_words]

        # Assign higher weight to heading words
        weight = 2 if is_heading else 1
        for word in filtered_words:
            word_freq[word] += weight

    return word_freq


def word_embeddings(content):
    word_freq = content_counter(content)
    # Convert words to embeddings
    word_embeddings = {word: model.encode(word) for word in word_freq.keys()}

    # Weight embeddings by frequency
    weighted_embeddings = {
        word: embedding * word_freq[word] for word, embedding in word_embeddings.items()
    }

    avg_query_embedding = np.mean([emb for emb in weighted_embeddings.values()], axis=0)

    return avg_query_embedding
