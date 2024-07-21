from datetime import datetime
from enum import Enum
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from uuid import UUID

from langchain.docstore.document import Document
from orjson import orjson
from pydantic import BaseModel, Field, validator

# 创建泛型变量
DataT = TypeVar('DataT')

class UnifiedResponseModel(Generic[DataT], BaseModel):
    """统一响应模型"""
    status_code: int
    status_message: str
    data: DataT = None

class JobCreateReq(BaseModel):
    name: str = Field(nullable=True, description="职位的名称")
    company: str = Field(nullable=True, description="职位对应的企业")
    education: str = Field(default="不限学历", description="职位要求的最低学历")
    address: str = Field(default="地球某处", description="职位对应的地址")
    experience: str = Field(default="不限经验", description="职位要求的最低工作经验")
    require_skill: str = Field(nullable=True, description="职位要求的技术")
    require_person: int = Field(default=1, description="职位招聘的人数")
    original_url: str = Field(default="",  description="职位对应的原链接")
    type: str = Field(nullable=True, description="职位对应的年限招聘信息")
    deadline: str = Field(default="全年可投", description="职位对应的截止时间")
    
class JobUpdateReq(BaseModel):
    id: UUID = Field(description="职位对应的唯一ID")
    name: str = Field(nullable=True, description="职位的名称")
    company: str = Field(nullable=True, description="职位对应的企业")
    education: str = Field(default="不限学历", description="职位要求的最低学历")
    address: str = Field(default="地球某处", description="职位对应的地址")
    experience: str = Field(default="不限经验", description="职位要求的最低工作经验")
    require_skill: str = Field(nullable=True, description="职位要求的技术")
    require_person: int = Field(default=1, description="职位招聘的人数")
    original_url: str = Field(default="",  description="职位对应的原链接")
    type: str = Field(nullable=True, description="职位对应的年限招聘信息")
    deadline: str = Field(default="全年可投", description="职位对应的截止时间")

class JobSelectReq(BaseModel):
    name: str | None = Field(default=None, max_length=100, description="职位对应的名字")
    company: str | None = Field(default=None, max_length=100, description="职位对应的企业")
    address: str | None = Field(default=None, description="职位对应的地址")
    type: str | None = Field(default=None, description="职位对应的类型,2024秋招 or 2025春招")
    id: UUID | None = Field(default=None, description="职位对应的唯一ID")

def resp_200(data: Union[list, dict, str, Any] = None,
             message: str = 'SUCCESS') -> UnifiedResponseModel:
    """成功的代码"""
    return UnifiedResponseModel(status_code=200, status_message=message, data=data)
    # return data


def resp_500(code: int = 500,
             data: Union[list, dict, str, Any] = None,
             message: str = 'BAD REQUEST') -> UnifiedResponseModel:
    """错误的逻辑回复"""
    return UnifiedResponseModel(status_code=code, status_message=message, data=data)

