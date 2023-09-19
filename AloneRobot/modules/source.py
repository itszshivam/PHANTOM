from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from AloneRobot import OWNER_ID, dispatcher
from AloneRobot import pbot as client

Alone = "https://graph.org/file/db758905c11768d49f8ee.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Alone,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [𝗥𝗢𝗖𝗞𝗬](https://t.me/ROCKY_ISS_BACK)♨️
  
╚═════ஜ۩۞۩ஜ════╝

**[𝗫𝗗 𝗥𝗢𝗕𝗢𝗧](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴛ ᴩᴜʙʟɪᴄ ʙᴜᴛ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ᴍʏ ᴏᴡɴᴇʀ ғᴏʀ sᴏᴜʀᴄᴇ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴏᴡɴᴇʀ•", url="https://t.me/ROCKY_ISS_BACK"
                    ),
                    InlineKeyboardButton(
                        "•xᴅ•", url="https://t.me/XD_NETWORKS"
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
