from markdown_parser import MarkdownParser

# Define folder containing markdown files
folder_path = "resources/sample-notes-markdown/Abstraction/Abstraction 1"  # Change this to your folder

parser = MarkdownParser(folder_path)
file_embeddings = parser.get_weighted_embeddings()
file_embeddings_ollama = parser.get_ollama_embeddings()


# Loop through each markdow
# Print sample output
for file, embeddings in file_embeddings.items():
    print("NLP + Sentence Transformer")
    print(f"\nFile: {file}")
    for word, embedding in list(embeddings.items())[:5]:  # Print first 5 words per file
        print(f"  {word}: {embedding[:5]}...")  # Print first 5 values of embedding

# test for ollama embeddings
for file, embeddings in file_embeddings_ollama.items():
    print("OLLAMA")
    print(f"\nFile: {file}")
    for word, embedding in list(embeddings.items())[:5]:  # Print first 5 words per file
        print(f"  {word}: {embedding[:5]}...")  # Print first 5 values of embedding
