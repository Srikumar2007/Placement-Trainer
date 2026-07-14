from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import os

async def check_db():
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME = "skillforge"
    client = AsyncIOMotorClient(MONGODB_URL, serverSelectionTimeoutMS=2000)
    db = client[DATABASE_NAME]
    try:
        await client.server_info()
        print("Connected to MongoDB successfully")
        users_count = await db.users.count_documents({})
        if users_count == 0:
            from passlib.context import CryptContext
            from datetime import datetime
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            demo_user = {
                "name": "Sri Kumar",
                "email": "sri@example.com",
                "password_hash": pwd_context.hash("password123"),
                "created_at": datetime.utcnow()
            }
            await db.users.insert_one(demo_user)
            print("Demo user created successfully: sri@example.com / password123")
        else:
            print(f"Users already exist: {users_count}")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

if __name__ == "__main__":
    asyncio.run(check_db())
