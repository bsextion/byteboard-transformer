from fastapi import APIRouter
from app.schemas.job import JobRequest,JobResponse

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/transform")
async def transformJobs(jobs: list[JobRequest]):
    return []