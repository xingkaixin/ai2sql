from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel


class Completion(BaseModel):
    model_name: Optional[str] = "gpt-3.5-turbo"
    max_token: Optional[int] = 1024
    temperature: Optional[float] = 0.5
    streaming: Optional[bool] = False
    stop: Optional[list[str]]
    n: Optional[int] = 1


class Config(BaseModel):
    description: str
    completion: Completion
    prompt: str

    @classmethod
    def load_skill(cls, path: Path):
        parten_path = Path("./skills").joinpath(path)
        yaml_path = parten_path.resolve().joinpath("config.yaml")
        txt_path = parten_path.resolve().joinpath("prompt.txt")
        data_config = yaml.safe_load(yaml_path.read_text("utf-8"))
        data_txt = txt_path.read_text("utf-8")
        return cls(
            description=data_config["description"],
            completion=Completion(**data_config["completion"]),
            prompt=data_txt,
        )


def load_skill(path: str):
    config = Config.load_skill(Path(path)).dict()
    return config
