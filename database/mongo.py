from pymongo import MongoClient

MONGO_URL = "mongodb+srv://itachii130506:W0Qif2solCNPDyUd@bickman.jaumcw3.mongodb.net/?retryWrites=true&w=majority&appName=Bickman"

client = MongoClient(MONGO_URL)
db = client["bennbickman"]

users = db["users"]
