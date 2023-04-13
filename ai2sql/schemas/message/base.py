import json

from pydantic import BaseModel

from ai2sql.schemas.role import ChatRole


class BaseMessage(BaseModel):
    role: ChatRole
    content: str

    def __str__(self):
        return json.dumps(self.dict())

    def to_messages(self):
        return json.loads(json.dumps(self.dict()))


class SystemMessage(BaseMessage):
    role = ChatRole.system


class UserMessage(BaseMessage):
    role = ChatRole.user


class AIMessage(BaseMessage):
    role = ChatRole.assistant
