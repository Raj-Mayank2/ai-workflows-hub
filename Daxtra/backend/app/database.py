from pymongo import MongoClient

MONGO_URI = Your url here

client = MongoClient(MONGO_URI)

db = client["resume_ai"]
resume_collection = db["resumes"]
