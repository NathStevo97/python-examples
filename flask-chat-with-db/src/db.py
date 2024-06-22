import os
from datetime import datetime
from bson import ObjectId
from pymongo import DESCENDING
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv, find_dotenv

from user import User

load_dotenv(find_dotenv())

DB_USERNAME = os.getenv("db_user")
DB_PASSWORD = os.getenv("db_password")
DB_CLUSTER = os.getenv("cluster_name")
DB_NAME = os.getenv("db_name")
APP_NAME = os.getenv("app_name")
DB_COLLECTION = os.getenv("db_collection")
ROOMS_COLLECTION = os.getenv("rooms_collection")
MEMBERS_COLLECTION = os.getenv("members_collection")
MESSAGES_COLLECTION = os.getenv("messages_collection")


client = MongoClient(
    f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_CLUSTER}.yxc1s5a.mongodb.net/?retryWrites=true&w=majority&appName={APP_NAME}",
    server_api=ServerApi("1"),
)

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

chat_db = client.get_database(DB_NAME)
users_collection = chat_db.get_collection(DB_COLLECTION)
rooms_collection = chat_db.get_collection(ROOMS_COLLECTION)
room_members_collection = chat_db.get_collection(MEMBERS_COLLECTION)
messages_collection = chat_db.get_collection("MESSAGES_COLLECTION")


def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    # use _id as the unique key and assign it to the username
    users_collection.insert_one(
        {"_id": username, "email": email, "password": password_hash}
    )


# save_user("nathan", "some@email.com", "test")


def get_user(username):
    user_data = users_collection.find_one({"_id": username})
    return (
        User(user_data["_id"], user_data["email"], user_data["password"])
        if user_data
        else None
    )


# Room Operations


def save_room(room_name, created_by):
    room_id = rooms_collection.insert_one(
        {"name": room_name, "created_by": created_by, "created_at": datetime.now()}
    ).inserted_id
    add_room_member(room_id, room_name, created_by, created_by, is_room_admin=True)
    return room_id


def update_room(room_id, room_name):
    rooms_collection.update_one(
        {"_id": ObjectId(room_id)}, {"$set": {"name": room_name}}
    )
    room_members_collection.update_many(
        {"_id.room_id": ObjectId(room_id)}, {"$set": {"room_name": room_name}}
    )


def get_room(room_id):
    return rooms_collection.find_one({"_id": ObjectId(room_id)})


def add_room_member(room_id, room_name, username, added_by, is_room_admin=False):
    room_members_collection.insert_one(
        {
            "_id": {"room_id": ObjectId(room_id), "username": username},
            "room_name": room_name,
            "added_by": added_by,
            "added_at": datetime.now(),
            "is_room_admin": is_room_admin,
        }
    )


def add_room_members(room_id, room_name, usernames, added_by):
    room_members_collection.insert_many(
        [
            {
                "_id": {"room_id": ObjectId(room_id), "username": username},
                "room_name": room_name,
                "added_by": added_by,
                "added_at": datetime.now(),
                "is_room_admin": False,
            }
            for username in usernames
        ]
    )


def remove_room_members(room_id, usernames):
    room_members_collection.delete_many(
        {
            "_id": {
                "$in": [
                    {"room_id": ObjectId(room_id), "username": username}
                    for username in usernames
                ]
            }
        }
    )


def get_room_members(room_id):
    return list(room_members_collection.find({"_id.room_id": ObjectId(room_id)}))


def get_rooms_for_user(username):
    return list(room_members_collection.find({"_id.username": username}))


def is_room_member(room_id, username):
    return room_members_collection.count_documents(
        {"_id": {"room_id": ObjectId(room_id), "username": username}}
    )


def is_room_admin(room_id, username):
    return room_members_collection.count_documents(
        {
            "_id": {"room_id": ObjectId(room_id), "username": username},
            "is_room_admin": True,
        }
    )


def save_message(room_id, text, sender):
    messages_collection.insert_one(
        {
            "room_id": room_id,
            "text": text,
            "sender": sender,
            "created_at": datetime.now(),
        }
    )


MESSAGE_FETCH_LIMIT = 3


def get_messages(room_id, page=0):
    offset = page * MESSAGE_FETCH_LIMIT
    messages = list(
        messages_collection.find({"room_id": room_id})
        .sort("_id", DESCENDING)
        .limit(MESSAGE_FETCH_LIMIT)
        .skip(offset)
    )
    for message in messages:
        message["created_at"] = message["created_at"].strftime("%d %b, %H:%M")
    return messages[::-1]
