# special thanks to Sur_vivor
# Re-written for Lucifer by @its_xditya

import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Lucifer import CMD_HELP
from Lucifer.init import StartTime
from Lucifer.plugins import ALIVE_NAME, OWNER_ID

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓυcιғεя υsεя"



# @command(pattern="^.ping$")


@Lucifer.on(admin_cmd(pattern="ping$"))
@Lucifer.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴋʏᴀ ᴅᴇᴋʜ ʀʜᴀ ʜᴀɪ ʙsᴅᴋ 👀")
    delta_ping = time() - start
    await message.reply_photo(
        photo=f"https://telegra.ph/file/42a423c45e4146cf8a94c.mp4",
        caption=f"𝗣𝗢𝗡𝗚 🎉!! \n" f"`{delta_ping * 1000:.3f} ᴍs`\n 𝗠𝗬 𝗦𝗪𝗘𝗘𝗧𝗛𝗘𝗔𝗥𝗧 𝗠𝗔𝗦𝗧𝗘𝗥 :  [{DEFAULTUSER}](tg://user?id={OWNER_ID})",
        reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton(text="👥 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/dominator_bot_support"),
                InlineKeyboardButton(text="📣 ᴄʜᴀɴɴᴇʟ", url="https://t.me/dominator_bot_official"),
            ]
        ]
     ),
  ) 




CMD_HELP.update({"ping": ".ping\nUse - See the ping stats and uptime of userbot."})
