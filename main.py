import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

app = Client(
    "BennBickmanBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Guide (In progress)", callback_data="guide")],
        [
            InlineKeyboardButton("Updates", url="https://t.me/bennbickman_offical"),
            InlineKeyboardButton("Support", url="https://t.me/bennbickman_support")
        ],
        [InlineKeyboardButton("Add Me", url=f"https://t.me/{client.me.username}?startgroup=true")]
    ])
    
    text = (
        f"☠️ Ahoy, {message.from_user.mention}!\n\n"
        "**I'm Benn Beckman**, your pirate crew's strategic commander! 🧠🏴‍☠️\n\n"
        "Use /help to see all my commands and start earning 🪙 doubloons!"
    )

    await message.reply_text(text, reply_markup=buttons)

@app.on_callback_query(filters.regex("guide"))
async def guide_callback(client, callback_query):
    await callback_query.answer("Guide is still in progress!", show_alert=True)

app.run()