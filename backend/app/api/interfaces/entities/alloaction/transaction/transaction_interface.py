import graphene
from app.api.interfaces import GlobalInterface


class TransactionInterface(GlobalInterface):
    """Interface for objects related to transactions.

    This interface extends the `GlobalInterface` interface and includes all of its fields
    and resolvers. It can be implemented by GraphQL types that represent the
    abstract implementation of ExpenseTransaction and IncomeTransaction in 
    the GraphQL Query Language.
    """
