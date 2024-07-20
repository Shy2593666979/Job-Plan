import uuid
from backend.database.service import DatabaseService
from sqlmodel import Session
from loguru import logger
from backend.config import settings
from contextlib import contextmanager

db_service: 'DatabaseService' = DatabaseService(settings.database_url)

@contextmanager
def session_getter() -> Session: # type: ignore
    """轻量级session context"""
    try:
        session = Session(db_service.engine)
        yield session
    except Exception as e:
        logger.info('Session rollback because of exception:{}', e)
        session.rollback()
        raise
    finally:
        session.close()

def generate_uuid() -> str:
    """
    生成uuid的字符串
    """
    return uuid.uuid4().hex