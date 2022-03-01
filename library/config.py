from loguru import logger
import toml
from pydantic import BaseModel

from .path import config


class XConfig(BaseModel):
    __scope__: str
    """toml 位置"""

    __dest__: str
    """配置文件名"""

    def __init__(self):
        path = config.joinpath(f"{self.__dest__}.toml")
        path.touch(exist_ok=True)
        text = path.read_text(encoding="utf-8")
        value = toml.loads(text)
        try:
            for key in self.__scope__.split("."):
                if key:
                    value = value[key]
        except KeyError:
            logger.critical(f"{path} 没有 {self.__scope__} 节点")
            raise
        super().__init__(**value)
