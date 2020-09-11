"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/70eab28fecda58256db63.jpg"
pm_caption = "`USERBOT STATUS :` **AKTIF**\n\n"
pm_caption += "**PROFIL PENGGUNA**\n"
pm_caption += "**NAMA** : `AI`\n**A.K.A** : `SEN`\n"
pm_caption += "**DOMISILI**: `KALSEL`\n"
pm_caption += "**JENIS KELAMIN** : `PEREMPUAN`\n"
pm_caption += "**UMUR** : `MASIH MUDA POKOKNYA`\n"
pm_caption += f"**USERNAME** : {DEFAULTUSER} \n"
pm_caption += "**SOSMED** : [TWITTER](https://twitter.com/aisyyynjm) \n"
pm_caption += "__Merupakan CoFounder dari__ @KerabatOnline __Group__ \n\n"
pm_caption += "• [Kerabat Online Channel](https://t.me/KerabatOnline_Ch)\n"
pm_caption += "• [Kerabat Online Moment](https://t.me/KerabatMoment)\n"
pm_caption += "• [Kerabat Online Twitter](https://twitter.com/KerabatOnline)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
