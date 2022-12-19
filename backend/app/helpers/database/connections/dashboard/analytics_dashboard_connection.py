from app import db
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class AnalyticsDashboardConnection(db.Model):
    __tablename__ = 'dashboard_facade'

    allocation_facade_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
