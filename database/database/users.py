from .mongo import db

users = db.users

async def get_user(user_id):
    return await users.find_one({"user_id": user_id}) or {}

async def add_xp(user_id, amount):
    await users.update_one({"user_id": user_id}, {"$inc": {"xp": amount}}, upsert=True)

async def get_balance(user_id):
    user = await get_user(user_id)
    return user.get("balance", 0)

async def update_balance(user_id, amount):
    await users.update_one({"user_id": user_id}, {"$set": {"balance": amount}}, upsert=True)

async def store_doubloons(user_id, amount):
    await users.update_one({"user_id": user_id}, {"$inc": {"balance": amount}}, upsert=True)

async def withdraw_doubloons(user_id, amount):
    await users.update_one({"user_id": user_id}, {"$inc": {"balance": -amount}}, upsert=True)

async def update_level(user_id, level):
    await users.update_one({"user_id": user_id}, {"$set": {"level": level}}, upsert=True)

async def get_chest(user_id):
    user = await get_user(user_id)
    return user.get("chest", 0)

async def get_all_users():
    return users.find()

# Sudo-related functions
async def get_sudo():
    return [int(x) for x in (os.getenv("SUDO_USERS") or "").split()]

async def is_sudo(user_id):
    return str(user_id) in os.getenv("SUDO_USERS", "")
