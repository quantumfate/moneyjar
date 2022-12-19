from app.models import BalanceDashboard
from graphene_sqlalchemy import SQLAlchemyObjectType


class BalanceDashboardSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = BalanceDashboard
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
