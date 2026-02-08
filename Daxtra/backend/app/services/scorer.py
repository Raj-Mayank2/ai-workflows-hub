def calculate_skill_match(resume_skills, jd_skills):
    resume_skills = resume_skills or []
    jd_skills = jd_skills or []

    if not jd_skills:
        return 0

    matched = set(resume_skills).intersection(set(jd_skills))
    return (len(matched) / len(jd_skills)) * 100


def calculate_experience_match(resume_exp, jd_exp):
    resume_exp = resume_exp or 0
    jd_exp = jd_exp or 0

    if jd_exp == 0:
        return 100

    if resume_exp >= jd_exp:
        return 100

    return (resume_exp / jd_exp) * 100


def final_score(resume_data, jd_data):
    resume_skills = resume_data.get("skills", [])
    resume_exp = resume_data.get("experience_years", 0)

    jd_skills = jd_data.get("required_skills", [])
    jd_exp = jd_data.get("min_experience", 0)

    skill_score = calculate_skill_match(resume_skills, jd_skills)
    experience_score = calculate_experience_match(resume_exp, jd_exp)

    score = (0.7 * skill_score) + (0.3 * experience_score)

    if score >= 75:
        status = "Shortlisted"
    elif score >= 50:
        status = "Maybe"
    else:
        status = "Rejected"

    return {
        "score": round(score, 2),
        "skill_match": round(skill_score, 2),
        "experience_match": round(experience_score, 2),
        "status": status
    }

def calculate_profile_bonus(resume_data):

    bonus = 0

    # CGPA bonus
    cgpa = resume_data.get("cgpa")
    if cgpa:
        if cgpa >= 8.5:
            bonus += 5
        elif cgpa >= 7:
            bonus += 3

    # Hackathons (max cap)
    hackathons = resume_data.get("hackathons_count", 0)
    bonus += min(hackathons * 2, 6)

    # Coding profiles
    coding = resume_data.get("coding_profiles", {})
    if any(coding.values()):
        bonus += 2

    # Projects count
    projects = resume_data.get("projects_count", 0)
    if projects >= 3:
        bonus += 2

    return bonus
