from app.services.parser import extract_skills, extract_experience

def parse_job_description(text:str):
    return{
        "required_skills":extract_skills(text),
        "min_experience":extract_experience(text)
    }