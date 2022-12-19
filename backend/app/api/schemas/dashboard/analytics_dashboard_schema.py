from app.models import AnalyticsDashboard
from graphene_sqlalchemy import SQLAlchemyObjectType


class AnalyticsDashboardSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = AnalyticsDashboard
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
