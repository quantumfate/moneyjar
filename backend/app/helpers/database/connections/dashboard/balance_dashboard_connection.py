from app import db
from app.helpers.database import Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class BalanceDashboardConnection(db.Model):
    __tablename__ = 'dashboard_facade'

    allocation_facade_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
