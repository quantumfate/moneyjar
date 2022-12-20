from app.models import DashboardFacade
from graphene_sqlalchemy import SQLAlchemyObjectType


class DashboardFacadeSchema(SQLAlchemyObjectType):
    """
    A GraphQL object type that represents a dashboard facade in the system.

    This class defines the GraphQL schema for the dashboard facade and
    maps it to the corresponding dashboard facade model in the database. It
    uses the `SQLAlchemyObjectType` class to automatically generate the
    GraphQL schema based on the fields of the dashboard facade model.
    
    It exposes the `allocation_facade` and `dashboards` fields of the
    `DashboardFacade` model in the GraphQL API.
    """

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = DashboardFacade
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = (
            'allocation_facade_id', 
            'analytics_dashboard_id', 
            'dashbord_dashboard_id', 
            'allocation_facade', 
            'dashboards'
            )
