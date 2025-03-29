from markdown_parser import MarkdownParser

# Define folder containing markdown files
folder_path = "resources/sample-notes-markdown/Abstraction/Abstraction 1/"  # Change this to your folder


parser = MarkdownParser(folder_path)
file_embeddings = parser.get_weighted_embeddings()


# Loop through each markdow
# Print sample output
for file, embeddings in file_embeddings.items():
    print(f"\nFile: {file}")
    for word, embedding in list(embeddings.items())[:5]:  # Print first 5 words per file
        print(f"  {word}: {embedding[:5]}...")  # Print first 5 values of embedding
