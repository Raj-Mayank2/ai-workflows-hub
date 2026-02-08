import spacy
import re

nlp=spacy.load("en_core_web_sm")


SKILL_KEYWORDS=[
    "python", "java", "c++", "javascript", "react", "node",
    "mongodb", "sql", "html", "css", "django", "flask",
    "fastapi", "machine learning", "deep learning",
    "nlp", "git", "docker", "aws","c++","llm","generative-ai","cloud"
]


EDUCATION_KEYWORDS = [
    "b.tech", "bachelor", "b.sc", "b.e",
    "m.tech", "master", "m.sc",
    "phd", "doctorate", "diploma"
]

def extract_skills(text:str):
    text=text.lower()
    return list({skill for skill in SKILL_KEYWORDS if skill in text})

def extract_experience(text: str):
    matches = re.findall(r'(\d+\.?\d*)\s*(years?|yrs?)', text.lower())
    years = [float(m[0]) for m in matches]
    return max(years) if years else 0

def extract_education(text:str):
    text=text.lower()
    return list({edu for edu in EDUCATION_KEYWORDS if edu in text})

def extract_cgpa(text: str):
    text = text.lower()

    match = re.search(
        r'(cgpa|gpa)\s*[:\-]?\s*(\d+\.?\d*)', text
    )
    if match:
        return float(match.group(2))

    match = re.search(r'(\d+\.?\d*)\s*/\s*10', text)
    if match:
        return float(match.group(1))

    return None

def extract_hackathons(text: str):
    keywords = ["hackathon", "ideathon", "coding competition"]
    text = text.lower()

    count = sum(text.count(k) for k in keywords)
    return count


def extract_achievements(text: str):
    achievements = []
    lines = text.split("\n")

    keywords = ["winner", "finalist", "rank", "awarded", "achievement"]

    for line in lines:
        if any(k in line.lower() for k in keywords):
            achievements.append(line.strip())

    return achievements[:5]  # limit noise

def extract_coding_profiles(text: str):
    text = text.lower()

    return {
        "leetcode": "leetcode" in text,
        "codeforces": "codeforces" in text,
        "codechef": "codechef" in text
    }

def extract_links(text: str):
    github = re.search(r'https?://github\.com/\S+', text)
    portfolio = re.search(r'https?://\S+\.(netlify|vercel|github\.io)\.?\S*', text)

    return {
        "github": github.group(0) if github else None,
        "portfolio": portfolio.group(0) if portfolio else None
    }


def extract_projects_count(text: str):
    keywords = ["project", "projects"]
    return sum(text.lower().count(k) for k in keywords)


def extract_certifications(text: str):
    certifications = []
    lines = text.split("\n")

    keywords = ["certified", "certification", "certificate"]

    for line in lines:
        if any(k in line.lower() for k in keywords):
            certifications.append(line.strip())

    return certifications[:5]

import re

def extract_email(text: str):
    match = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
    return match.group(0) if match else None


def extract_name(text: str):
    lines = text.strip().split("\n")
    # Assume first non-empty line is candidate name (common in resumes)
    for line in lines:
        line = line.strip()
        if line and len(line.split()) <= 4:
            return line
    return "Unknown"
