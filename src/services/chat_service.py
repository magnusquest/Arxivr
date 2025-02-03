from baml_client import b
from baml_client.types import ToolType, Message, Task

class ChatService:
    def __init__(self):
        self.toolsEnabled = False
        self.messageQueue: list[Message] = []
        self.messages: list[Message] = []
        self.prompt: str = ""

    def run(self):
        while True:
            if len(self.messageQueue) > 0:
                print(f"AI: {self.messageQueue.pop(0).message}")
            else:
                self.prompt = input("Enter your message (or 'quit' to exit): ")
                if self.prompt.lower() == "quit":
                    break
                if self.prompt.lower().startswith("enable tools"):
                    self.toolsEnabled = True
                    print("Tools enabled")
                    continue
                if self.prompt.lower().startswith("disable tools"):
                    self.toolsEnabled = False
                    print("Tools disabled")
                    continue
                message = Message(role="user", message=self.prompt)
                
            self.messages.append(message)
            
            # TODO AgentManager sends message to target agent
            
            if self.toolsEnabled:
                agent_tool_response = b.ReasoningAgent(self.prompt) # will create tool call tasks
                agent_response = str(agent_tool_response)
            else:
                agent_response = b.Prompt(messages_to_strings(self.messages)) 
            
            print(f"AI: {agent_response}")
            print()

            # TODO : Needs to be broadcast using Observer - Subject pattern
            # TODO : Agent Wrapper Classes ^^ AgentBuilder Factory Pattern
            
            self.messages.append(Message(role="system", message=agent_response))

def messages_to_strings(messages: list[Message]) -> list[str]:
    return [message.message for message in messages]

if __name__ == "__main__":
    chat_service = ChatService()
    chat_service.run()
