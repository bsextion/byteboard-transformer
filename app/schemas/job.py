from pydantic import BaseModel

class JobRequest(BaseModel):
    job_id: str
    job_description: str

class JobResponse(BaseModel):
    job_id: str
    job_description: str
    skills: list[str]
    certs: list[str]