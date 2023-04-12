import random

import openai

from utils import logger, openai_config

from .base import Base


class GPTBot(Base):
    def __init__(self):
        openai.api_key = random.choice(openai_config.key)
        openai.api_base = openai_config.base_url
        self.client = openai
        self.model = "gpt-3.5-turbo"

    def ask(self, messages: list):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.5,
                max_tokens=1024,
                stop="Observation",
            )
            return (
                response["choices"][0]
                .get("message")
                .get("content")
                .encode("utf8")
                .decode()
            )
        except Exception:
            logger.exception("GPTBot:ask")
            return ""
