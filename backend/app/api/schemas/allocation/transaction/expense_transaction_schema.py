from graphene_sqlalchemy import SQLAlchemyObjectType

from backend.models.allocation.transaction.expense_transaction import \
    ExpenseTransaction


class ExpenseTransactionSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = ExpenseTransaction
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
