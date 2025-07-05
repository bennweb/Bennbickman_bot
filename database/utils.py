from datetime import datetime, timedelta
from pyrogram.types import Message
import asyncio
import random

# Cooldown dictionary
user_cooldowns = {}

# Daily cooldown logic
def daily_cooldown(user_id):
    now = datetime.utcnow()
    if user_id in user_cooldowns:
        last_used = user_cooldowns[user_id]
        if now - last_used < timedelta(hours=24):
            remaining = timedelta(hours=24) - (now - last_used)
            return False, remaining
    user_cooldowns[user_id] = now
    return True, None

# Bet limit
def bet_limit(amount):
    if amount <= 0:
        return False
    return True

# XP required per level
def xp_required_for_level(level):
    return 100 + (level * 20)

# Image reply helper
async def send_image_reply(message: Message, image_url: str, caption: str = ""):
    try:
        await message.reply_photo(photo=image_url, caption=caption)
    except Exception:
        await message.reply_text(caption)
