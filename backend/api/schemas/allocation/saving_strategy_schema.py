from graphene_sqlalchemy import SQLAlchemyObjectType

from backend.models.allocation.saving_strategy import SavingStrategy


class SavingStrategySchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = SavingStrategy
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
