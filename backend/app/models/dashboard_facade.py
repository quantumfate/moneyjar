from typing import List, Tuple

from app.helpers.database import DashboardFacadeConnection, db
from app.models import AnalyticsDashboard, BalanceDashboard
from graphene import Field, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.dialects.postgresql import UUID


class DashboardFacade(SQLAlchemyObjectType):
    """
    A GraphQL object type that represents a dashboard facade in the system.

    A dashboard facade is a higher-level abstract dashboard that manages and
    controls multiple dashboards. It is used to provide a unified view of
    different dashboards and to abstract away the underlying implementation
    details of each dashboard. The dashboard facade also creates an instance of
    `AllocationFacade`.

    This class defines the structure and relationships of the GraphQL object
    type and maps it to the corresponding dashboard facade model in the database.
    It defines the `allocation_facade` and `dashboards` fields, which are
    exposed in the GraphQL API by the `DashboardFacadeSchema` class.
    """
    class Meta:
        model = DashboardFacadeConnection
        interfaces = (ObjectType,)
    

    dashbord_facade_id = Field(UUID, required=True)
    dashboards: List[Tuple[AnalyticsDashboard, BalanceDashboard]] = db.relationship("AbstractDashboard", backref="facade", lazy=True)