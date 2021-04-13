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


@register(outgoing=True, pattern=r"^\.gen(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan bin yang mau di generate!..__")
    await event.edit(f"```Generated CC {query}..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/gen {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal generate {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.ss(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/ss {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan BIN yang mau di check!..__")
    await event.edit(f"```Checking BIN {query}```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/bin {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Bin {query} Invalid!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.key(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan SK-KEY yang mau di check!..__")
    await event.edit(f"```Checking SK KEY {query}```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/key {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit("SK KEY Invalid!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.ch(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/ch {query}")
            await asyncio.sleep(12)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.vbv(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/vbv {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.pp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/pp {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])


@register(outgoing=True, pattern=r"^\.au(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/au {query}")
            await asyncio.sleep(12)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])

@register(outgoing=True, pattern=r"^\.iban(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Silahkan masukan cc yang mau di check!..__")
    await event.edit("```Checking CC Number..```")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            jemboed = await conv.send_message(f"/iban {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @Carol5_bot atau chat dulu")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Gagal Mengecek {query}!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])

CMD_HELP.update({
    "binner":
    "\n╭━━━━━━━━━━━━━━━━━━━╮\
\n  `.gen`\
\n   Usage: to generate cc with bin.\
\n\n  `.ss`\
\n   Usage: Stripity-Stripe Auth.\
\n\n  `.bin`\
\n   Usage: to cek bin information.\
\n\n  `.key`\
\n   Usage: to check skkey respond.\
\n\n  `.ch`\
\n   Usage: Auth CC LIVE OR DEAD.\
\n\n  `.vbv`\
\n   Usage: CC CHECKER IF ITS VBV OR NOT.\
\n\n  `.pp`\
\n   Usage: Paypal Charge 0.01$.\
\n\n  `.au`\
\n   Usage: Auth CC LIVE OR DEAD.\
\n\n  `.iban`\
\n   Usage: IBAN Checker.\
\n╰━━━━━━━━━━━━━━━━━━━╯"
})








