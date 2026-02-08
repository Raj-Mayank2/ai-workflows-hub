from fastapi import APIRouter, UploadFile, File
import os

from app.services.parser import extract_name, extract_email
from app.services.jd_parser import parse_job_description
from app.services.scorer import final_score, calculate_profile_bonus
from app.models.match_request import MatchRequest
from app.services.ai_matcher import compute_semantic_similarity
from app.services.resume_store import save_resume, get_resume, get_all_resumes
import csv
from fastapi.responses import FileResponse



from app.services.extractor import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from app.services.parser import (
    extract_skills,
    extract_experience,
    extract_education,
    extract_cgpa,
    extract_hackathons,
    extract_achievements,
    extract_coding_profiles,
    extract_links,
    extract_projects_count,
    extract_certifications
)

resume_router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ---------------- UPLOAD RESUME ---------------- #

@resume_router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    if file.filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file.filename.lower().endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        return {"error": "Only PDF and DOCX files are supported"}

    parsed_data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "filename": file.filename,
        "skills": extract_skills(text),
        "experience_years": extract_experience(text),
        "education": extract_education(text),
        "cgpa": extract_cgpa(text),
        "hackathons_count": extract_hackathons(text),
        "achievements": extract_achievements(text),
        "coding_profiles": extract_coding_profiles(text),
        "links": extract_links(text),
        "projects_count": extract_projects_count(text),
        "certifications": extract_certifications(text),
        "resume_text": text
    }

    resume_id = save_resume(parsed_data)

    return {
        "resume_id": resume_id,
        "name": parsed_data["name"],
        "email": parsed_data["email"],
        "message": "Resume parsed and stored successfully"
    }


# ---------------- MATCH SINGLE RESUME WITH JD ---------------- #

@resume_router.post("/match")
async def match_resume_with_jd(payload: MatchRequest):

    stored_resume = get_resume(payload.resume_id)

    if not stored_resume:
        return {"error": "Invalid resume_id"}

    jd_data = parse_job_description(payload.job_description)

    rule_result = final_score(
        resume_data=stored_resume,
        jd_data=jd_data
    )

    ai_score = compute_semantic_similarity(
        stored_resume["resume_text"],
        payload.job_description
    )

    bonus = calculate_profile_bonus(stored_resume)

    combined_score = round(
        (0.5 * ai_score) +
        (0.25 * rule_result["skill_match"]) +
        (0.15 * rule_result["experience_match"]) +
        (0.10 * bonus),
        2
    )

    return {
        "resume_id": payload.resume_id,
        "name": stored_resume["name"],
        "email": stored_resume["email"],
        "job_requirements": jd_data,
        "ai_score": ai_score,
        "skill_match": rule_result["skill_match"],
        "experience_match": rule_result["experience_match"],
        "bonus_score": bonus,
        "final_score": combined_score,
        "status": rule_result["status"]
    }


# ---------------- RANK ALL CANDIDATES ---------------- #

@resume_router.post("/rank")
async def rank_candidates(job_description: str):

    resumes = get_all_resumes()

    if not resumes:
        return {"message": "No resumes uploaded"}

    jd_data = parse_job_description(job_description)

    ranked_list = []

    for resume_id, resume_data in resumes.items():

        rule_result = final_score(
            resume_data=resume_data,
            jd_data=jd_data
        )

        ai_score = compute_semantic_similarity(
            resume_data["resume_text"],
            job_description
        )

        bonus = calculate_profile_bonus(resume_data)

        combined_score = round(
            (0.5 * ai_score) +
            (0.25 * rule_result["skill_match"]) +
            (0.15 * rule_result["experience_match"]) +
            (0.10 * bonus),
            2
        )

        ranked_list.append({
            "resume_id": resume_id,
            "name": resume_data["name"],
            "email": resume_data["email"],
            "final_score": combined_score,
            "ai_score": ai_score,
            "skill_match": rule_result["skill_match"],
            "experience_match": rule_result["experience_match"],
            "bonus_score": bonus,
            "status": rule_result["status"]
        })

    ranked_list.sort(key=lambda x: x["final_score"], reverse=True)

    return ranked_list


@resume_router.post("/export")
async def export_ranked_candidates(job_description: str):

    resumes = get_all_resumes()

    if not resumes:
        return {"message": "No resumes uploaded"}

    jd_data = parse_job_description(job_description)

    ranked_list = []

    for resume_id, resume_data in resumes.items():

        rule_result = final_score(
            resume_data=resume_data,
            jd_data=jd_data
        )

        ai_score = compute_semantic_similarity(
            resume_data["resume_text"],
            job_description
        )

        bonus = calculate_profile_bonus(resume_data)

        combined_score = round(
            (0.5 * ai_score) +
            (0.25 * rule_result["skill_match"]) +
            (0.15 * rule_result["experience_match"]) +
            (0.10 * bonus),
            2
        )

        ranked_list.append({
            "resume_id": resume_id,
            "name": resume_data.get("name"),
            "email": resume_data.get("email"),
            "final_score": combined_score,
            "status": rule_result["status"]
        })

    ranked_list.sort(key=lambda x: x["final_score"], reverse=True)

    file_path = "ranked_candidates.csv"

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=ranked_list[0].keys())
        writer.writeheader()
        writer.writerows(ranked_list)

    return FileResponse(
        path=file_path,
        filename="ranked_candidates.csv",
        media_type="text/csv"
    )
