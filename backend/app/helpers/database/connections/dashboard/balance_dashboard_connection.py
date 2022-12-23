from app import db
from app.helpers.database import AbstractDashboardConnection, Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class BalanceDashboardConnection(AbstractDashboardConnection, db.Model):
    """Concrete class for balance dashboard connections.

    This class represents a connection for balance dashboards and inherits
    the structure and abstract method from the AbstractDashboardConnection class.

    Attributes:
        balance_facade_id (UUID): A UUID field that is specified as the primary key.
        __tablename__ (str): The name of the database table for this model.
    """
    __tablename__ = 'dashboard_facade'

    balance_dashboard_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
    def my_abstract_method(self):
        pass
