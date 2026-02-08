from pymongo import MongoClient

MONGO_URI = "mongodb+srv://vmayank0123:Mayank84@cluster0.pih8bnx.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["resume_ai"]
resume_collection = db["resumes"]
