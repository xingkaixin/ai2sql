from enum import Enum


class ChatRole(str, Enum):
    system = "system"
    user = "user"
    assistant = "assistant"


class PromptMessage:
    def __init__(self, chat_role: ChatRole, chat_content: str):
        self.role = chat_role.value
        self.content = chat_content

    @property
    def message(self):
        return {
            "role": self.role,
            "content": self.content,
        }
