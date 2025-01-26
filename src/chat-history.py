from baml_client import b
from baml_client.types import MyUserMessage

def main():
    messages: list[MyUserMessage] = []
    
    while True:
        content = input("Enter your message (or 'quit' to exit): ")
        if content.lower() == 'quit':
            break
        
        messages.append(MyUserMessage(role="user", content=content))
        
        agent_response = b.ChatWithLLM(messages=messages)
        print(f"AI: {agent_response}")
        print()
        
        # Add the agent's response to the chat history
        messages.append(MyUserMessage(role="assistant", content=agent_response))

if __name__ == "__main__":
    main()
