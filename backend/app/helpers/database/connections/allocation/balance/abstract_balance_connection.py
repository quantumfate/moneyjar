import abc

from app.helpers.database.database import Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class AbstractBalanceConnection(Base):
    __abstract__ = True

    allocation_facade_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
    
    @abc.abstractmethod
    def my_abstract_method(self):
        pass
