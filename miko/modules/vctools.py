# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from miko import *
from pytgcalls import GroupCallFactory 

MODULE = "vctools"
HELP = f"""
✘ Bantuan Untuk Voice Chat

๏ Perintah: <code>startvc</code>
◉ Penjelasan: Untuk memulai voice chat grup.

๏ Perintah: <code>stopvc</code>
◉ Penjelasan: Untuk mengakhiri voice chat grup.
           
๏ Perintah: <code>joinvc</code>
◉ Penjelasan: Untuk bergabung voice chat grup.

๏ Perintah: <code>leavevc</code>
◉ Penjelasan: Untuk meninggalkan voice chat grup.
"""


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"No group call Found {err_msg}")
    return False


