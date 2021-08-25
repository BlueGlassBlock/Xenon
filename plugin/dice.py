# coding=utf-8
"""
骰娘
"""
import heapq
import random
import re

from graia.application import MessageChain
from graia.application.message.elements.internal import Plain
from graia.saya import Saya, Channel
from graia.saya.builtins.broadcast import ListenerSchema

from lib.command import CommandEvent

LIMIT = 100

__version__ = "1.0.0"
__author__ = "BlueGlassBlock"
__plugin_name__ = "dice"
__plugin_doc__ = f"""\
.roll 掷骰子
"""

saya = Saya.current()
channel = Channel.current()

pattern = re.compile(r"^.roll[ ]?(?P<dice_cnt>\d+)?d?(?P<max_side>\d+)?k?(?P<max_cnt>\d+)?")


@channel.use(ListenerSchema(listening_events=[CommandEvent]))
async def roll_dice(event: CommandEvent):
    if event.command.startswith(".roll"):
        match = re.match(pattern, event.command)

        dice_cnt_str = match.group('dice_cnt')
        dice_max_str = match.group('max_side')
        max_cnt_str = match.group('max_cnt')

        if not dice_cnt_str:
            dice_cnt = 1
        elif int(dice_cnt_str) > 100:
            return await event.send_result(MessageChain.create([
                Plain(f"一次仅可投掷 100 个以内的骰子")
            ]))
        else:
            dice_cnt = int(dice_cnt_str)

        if not dice_max_str:
            single_dice_max = 100
        elif int(dice_max_str) > 1000:
            return await event.send_result(MessageChain.create([
                Plain(f"仅可投掷 1000 面以下的骰子")
            ]))
        else:
            single_dice_max = int(dice_max_str)

        if not max_cnt_str:
            max_cnt = 0
        elif int(max_cnt_str) > dice_cnt:
            return await event.send_result(MessageChain.create([
                Plain(f"你输入的值有误，取最大数{max_cnt_str} 不可大于总骰子数 {dice_cnt_str}")
            ]))
        else:
            max_cnt = int(max_cnt_str)

        dice_list = []
        for _ in range(dice_cnt):
            current_val = random.randint(1, single_dice_max)
            dice_list.append(current_val)

        if max_cnt_str:
            max_dice = heapq.nlargest(max_cnt, dice_list)
            num_list_new = map(lambda x: str(x), max_dice)
            max_dice_str = ", ".join(num_list_new)
            dice_sum = sum(max_dice)
            await event.send_result(MessageChain.create([
                Plain(
                    f"你投出 {dice_cnt} 个骰子\n其中最大的 {max_cnt} 个为：{max_dice_str}\n它们的和为 {dice_sum}")
            ]))
        elif dice_cnt == 1:
            await event.send_result(MessageChain.create([
                Plain(f"你投出 1 个骰子\n它的值为 {dice_list[0]}")
            ]))
        else:
            dice_list_new = map(lambda x: str(x), dice_list)
            dice_list_str = ", ".join(dice_list_new)
            dice_sum = sum(dice_list)
            await event.send_result(MessageChain.create([
                Plain(f"你投出 {dice_cnt} 个骰子\n他们分别为：{dice_list_str}\n它们的和为：{dice_sum}")
            ]))
