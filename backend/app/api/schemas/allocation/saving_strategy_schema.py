from app.models import SavingStrategy
from graphene_sqlalchemy import SQLAlchemyObjectType


class SavingStrategySchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = SavingStrategy
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
