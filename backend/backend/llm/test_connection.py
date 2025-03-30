# test_ollama.py - Test script for Ollama integration

import ollama
import time


def test_basic_generation():
    """Test basic text generation with Ollama"""
    print("Testing basic generation...")

    start_time = time.time()
    response = ollama.generate(
        model="llama3.2",
        prompt="What are three effective knowledge management techniques?",
        options={"temperature": 0.7, "top_p": 0.9},
    )
    end_time = time.time()

    print(f"Response (took {end_time - start_time:.2f} seconds):")
    print(response["response"])
    print("\n" + "-" * 50 + "\n")


def test_chat_completion():
    """Test chat completion with Ollama"""
    print("Testing chat completion...")

    start_time = time.time()
    chat_response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant that specializes in knowledge management and connecting ideas across disciplines.",
            },
            {
                "role": "user",
                "content": "I have notes about neural networks from my CS class and notes about human memory from psychology. How might these topics connect?",
            },
        ],
    )
    end_time = time.time()

    print(f"Chat response (took {end_time - start_time:.2f} seconds):")
    print(chat_response["message"]["content"])
    print("\n" + "-" * 50 + "\n")


def test_note_connections():
    """Test finding connections between notes"""
    print("Testing note connections functionality...")

    new_note = """
    Today I learned about backpropagation in neural networks. The way errors propagate
    backward through the network to adjust weights seems like an elegant learning mechanism.
    The gradient descent optimization reminds me of how we iteratively improve solutions.
    """

    old_notes = """
    Note from Psychology 101: Memory consolidation involves strengthening neural pathways.
    Short-term memories become long-term memories through repeated activation and connection
    formation. The hippocampus plays a crucial role in this process.
    
    Note from Philosophy class: Connectionism suggests that knowledge exists in the connections
    between simple processing units, rather than being stored explicitly. This contrasts with
    symbolic approaches to knowledge representation.
    """

    prompt = f"""
    NEW NOTE:
    {new_note}
    
    RELEVANT PAST NOTES:
    {old_notes}
    
    TASK: Identify 2-3 meaningful connections between the new note about backpropagation
    and the past notes about memory consolidation and connectionism. How do these concepts
    relate to each other? What insights might emerge from connecting these ideas?
    """

    start_time = time.time()
    response = ollama.generate(model="llama3.2", prompt=prompt)
    end_time = time.time()

    print(f"Connections response (took {end_time - start_time:.2f} seconds):")
    print(response["response"])


if __name__ == "__main__":
    print("TESTING OLLAMA INTEGRATION WITH LLAMA 3.2\n")

    try:
        test_basic_generation()
        test_chat_completion()
        test_note_connections()
        print("\nAll tests completed successfully!")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("\nMake sure Ollama is running and the llama3.2:1b model is installed.")
        print("You can install it with: ollama pull llama3.2:1b")
