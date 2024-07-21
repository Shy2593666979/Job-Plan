from datetime import datetime
from typing import Optional, List, Union, Tuple
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, select, delete
from sqlalchemy import JSON, Column, DateTime, Text, and_, func, or_, text
from sqlalchemy import JSON, Column, DateTime
from backend.database.base import session_getter

class JobBase(SQLModel):
    id: Optional[UUID] = Field(nullable=True, primary_key=True, description="唯一ID")
    name: str = Field(nullable=True, sa_column=Column(Text), description="职位的名称")
    company: str = Field(nullable=True, sa_column=Column(Text), description="职位对应的企业")
    education: str = Field(default="不限学历", sa_column=Column(Text), description="职位要求的最低学历")
    address: str = Field(default="地球某处", sa_column=Column(Text), description="职位对应的地址")
    experience: str = Field(default="不限经验", sa_column=Column(Text), description="职位要求的最低工作经验")
    require_skill: str = Field(nullable=True, sa_column=Column(Text), description="职位要求的技术")
    require_person: int = Field(default=1, sa_column=Column(Text), description="职位招聘的人数")
    original_url: str = Field(default="", sa_column=Column(Text), description="职位对应的原链接")
    type: str = Field(nullable=True, sa_column=Column(Text), description="职位对应的年限招聘信息")
    deadline: str = Field(default="全年可投", sa_column=Column(Text), description="职位对应的截止时间")
    create_time: datetime = Field(sa_column=Column(DateTime, nullable=False, index=True, server_default=text('CURRENT_TIMESTAMP')), description="添加该职位的时间")

class Job(JobBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)

class JobDao(Job):
    
    @classmethod
    def create_job(cls, data: Job) -> Job:
        with session_getter() as session:
            session.add(data)
            session.commit()
            session.refresh(data)
            return data    
    
    @classmethod
    def update_job(cls, data: Job) -> Job:
        with session_getter() as session:
            session.add(data)
            session.commit()
            session.refresh(data)
            return data
    
    @classmethod
    def delete_job_by_id(cls, id: UUID) -> Job:
        with session_getter() as session:
            statement = delete(Job).where(Job.id == id)
            session.exec(statement)
            session.commit()
    
    @classmethod
    def select_job_by_name(cls, name: str) -> Job:
        with session_getter() as session:
            statement = select(Job).where(Job.name.like(f"%{name}%"))
            return session.exec(statement).all()
    
    @classmethod
    def select_job_by_company(cls, company: str) -> Job:
        with session_getter() as session:
            statement = select(Job).where(Job.company == company)
            return session.exec(statement).all()
    
    @classmethod
    def select_job_by_address(cls, address: str) -> Job:
        with session_getter() as session:
            statement = select(Job).where(Job.address == address)
            return session.exec(statement).all()
    
    @classmethod
    def select_job_by_type(cls, type: str) -> Job:
        with session_getter() as session:
            statement = select(Job).where(Job.type == type)
            return session.exec(statement).all()
    
    @classmethod
    def select_job_by_id(cls, id: UUID) -> Job:
        with session_getter() as session:
            statement = select(Job).where(Job.id == id)
            return session.exec(statement).first()
    
    @classmethod
    def select_job_by_fields(cls, name: str = None, company: str = None,
                            address: str = None, type: str = None,
                            id: str = None) -> Job:
        with session_getter() as session:
            conditions = []
            if name is not None:
                conditions.append(Job.name == name)
            if company is not None:
                conditions.append(Job.company == company)
            if address is not None:
                conditions.append(Job.address == address)
            if type is not None:
                conditions.append(Job.type == type)
            if id is not None:
                conditions.append(Job.id == id)
            statement = select(Job).where(and_(*conditions))
            return session.exec(statement).all()
        
    @classmethod
    def get_order_job_by_deadline(cls) -> Job:
        with session_getter() as session:
            statement = select(Job).order_by(Job.deadline)
            return session.exec(statement).all()
            
    @classmethod
    def get_order_desc_job_by_deadline(cls) -> Job:
        with session_getter() as session:
            statement = select(Job).order_by(Job.deadline.desc())
            return session.exec(statement).all()
    
    @classmethod
    def get_order_job_by_create_time(cls) -> Job:
        with session_getter() as session:
            statement = select(Job).order_by(Job.create_time)
            return session.exec(statement).all()
        
    @classmethod
    def get_order_desc_job_by_create_time(cls) -> Job:
        with session_getter() as session:
            statement = select(Job).order_by(Job.create_time.desc())
            return session.exec(statement).all()
    
    @classmethod
    def get_order_job_by_require_person(cls) -> Job:
        with session_getter() as session:
            statement = select(Job).order_by(Job.require_person)
            return session.exec(statement).all()
    
    @classmethod
    def get_order_desc_job_by_require_person(cls) -> Job:
        with session_getter() as session:
            statement = select(Job).order_by(Job.require_person.desc())
            return session.exec(statement).all()
            
    @classmethod
    def get_sql_distinct_field(cls, name: str = None, company: str = None,
                               education: str = None, address: str = None,
                               experience: str = None, require_persion: str = None,
                               type: str = None, deadline: str = None) -> Job:
        with session_getter() as sesion:
            if name is not None:
                statement = select(Job.name).distinct()
            if company is not None:
                statement = select(Job.company).distinct()
            if education is not None:
                statement = select(Job.education).distinct()
            if address is not None:
                statement = select(Job.address).distinct()
            if experience is not None:
                statement = select(Job.experience).distinct()
            if require_persion is not None:
                statement = select(Job.require_person).distinct()
            if type is not None:
                statement = select(Job.type).distinct()
            if deadline is not None:
                statement = select(Job.deadline).distinct()
            return sesion.exec(statement).all()