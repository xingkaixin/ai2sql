from enum import Enum


class ChatRole(str, Enum):
    default = "default"
    system = "system"
    user = "user"
    assistant = "assistant"
