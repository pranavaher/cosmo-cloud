import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection settings
MONGODB_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Connect to MongoDB Atlas
client = AsyncIOMotorClient(MONGODB_URL)

# Access a specific database
db = client[DB_NAME]

# Access a specific collection within the database
collection = db[COLLECTION_NAME]
