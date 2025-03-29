import os
import markdown
from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer

# Download required NLTK resources
nltk.download("stopwords")
nltk.download("punkt")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

class MarkdownParser:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.stop_words = set(stopwords.words("english"))
        self.file_embeddings = {}
        self.markdown_set_weighted_embeddings()
        
    def markdown_plaintext(self, file_path):
        # Read the file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()  # Read line by line
        return content
            
    def markdown_set_weighted_embeddings(self):
        # Loop through each markdown file in the folder
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".md"):  # Only process Markdown files
                file_path = os.path.join(self.folder_path, filename)

                content = self.markdown_plaintext(file_path)

                word_freq =  self.content_counter(content)

                # Convert words to embeddings
                word_embeddings = {word: model.encode(word) for word in word_freq.keys()}

                # Weight embeddings by frequency
                weighted_embeddings = {word: embedding * word_freq[word] for word, embedding in word_embeddings.items()}

                # Store embeddings for this file
                self.file_embeddings[filename] = weighted_embeddings
          
    def content_counter(self, content):
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
            filtered_words = [word for word in words if word not in self.stop_words]

            # Assign higher weight to heading words
            weight = 2 if is_heading else 1
            for word in filtered_words:
                word_freq[word] += weight
        
        return word_freq
          
    def get_weighted_embeddings(self):
        return self.file_embeddings
                
                

