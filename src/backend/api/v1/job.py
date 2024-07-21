from uuid import UUID
from fastapi import APIRouter, Body
from backend.database.models.job import JobBase, Job
from backend.services import JobService
from backend.schemas import UnifiedResponseModel, JobCreateReq, JobUpdateReq, JobSelectReq

router = APIRouter()

@router.get("/job", response_model=UnifiedResponseModel[list[JobBase]])
async def get_all_job():
    return await JobService.get_job()

@router.post("/job", response_model=UnifiedResponseModel[JobBase])
async def create_job(req: JobCreateReq):
    job = Job(**req.dict())
    return await JobService.create_job(job)

@router.put("/job", response_model=UnifiedResponseModel[JobBase])
async def update_job(req: JobUpdateReq):
    return await JobService.update_job(req)

@router.delete("/job", response_model=UnifiedResponseModel[JobBase])
async def delete_job(id: UUID):
    return await JobService.delete_job(id)

@router.post("/job/filter", response_model=UnifiedResponseModel[list[JobBase]])
async def filter_job_by_field(req: JobSelectReq):
    return await JobService.select_job_by_fields(req)

@router.post("/job/sort", response_model=UnifiedResponseModel[list[JobBase]])
async def sort_job_by_field(field: str):
    return await JobService.get_sort_by_field(field)