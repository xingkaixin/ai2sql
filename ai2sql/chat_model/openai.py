import random
from typing import Any, Dict, Optional

from pydantic import root_validator

from ai2sql.chat_model.base import BaseChatModel
from ai2sql.core.config import openai_config
from ai2sql.schemas.message import BaseMessage
from ai2sql.schemas.template import BaseTemplate


class ChatOpenAI(BaseChatModel):
    client: Any
    model_name: str = "gpt-3.5-turbo"
    temperature: float = 0.5
    openai_api_key: str = None
    openai_base_url: str = None
    streaming: bool = False
    n: int = 1
    max_tokens: Optional[int] = None

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        openai_api_key = random.choice(openai_config.key)
        openai_base_url = openai_config.base_url
        try:
            import openai

            openai.api_key = openai_api_key
            if openai_base_url:
                openai.api_base = openai_base_url
        except ImportError:
            raise ValueError(
                "Could not import openai python package. "
                "Please install it with `pip install openai`."
            )
        try:
            values["client"] = openai.ChatCompletion
        except AttributeError:
            raise ValueError(
                "`openai` has no `ChatCompletion` attribute, this is likely "
                "due to an old version of the openai package. Try upgrading it "
                "with `pip install --upgrade openai`."
            )
        if values["n"] < 1:
            raise ValueError("n must be at least 1.")
        if values["n"] > 1 and values["streaming"]:
            raise ValueError("n must be 1 when streaming.")
        return values

    def __call__(
        self,
        prompt: list[BaseMessage] | list[BaseTemplate],
        stop: Optional[list[str]] = None,
    ):
        return self._generate(prompt, stop)

    def _generate(
        self,
        prompt: list[BaseMessage] | list[BaseTemplate],
        stop: Optional[list[str]] = None,
    ):
        return self._prompt_to_messages(prompt)

    @staticmethod
    def _prompt_to_messages(prompt):
        if isinstance(prompt, dict):
            return [prompt]
        elif isinstance(prompt, BaseMessage):
            return [prompt.to_messages()]
        elif isinstance(prompt, list) and all(
            isinstance(p, BaseMessage) for p in prompt
        ):
            return [p.to_messages() for p in prompt]
        elif isinstance(prompt, list) and all(
            isinstance(p, BaseTemplate) for p in prompt
        ):
            return [p for p in prompt]
