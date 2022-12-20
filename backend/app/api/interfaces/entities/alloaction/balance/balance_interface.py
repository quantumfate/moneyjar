import graphene
from app.api.interfaces import GlobalInterface


class BalanceInterface(GlobalInterface):
    """Interface for objects related to balances.

    This interface extends the `GlobalInterface` interface and includes all of its fields
    and resolvers. It can be implemented by GraphQL types that represent the
    abstract implementation of BalanceFund and BalanceJar in 
    the GraphQL Query Language.
    """

