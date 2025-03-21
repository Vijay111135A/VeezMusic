from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention} !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝚊𝚕𝚕𝚘𝚠𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚙𝚕𝚊𝚢 𝚖𝚞𝚜𝚒𝚌 𝚘𝚗 𝚐𝚛𝚘𝚞𝚙𝚜 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚝𝚑𝚎 𝚗𝚎𝚠 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖'𝚜 𝚟𝚘𝚒𝚌𝚎 𝚌𝚑𝚊𝚝𝚜 𝚙𝚘𝚠𝚎𝚛 𝚋𝚢 𝚙𝚢𝚝𝚐𝚌𝚊𝚕𝚕𝚜 !**

⚡ ** ɪ ᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴠᴇʀʏ ꜰᴀsᴛ ᴀɴᴅ sᴍᴏᴏᴛʜʟʏ.. >> ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ @Attitude_king_vj !**

❔ ** 𝘛𝘰 𝘬𝘯𝘰𝘸 𝘩𝘰𝘸 𝘵𝘰 𝘶𝘴𝘦 𝘵𝘩𝘪𝘴 𝘣𝘰𝘵, 𝘫𝘶𝘴𝘵 𝘤𝘭𝘪𝘤𝘬 𝘰𝘯 𝘵𝘩𝘦 » 😢 𝘉𝘢𝘴𝘪𝘤 𝘎𝘶𝘪𝘥𝘦 𝘣𝘶𝘵𝘵𝘰𝘯 !**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group 😁",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("😢 Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("🤔 Commands", url=f"https://t.me/tgcalls_Music_update/10"),
                    InlineKeyboardButton("👩‍💻 Developer", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "🔥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🔖 log channel", url="https://github.com/levina-lab/VeezMusic"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ PyTgGroup", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 PytgChannel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing music on your Group voice chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Hello** {message.from_user.mention()} !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="❓ Basic Guide", callback_data="cbguide")]]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("📌 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
