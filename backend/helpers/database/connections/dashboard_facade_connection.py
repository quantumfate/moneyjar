from app import db
from models.dashboard_facade import DashboardFacade
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from database.base import Base

class DashboardFacadeConnection(db.Model):
    __tablename__ = 'dashboard_facade'

    dashboard_facade_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)