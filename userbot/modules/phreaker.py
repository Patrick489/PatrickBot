# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Created By @ximfine

from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio
from userbot import bot, CMD_HELP
from userbot.events import register



@register(outgoing=True, pattern=r"^\.nmap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di check!..__")
    await event.edit(f"```Getting info {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/nmap {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.subd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di generate!..__")
    await event.edit(f"```Generated subdomain {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/subdomain {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.cekhttp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan domain yang mau di check!..__")
    await event.edit(f"```Checking Respond {query}..```")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/httpheader {query}")
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @scriptkiddies_bot atau chat dulu")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


CMD_HELP.update({
    "phreaker":
    "\n╭━━━━━━━━━━━━━━━━━━━╮\
\n\n  `.nmap <domain hosts>`\
\n   Usage: to get info bug/host.\
\n\n  `.subd <domain hosts>`\
\n   Usage: to get subdomain bug/host.\
\n\n  `.cekhttp <domain hosts>`\
\n   Usage: to cek respons bug/host.\
\n╰━━━━━━━━━━━━━━━━━━━╯"
})
