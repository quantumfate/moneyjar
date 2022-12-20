import abc

from app.helpers.database.database import Base
from app.models import AbstractDahboard
from graphene import Connection, ConnectionField, Node
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class AbstractDashboardConnection(Base, Connection):
    __abstract__ = True
    class Meta:
        node = AbstractDahboard
        
    allocation_facade_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
    
    @abc.abstractmethod
    def my_abstract_method(self):
        pass
