import json

from pydantic import BaseModel

from ai2sql.schemas.role import ChatRole


class BaseTemplate(BaseModel):
    role: ChatRole
    content: str

    @classmethod
    def from_template(cls, in_template: str):
        return cls(role=ChatRole.default, content=in_template)

    def __str__(self):
        return json.dumps(self.dict())


class SystemTemplate(BaseTemplate):
    @classmethod
    def from_template(cls, in_template: str):
        return cls(role=ChatRole.system, content=in_template)


class UserTemplate(BaseTemplate):
    @classmethod
    def from_template(cls, in_template: str):
        return cls(role=ChatRole.user, content=in_template)


class AITemplate(BaseTemplate):
    @classmethod
    def from_template(cls, in_template: str):
        return cls(role=ChatRole.assistant, content=in_template)


class ChatPromptTemplate(BaseModel):
    messages: list

    @classmethod
    def from_messages(cls, messages: list[BaseTemplate]):
        return cls(messages=messages)

    def format_prompt(self, **process_params):
        formatted_messages = []
        for message in self.messages:
            print(message)
            formatted_messages.append(
                BaseTemplate(
                    role=message.role, content=message.content.format(**process_params)
                )
            )
        return ChatPromptTemplate.from_messages(formatted_messages)

    def to_messages(self):
        return [json.loads(str(msg)) for msg in self.messages]
