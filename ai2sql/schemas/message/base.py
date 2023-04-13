from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseMessage(BaseModel, ABC):
    content: str

    @property
    @abstractmethod
    def role(self) -> str:
        return


class SystemMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "system"


class UserMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "user"


class AIMessage(BaseMessage):
    @property
    def role(self) -> str:
        return "assistant"


def message_to_dict(message: BaseMessage) -> dict:
    return {"role": message.role, "content": message.content}


def messages_to_dict(messages: list[BaseMessage]) -> list[dict]:
    return [message_to_dict(m) for m in messages]


def message_from_dict(message: dict) -> BaseMessage:
    _role = message["role"]
    if _role == "user":
        return UserMessage(**message)
    elif _role == "assistant":
        return AIMessage(**message)
    elif _role == "system":
        return SystemMessage(**message)
    else:
        raise ValueError(f"Got unexpected role: {_role}")


def messages_from_dict(messages: list[dict]) -> list[BaseMessage]:
    return [message_from_dict(m) for m in messages]
