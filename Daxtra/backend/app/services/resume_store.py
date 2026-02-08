from bson import ObjectId
from app.database import resume_collection


def save_resume(data):
    result = resume_collection.insert_one(data)
    return str(result.inserted_id)


def get_resume(resume_id):
    resume = resume_collection.find_one({"_id": ObjectId(resume_id)})
    if resume:
        resume["_id"] = str(resume["_id"])
    return resume


def get_all_resumes():
    resumes = {}
    for r in resume_collection.find():
        resumes[str(r["_id"])] = r
    return resumes
