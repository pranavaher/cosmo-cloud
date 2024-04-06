# db.py
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection settings
MONGODB_URL = "mongodb+srv://pranav-cosmocloud:WfJ9y73jeoKA2xbf@cluster0.1tizddf.mongodb.net/"

# Connect to MongoDB Atlas
client = AsyncIOMotorClient(MONGODB_URL)

# Access a specific database
db = client["cosmo-cloud"]

# Access a specific collection within the database
collection = db["student"]
