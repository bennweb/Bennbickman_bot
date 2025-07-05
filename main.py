from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.users import (
    get_user, add_xp, get_balance, update_balance, get_sudo, is_sudo,
    store_doubloons, withdraw_doubloons, get_chest, update_level, get_all_users
)
from utils import send_image_reply, daily_cooldown, bet_limit, xp_required_for_level
from datetime import datetime, timedelta
import random, asyncio, os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))

app = Client("bennbickman", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# /start command
@app.on_message(filters.command("start"))
async def start_cmd(_, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates", url="https://t.me/bennbickman_offical"),
         InlineKeyboardButton("Support", url="https://t.me/bennbickman_support")],
        [InlineKeyboardButton("Add Me", url=f"https://t.me/{(await app.get_me()).username}?startgroup=true")]
    ])
    await message.reply_text(
        f"☠️ Ahoy, {message.from_user.first_name}! I'm **Benn Bickman** 🧠 – strategist of Red Hair Pirates!\n\n"
        "💰 Collect doubloons, climb the leaderboard, and rise through the ranks!\n\n"
        "Use /help to see my commands.\n\n⚓",
        reply_markup=keyboard
    )

# /help command
@app.on_message(filters.command("help"))
async def help_cmd(_, message: Message):
    await message.reply_text(
        "🧭 **Benn Bickman Commands:**\n\n"
        "/start - Start the journey\n"
        "/help - Show this help menu\n"
        "/daily - Collect your daily doubloons\n"
        "/balance - Check your balance\n"
        "/gamble <amount> - Try your luck\n"
        "/bet <amount> - Double or nothing\n"
        "/leaderboard - See the top pirates\n"
        "/give <user_id> <amount> - Share wealth (sudo only)\n"
        "/shotgun - Surprise pirate attack!\n"
        "/loot - Try to find treasure"
    )

app.run()
