import graphene
from app.api.interfaces import GlobalInterface


class DashboardInterface(GlobalInterface):
    """Interface for objects related to dashboards.

    This interface extends the `GlobalInterface` interface and includes all of its fields
    and resolvers. It can be implemented by GraphQL types that represent the
    abstract implementation of AnalyticsDashboard and BalanceDashboard in 
    the GraphQL Query Language.
    """
