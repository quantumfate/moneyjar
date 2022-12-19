from app.models import BalanceFund
from graphene_sqlalchemy import SQLAlchemyObjectType


class BalanceFundSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = BalanceFund
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
