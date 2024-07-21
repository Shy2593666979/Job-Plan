from datetime import datetime
from fastapi import Request
from typing import Any, List, Optional
from uuid import UUID
from backend.database.models.job import JobDao, JobBase, Job
from backend.schemas import JobUpdateReq, UnifiedResponseModel, resp_200, resp_500, JobSelectReq
from loguru import logger


class JobService:

    @classmethod
    def get_job(cls) -> UnifiedResponseModel[JobBase]:
        try:
            return JobDao.get_order_desc_job_by_create_time()
        except Exception as err:
            logger.error(err)
            return resp_500(data=err)

    @classmethod
    def create_job(cls, data: Job) -> UnifiedResponseModel[JobBase]:
        try:
            jobSql = JobDao.create_job(data)
            return resp_200(data=JobBase(**jobSql.dict()))
        except Exception as err:
            logger.error(err)
            return resp_500(data=err)

    @classmethod
    def update_job(cls, req: JobUpdateReq) -> UnifiedResponseModel[JobBase]:
        try:
            job = JobDao.select_job_by_id(req.id)
            jobSql = JobDao.update_job(job)
            return resp_200(data=JobBase(**jobSql.dict()))
        except Exception as err:
            logger.error(err)
            return resp_500(data=err)

    @classmethod
    def delete_job(cls, id: UUID) -> UnifiedResponseModel[JobBase]:
        try:
            jobSql = JobDao.delete_job_by_id(id)
            return resp_200(data=JobBase(**jobSql.dict()))
        except Exception as err:
            logger.error(err)
            return resp_500(data=err)

    @classmethod
    def get_sort_by_field(cls, field: str) -> UnifiedResponseModel[JobBase]:
        try:
            if field == "create_time":
                jobSql = JobDao.get_order_job_by_create_time()
            elif field == "deadline":
                jobSql = JobDao.get_order_job_by_deadline()
            elif field == "require_person":
                jobSql = JobDao.get_order_job_by_require_person()
            return resp_200(data=JobBase(**jobSql.dict()))
        except Exception as err:
            logger.error(err)
            return resp_500(data=err)

    @classmethod
    def get_sort_desc_by_field(cls, field: str) -> UnifiedResponseModel[JobBase]:
        try:
            if field == "create_time":
                jobSql = JobDao.get_order_desc_job_by_create_time()
            elif field == "deadline":
                jobSql = JobDao.get_order_desc_job_by_deadline()
            elif field == "require_person":
                jobSql = JobDao.get_order_desc_job_by_require_person()
            return resp_200(data=JobBase(**jobSql.dict()))
        except Exception as err:
            logger.error(err)
            return resp_500(data=err)

    @classmethod
    def select_job_by_fields(cls, data: JobSelectReq) -> UnifiedResponseModel[JobBase]:
        try:
            jobSql = JobDao.select_job_by_fields(**data.dict())
            return resp_200(data=JobBase(**jobSql.dict))
        except Exception as err:
            logger.error(err)
            return resp_500(data=err)
