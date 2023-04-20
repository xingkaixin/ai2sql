from typing import Callable

from pydantic import BaseModel


class Tool(BaseModel):
    name: str
    description: str
    func: Callable[[str], str]
