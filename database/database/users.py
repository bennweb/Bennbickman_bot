from database.mongo import users

def get_user(user_id):
    user = users.find_one({"_id": user_id})
    if not user:
        users.insert_one({
            "_id": user_id,
            "coins": 100,
            "xp": 0,
            "last_daily": None
        })
        return get_user(user_id)
    return user

def update_user(user_id, field, value):
    users.update_one({"_id": user_id}, {"$set": {field: value}})

def increment_user(user_id, field, amount):
    users.update_one({"_id": user_id}, {"$inc": {field: amount}})
