# special thanks to Sur_vivor
# Re-written for Lucifer by @its_xditya

import time
from datetime import datetime

from Lucifer import CMD_HELP
from Lucifer.__init__ import StartTime
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


# @command(pattern="^.lping$")


@Lucifer.on(admin_cmd(pattern="lping$"))
@Lucifer.on(sudo_cmd(pattern="lping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    x = await eor(event, "`❝❄ᑭ♨ɳց…!❄❞´")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    await x.edit(
        f"[LUCIFER](https://telegra.ph/file/42a423c45e4146cf8a94c.mp4)\n\n█████████\n█▄█████▄█\n█▼▼▼▼▼\n█🔥Luciferβօէ įʂ ටղƑìɾҽ🔥\n█▲▲▲▲▲\n█████████\n██ ██\n\n✘ **ριиg** : `{ms}`\n✘ **υρтιмє** : `{uptime}`\n✘ **𝐌𝐘 𝐏𝐄𝐑𝐎 𝐌𝐀𝐒𝐓𝐄𝐑** : [{DEFAULTUSER}](tg://user?id={OWNER_ID})\n😎𝗖𝗥𝗘𝗔𝗧𝗢𝗥😎    : [Ꭰօʍìղąէօɾ](https://t.me/dominator_bot_official)\n\n[© 𝙻ucifer 𝚇 𝚄𝚂𝙴𝚁𝙱𝙾𝚃](https://t.me/dominator_bot_official)"
    )


CMD_HELP.update({"lping": ".lping\nUse - See the lping stats and uptime of userbot."})
