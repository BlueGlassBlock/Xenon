from typing import List
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image
from graia.ariadne.message.parser.twilight import UnionMatch, Twilight
from graia.saya.channel import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.app import Ariadne
from library.path import asset
from library.config import XConfig
import random

from loguru import logger

channel = Channel.current()


class PicConfig(XConfig):
    __scope__ = "pic"
    __dest__ = "pic"
    trigger: List[str] = ["图片"]
    relative_path: str = "pic"


cfg = PicConfig()

path = asset.joinpath(cfg.relative_path)

path.mkdir(parents=True, exist_ok=True)

img_list = [f for f in path.iterdir() if f.is_file()]
if not img_list:
    logger.warning(f"没有图片在 {path} 下")


@channel.use(ListenerSchema([GroupMessage], inline_dispatchers=[Twilight([UnionMatch(*cfg.trigger)])]))
async def handle(app: Ariadne, ev: GroupMessage):
    img_list = [f for f in path.iterdir() if f.is_file()]
    if not img_list:
        return await app.sendMessage(ev, MessageChain.create("没有图片"))
    await app.sendMessage(ev, MessageChain([Image(data_bytes=random.choice(img_list).read_bytes())]))
