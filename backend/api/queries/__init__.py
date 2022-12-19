import graphene
from graphene import ObjectType

from backend.api.resolvers._allocation_facade_resolver import \
    _AllocationFacadeResolver
from backend.api.resolvers._dashboard_facade_resolver import \
    _DashboardFacadeResolver
from backend.api.resolvers._user_account_resolver import _UserAccountResolver
from backend.api.resolvers.allocation import (_BalanceFundResolver,
                                              _BalanceJarResolver,
                                              _ExpenseTransactionResolver,
                                              _IncomeTransactionResolver,
                                              _SavingStrategyResolver,
                                              _TransactionScheduleResolver)
from backend.api.resolvers.dashboard import (_AnalyticsDashboardResolver,
                                             _BalanceDashboardResolver)

from .allocation import *
from .allocation_facade_query import AllocationFacadeQuery
from .dashboard import *
from .dashboard_facade_query import DashboardFacadeQuery
from .user_account_query import UserAccountQuery


# Connect all queries with their respective resolver from this package
class BalanceFundQueryResolver(BalanceFundQuery, _BalanceFundResolver):
    """
    Combines BalanceFundQuery with its resolver methods BalanceFundResolver
    """
class BalanceJarQueryResolver(BalanceJarQuery, _BalanceJarResolver):
    """
    Combines BalanceJarQuery with its resolver methods BalanceJarResolver
    """
class IncomeTransactionQueryResolver(IncomeTransactionQuery, _IncomeTransactionResolver):
    """
    Combines IncomeTransactionQuery with its resolver methods IncomeTransactionResolver
    """
class ExpenseTransactionQueryResolver(ExpenseTransactionQuery, _ExpenseTransactionResolver):
    """
    Combines ExpenseTransactionQuery with its resolver methods ExpenseTransactionResolver
    """
class SavingStrategyQueryResolver(SavingStrategyQuery, _SavingStrategyResolver):
    """
    Combines SavingStrategyQuery with its resolver methods SavingStrategyResolver
    """
class TransactionScheduleQueryResolver(TransactionScheduleQuery, _TransactionScheduleResolver):
    """
    Combines TransactionScheduleQuery with its resolver methods TransactionScheduleResolver
    """
class AllocationFacadeQueryResolver(AllocationFacadeQuery, _AllocationFacadeResolver):
    """
    Combines AllocationFacadeQuery with its resolver methods AllocationFacadeResolver
    """
class AnalyticsDashboardQueryResolver(AnalyticsDashboardQuery, _AnalyticsDashboardResolver):
    """
    Combines AnalyticsDashboardQuery with its resolver methods AnalyticsDashboardResolver
    """
class BalanceDashboardQueryResolver(BalanceDashboardQuery, _BalanceDashboardResolver):
    """
    Combines BalanceDashboardQuery with its resolver methods BalanceDashboardQuery
    """
class DashboardFacadeQueryResolver(DashboardFacadeQuery, _DashboardFacadeResolver):
    """
    Combines DashboardFacadeQuery with its resolver methods DashboardFacadeResolver
    """
class UserAccountQueryResolver(UserAccountQuery, _UserAccountResolver):
    """
    Combines UserAccountQuery with its resolver methods UserAccountResolver
    """

__all__ = [
    'BalanceFundQueryResolver',
    'BalanceJarQueryResolver',
    'IncomeTransactionQueryResolver',
    'ExpenseTransactionQueryResolver',
    'SavingStrategyQueryResolver',
    'TransactionScheduleQueryResolver',
    'AllocationFacadeQueryResolver',
    'AnalyticsDashboardQueryResolver',
    'BalanceDashboardQueryResolver',
    'DashboardFacadeQueryResolver',
    'UserAccountQueryResolver'
]