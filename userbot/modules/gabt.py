from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.ohayou(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`ohayou Sekai`")
    sleep(3)
    await typew.edit("`Morning Lord`")
    sleep(1)
    await typew.edit("`Ohayou Sekai Morning Lord:)`")
# @salama219


@register(outgoing=True, pattern='^.syg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Sayang aku`")
    sleep(3)
    await typew.edit("`Cuma mau bilang`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
    sleep(2) 
    await typew.edit("`Jangan Tinggalin aku ya`")
# @salama219


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Tetap Semangat`")
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# @salama219


@register(outgoing=True, pattern='^.mantan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`HAI MANTAN 🙂`")
    sleep(1)
    await typew.edit("`BERUBAH KARENA DIA`")
    sleep(1)
    await typew.edit("`ALASAN BANYAK`")
    sleep(1)
    await typew.edit("`SOK SIBUK`")
    sleep(1)
    await typew.edit("`JAWAB SINGKAT AMAT PAS BELUM PUTUS`")
    sleep(1)
    await typew.edit("`KAU PERGI DENGANNYA`")
    sleep(1)
    await typew.edit("`SUNGGUH TEGA`")
    sleep(1)
    await typew.edit("`AKU LIAT KAU BERDUAAN 🙃`")
    sleep(1)
    await typew.edit("`KAN KEINGET LAGI MASA SAKITNYA `")
    sleep(1)
    await typew.edit("`CUMA MANTAN AJAPUN 😂`")
    sleep(3)
    await typew.edit("`😁`")
    sleep(2)
    await typew.edit("`MANTAN KEKASIH GELAP`")
    sleep(2)
    await typew.edit("`😂`")


@register(outgoing=True, pattern='^.sedih(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`AKU SEDIH LOH `")
    sleep(1)
    await typew.edit("`KAU SEDIH GAK?`")
    sleep(1)
    await typew.edit("`🥺🥺🥺`")
    sleep(1)
    await typew.edit("`🥺🥺`")
    sleep(1)
    await typew.edit("`😭🙃`")
    sleep(1)
    await typew.edit("`😭😭😭😭`")
    sleep(1)
    await typew.edit("`SUNGGUH TEGA`")
    sleep(1)
    await typew.edit("`AKU LIAT KAU BERDUAAN😭`")
    sleep(1)
    await typew.edit("`🙂🙃😭`")
    sleep(1)
    await typew.edit("`🥺😭🥺😭🥺😭🥺`")
# Create by myself @localheart

@register(outgoing=True, pattern='^.salam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Bismillah semoga diterima salamnya`")
    sleep(1)
    await typew.edit("`Assalammuallaikum😊😊`")


@register(outgoing=True, pattern='^.jawab(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Eh lupa jawab salam maaf atuh`")
    sleep(1)
    await typew.edit("`Walaikumsalam😊`")
# Create by myself @localheart

@register(outgoing=True, pattern="^.pantun$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        sleep(1)
        await e.edit("I LOVEE YOUUU 💕")
        sleep(2)
        await e.edit("IKAN HIU")
        sleep(2)
        await e.edit("MAKAN ULAR")
        sleep(2)
        await e.edit("EH SALAH APA YA LUPA TADI")
        sleep(2)
        await e.edit("EH GOBLOK")
        sleep(2)
        await e.edit("LU GOBLOK")
        sleep(1)
        await e.edit("BUAT PARA CEWEK ILOVE U😍")
        sleep(2)
        await e.edit("JANGAN PERNAH BILANG ADA YANG MENYAKITIMU")
        sleep(2)
        await e.edit("NANTI ORANG ITU AKAN HILANG")
        sleep(2)
        await e.edit("MAU GA JADI PACARKU")
        sleep(1)
        await e.edit("TETAP DISINI")
        sleep(2)
        await e.edit("TENAMANI AKU")
        sleep(1)
        await e.edit("SEPANJANG HIDUPKUUU")
        sleep(2)
        await e.edit("PERCAYALAH KUAKAN SELINGKUH 💕")
        sleep(1)
        await e.edit("MENDUAKANMU")
        sleep(2)
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("KAMU")
        sleep(1)
        await e.edit("SAYANG")
        sleep(1)
        await e.edit("YOK GASKANNNN")
        sleep(2)
        await e.edit("I LOVE YOUUUU")
        sleep(1)
        await e.edit("MY BABY")
        sleep(1)
        await e.edit("💕💞💘💝")
        sleep(1)
        await e.edit("💘💕💞💝")
        sleep(1)
        await e.edit("MUACH MUACH😍😁💞")


@register(outgoing=True, pattern='^.galau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(5)
    await typew.edit("`🎸 JRENG JRENG JRENG `")
    sleep(3)
    await typew.edit("`KUMOHON KAU MENGERTI COBALAH KAU TAMBAHKAN HATI`")
    sleep(2)
    await typew.edit("`🎸 MUNGKIN DISAAT INI CINTA KITA SEDANG DIUJI `")
    sleep(2)
    await typew.edit("`TABAHKANLAH HATIMU OLEH SIKSA ORANG TUAMU `")
    sleep(2)
    await typew.edit("`🎸 KUYAKIN KITA MAMPU BILA KITA SALING MENUNGGU `")
    sleep(2)
    await typew.edit("`KU KAN SELALU SENANG MENUNGGU (WALAU HANYA KEKASIH GELAP MU`")
    sleep(2)
    await typew.edit("`🎸 SAD YA SEBAGAI SIMPANAN `")
    sleep(2)
    await typew.edit("`DAHLA MALES 🙂`")


@register(outgoing=True, pattern='^.sad(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` MARI KITA NANGIS-NANGIS BUAT YANG LAGI PATAH HATI/BROKENHOME `")
    sleep(2)
    await typew.edit("`1`")
    sleep(2)
    await typew.edit("` 2 `")
    sleep(2)
    await typew.edit("` 3 `")
    sleep(2)
    await typew.edit("` 🥺 `")
    sleep(2)
    await typew.edit("`😭`")
    sleep(2)
    await typew.edit("`🥺`")
    sleep(2)
    await typew.edit("`😭`")


@register(outgoing=True, pattern='^.wkwk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` 😂 `")
    sleep(1)
    await typew.edit("`🤣`")
    sleep(1)
    await typew.edit("` 😁 `")
    sleep(1)
    await typew.edit("` 😅`")
    sleep(1)
    await typew.edit("`😄`")
    sleep(2)
    await typew.edit("`😀`")
    sleep(1)
    await typew.edit("`😆`")
    sleep(1)
    await typew.edit("`😓`")
# Create by myself @localheart

@register(outgoing=True, pattern='.melamar(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` AKU ADALAH KAMU  `")
    sleep(1)
    await typew.edit("`AKU INGIN MENJADI TEMAN HIDUP UNTUKMU`")
    sleep(2)
    await typew.edit("` MAU GAK KALAU GAK MAU AKU TARIK LAGI KATA NYA `")
    sleep(2)
    await typew.edit("`KALAU MAU MAH TROBOS AJA`")
    sleep(3)
    await typew.edit("`😄`")
    sleep(2)
    await typew.edit("`BISMILAH`")
    sleep(3)
    await typew.edit("`KUCINTAI DIRIMU SEKARANG DENGAN SAH`")
    sleep(1)
    await typew.edit("`DILAN 1990`")
# Create by myself @localheart

@register(outgoing=True, pattern='.buaya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`KAMU MAU LIHAT BUAYA `")
    sleep(1)
    await typew.edit("`INISIAL R 🐊`")
    sleep(1)
    await typew.edit("` INISIAL V 🦎 `")
    sleep(1)
    await typew.edit("`INISIAL I 👌`")
    sleep(1)
    await typew.edit("`INISIAL D 🐊🦎`")
    sleep(2)
    await typew.edit("`C 🐊 DARAT`")
    sleep(1)
    await typew.edit("`U🦎 LAUT`")
    sleep(1)
    await typew.edit("`ITULAH BUAYA BUAYA HATI HATI YA 😁`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.yang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("` Sayang udah makan? `")
    sleep(1)
    await typew.edit("`Apa Kabar mu`")
    sleep(1)
    await typew.edit("` Kuharap  `")
    sleep(1)
    await typew.edit("` kau`")
    sleep(1)
    await typew.edit("`Baik-baik saja`")
    sleep(2)
    await typew.edit("`Aku sayang kamu`")
    sleep(1)
    await typew.edit("`Tapi kamu nya tidak`")
    sleep(1)
    await typew.edit("`Semoga engkau baik baik saja meski tak kumiliki.`")
# Create by myself @localheart

@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart

CMD_HELP.update({
    "sad":
    "`.ohayou` ; `.sadboy`\
    \nUsage: ntahlah gabut doang.\
    \n\n`.syg`\
    \nUsage: buat bercanda\
    \n\n`.semangat`\
    \nUsage: untuk memberi semangat\
    \n\n`.mantan`\
    \nUsage: saat keinget mantan\
    \n\n`.sedih`\
    \nUsage: tiba-tiba sedih\
    \n\n`.salam`\
    \nUsage: untuk memberi salam\
    \n\n`.jawab`\
    \nUsage: untuk menjawab salam\
    \n\n`.pantun`\
    \nUsage: auk dah iseng doang\
    \n\n`.galau`\
    \nUsage: liat aja sendiri\
    \n\n`.sad`\
    \nUsage: pokok nya sad:v\
    \n\n`.wkwk`\
    \nUsage: ketawa\
    \n\n`.melamar`\
    \nUsage: untuk melamar kamu\
    \n\n`.buaya`\
    \nUsage: untuk jadi buaya.\
    \n\n`.yang`\
    \nUsage: iseng doang:v"
})




