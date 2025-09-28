from pydantic import BaseModel
# from typing import Optional

class JobDetailsRequest(BaseModel):
    job_id: str
    job_description: str

class JobDetailsResponse(BaseModel):
    skills: list[str]
    certs: list[str]