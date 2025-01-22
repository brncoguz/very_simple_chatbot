from anthropic import Anthropic

# Load environment variables
from helper import load_env
load_env()

client = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

MODEL_NAME="claude-3-5-sonnet-20241022"

print("Simple Chatbot (type 'quit' to exit)")
# Store conversation history
messages = []
while True:
    # Get user input
    user_input = input("You: ")
    # Check for quit command
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    try:
        # Get response from Claude
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=200,
            messages=messages
        )
        # Extract and print Claude's response
        asst_message = response.content[0].text
        print("Assistant:", asst_message)
        
        # Add assistant response to history
        messages.append({"role": "assistant", "content": asst_message})
        
    except Exception as e:
        print(f"An error occurred: {e}")