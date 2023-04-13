from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel

from ai2sql.schemas.message import AIMessage, BaseMessage, SystemMessage, UserMessage


class BaseMessageTemplate(BaseModel, ABC):
    prompt: str

    @classmethod
    def from_template(cls, template: str):
        return cls(prompt=template)

    @abstractmethod
    def format_prompt(self, **kwargs: Any) -> BaseMessage:
        return


class SystemMessageTemplate(BaseMessageTemplate):
    def format_prompt(self, **kwargs: Any) -> BaseMessage:
        text = self.prompt.format(**kwargs)
        return SystemMessage(content=text)


class UserMessageTemplate(BaseMessageTemplate):
    def format_prompt(self, **kwargs: Any) -> BaseMessage:
        text = self.prompt.format(**kwargs)
        return UserMessage(content=text)


class AIMessageTemplate(BaseMessageTemplate):
    def format_prompt(self, **kwargs: Any) -> BaseMessage:
        text = self.prompt.format(**kwargs)
        return AIMessage(content=text)
