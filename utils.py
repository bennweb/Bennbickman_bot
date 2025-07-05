from datetime import datetime, timedelta
from pyrogram.types import Message
import random

user_cooldowns = {}

def daily_cooldown(user_id):
    now = datetime.utcnow()
    if user_id in user_cooldowns:
        last_used = user_cooldowns[user_id]
        if now - last_used < timedelta(hours=24):
            remaining = timedelta(hours=24) - (now - last_used)
            return False, remaining
    user_cooldowns[user_id] = now
    return True, None

def bet_limit(amount):
    return amount > 0

def xp_required_for_level(level):
    return 100 + (level * 20)

async def send_image_reply(message: Message, image_url: str, caption: str = ""):
    try:
        await message.reply_photo(photo=image_url, caption=caption)
    except Exception:
        await message.reply_text(caption)
