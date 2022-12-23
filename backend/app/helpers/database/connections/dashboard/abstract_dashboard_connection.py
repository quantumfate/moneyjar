import abc

from app.helpers.database.database import Base
from app.models import AbstractDashboard
from graphene import Connection, ConnectionField, Node
from sqlalchemy import Column, MetaData, String, Table, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import expression


class AbstractDashboardConnection(Base, Connection):
    """Abstract class for dashboard connections.

    This class defines the basic structure for dashboard connections and
    provides an abstract method that must be implemented by concrete classes.

    Attributes:
        abstract_balance_id (UUID): A UUID field that is not specified as a primary key.
        Meta: A class that specifies the node for this connection.
    """

    __abstract__ = True

    abstract_dashboard_id = Column(UUID(as_uuid=True), nullable=False)

    class Meta:
        node = AbstractDashboard

    @abc.abstractmethod
    def my_abstract_method(self):
        pass
