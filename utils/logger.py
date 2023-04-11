from pathlib import Path

from loguru import logger as log


class Logger:
    def __init__(
        self,
        log_dir: str,
        rotation: str = "00:00",
        encoding: str = "utf-8",
        enqueue: bool = True,
        compression: str = "zip",
        retention: str = "7 days",
        level: str = "INFO",
    ):
        self.log_path = Path(log_dir).joinpath("run.log")
        self.log_path.parent.mkdir(exist_ok=True, parents=True)
        log.add(
            self.log_path,
            rotation=rotation,
            encoding=encoding,
            enqueue=enqueue,
            compression=compression,
            retention=retention,
            level=level,
        )

    def get_logger(self):
        return log


logger = Logger("log").get_logger()
