# special thanks to Sur_vivor
# Re-written for Lucifer by @its_xditya

import time
from datetime import datetime
from pyrogram import Client, filters
from Lucifer import CMD_HELP
from Lucifer.init import StartTime
from Lucifer.plugins import ALIVE_NAME, OWNER_ID

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓυcιғεя υsεя"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


# @command(pattern="^.ping$")


@Lucifer.on(admin_cmd(pattern="ping$"))
@Lucifer.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢ..... 👀")
    delta_ping = time() - start
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2256701b54c183ab45e11.jpg",
        caption=f"ᴘ ᴏ ɴ ɢ ! " f"`{delta_ping * 1000:.3f} ᴍs`\n✘ 💖υρтιмє💖 : {uptime}\n✘ 𝐌𝐘 𝐏𝐄𝐑𝐎 𝐌𝐀𝐒𝐓𝐄𝐑 : [{DEFAULTUSER}](tg://user?id={OWNER_ID})\n\n© [𝙻ucifer 𝚇 𝚄𝚂𝙴𝚁𝙱𝙾𝚃](https://t.me/dominator_bot_official)"")





CMD_HELP.update({"ping": ".ping\nUse - See the ping stats and uptime of userbot."})
