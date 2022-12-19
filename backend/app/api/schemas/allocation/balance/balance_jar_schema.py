from app.models import BalanceJar
from graphene_sqlalchemy import SQLAlchemyObjectType


class BalanceJarSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = BalanceJar
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
