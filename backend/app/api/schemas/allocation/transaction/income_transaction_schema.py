from graphene_sqlalchemy import SQLAlchemyObjectType

from backend.models.allocation.transaction.income_transaction import \
    IncomeTransaction


class IncomeTransactionSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = IncomeTransaction
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
