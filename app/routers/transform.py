from fastapi import APIRouter
from app.schemas.job import JobDetailsRequest
from app.schemas.job import JobDetailsResponse

from app.services.transformer import transformDescription

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/transform")
async def transformJobs(jobDetailsRequest: list[JobDetailsRequest]) -> dict[str, JobDetailsResponse]:
    return transformDescription(jobDetailsRequest)