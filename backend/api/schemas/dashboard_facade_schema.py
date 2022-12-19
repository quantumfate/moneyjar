from graphene_sqlalchemy import SQLAlchemyObjectType

from backend.models.dashboard_facade import DashboardFacade


class DashboardFacadeSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = DashboardFacade
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
