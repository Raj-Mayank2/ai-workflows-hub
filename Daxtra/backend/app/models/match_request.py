from pydantic import BaseModel

class MatchRequest(BaseModel):
    resume_id: str
    job_description: str
