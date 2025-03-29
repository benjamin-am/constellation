from markdown_parser import MarkdownParser

# TODO: PLEASE CHANGE THIS TO YOUR FOLDER PATH
folder_path = "/Users/jasminezou/Documents/BCS/Hackathons/bcs-hacks-roots/resources/sample-notes-markdown/Abstraction/Abstraction 1"  # Change this to your folder

parser = MarkdownParser(folder_path)

file_embeddings = parser.get_weighted_embeddings()
parser.calculate_ollama_embeddings() 
file_embeddings_ollama = parser.get_ollama_embeddings()

# Loop through each markdow
# Print sample output
print("\n--- NLP Sentence Transformer Embeddings: PER WORD ---")
for file, embeddings in file_embeddings.items():
    print(f"\nFile: {file}")
    for word, embedding in list(embeddings.items())[:5]:  # Print first 5 words per file
        print(f"  {word}: {embedding[:5]}...")  # Print first 5 values of embedding

# test for ollama embeddings
print("\n--- OLLAMA Embeddings: PER FILE  ---")
for file, embedding in file_embeddings_ollama.items():
    print(f"\nFile: {file}")
    print(f"  Embedding (first 5 values) for the entire file: {embedding[:5]}...")
