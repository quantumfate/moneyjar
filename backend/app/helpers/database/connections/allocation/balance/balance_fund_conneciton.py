from app import db
from app.helpers.database import AbstractBalanceConnection, Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class BalanceFundConnection(AbstractBalanceConnection,db.Model):
    __tablename__ = 'dashboard_facade'

    allocation_facade_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
    def my_abstract_method(self):
        pass
