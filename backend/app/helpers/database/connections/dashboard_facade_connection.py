from app import db
from app.helpers.database import Base
from app.models import DashboardFacade
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class DashboardFacadeConnection(db.Model):
    __tablename__ = 'dashboard_facade'

    dashboard_facade_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
