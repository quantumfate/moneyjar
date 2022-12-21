from app.api.resolvers._allocation_facade_resolver import \
    _AllocationFacadeResolver
from app.api.resolvers._dashboard_facade_resolver import \
    _DashboardFacadeResolver
from app.api.resolvers._user_account_resolver import _UserAccountResolver
from app.api.resolvers.allocation import (_BalanceFundResolver,
                                          _BalanceJarResolver,
                                          _ExpenseTransactionResolver,
                                          _IncomeTransactionResolver,
                                          _SavingStrategyResolver,
                                          _TransactionScheduleResolver)
from app.api.resolvers.dashboard import (_AnalyticsDashboardResolver,
                                         _BalanceDashboardResolver)

from ._allocation_facade_query import _AllocationFacadeQuery
from ._dashboard_facade_query import _DashboardFacadeQuery
from ._user_account_query import _UserAccountQuery
from .allocation import (_BalanceFundQuery, _BalanceJarQuery,
                         _ExpenseTransactionQuery, _IncomeTransactionQuery,
                         _SavingStrategyQuery, _TransactionScheduleQuery)
from .dashboard import _AnalyticsDashboardQuery, _BalanceDashboardQuery


# Connect all queries with their respective resolver
class BalanceFundQuery(_BalanceFundQuery, _BalanceFundResolver):
    """
    Combines _BalanceFundQuery with its resolver methods _BalanceFundResolver
    """
class BalanceJarQuery(_BalanceJarQuery, _BalanceJarResolver):
    """
    Combines _BalanceJarQuery with its resolver methods _BalanceJarResolver
    """
class IncomeTransactionQuery(_IncomeTransactionQuery, _IncomeTransactionResolver):
    """
    Combines _IncomeTransactionQuery with its resolver methods _IncomeTransactionResolver
    """
class ExpenseTransactionQuery(_ExpenseTransactionQuery, _ExpenseTransactionResolver):
    """
    Combines _ExpenseTransactionQuery with its resolver methods _ExpenseTransactionResolver
    """
class SavingStrategyQuery(_SavingStrategyQuery, _SavingStrategyResolver):
    """
    Combines _SavingStrategyQuery with its resolver methods _SavingStrategyResolver
    """
class TransactionScheduleQuery(_TransactionScheduleQuery, _TransactionScheduleResolver):
    """
    Combines _TransactionScheduleQuery with its resolver methods _TransactionScheduleResolver
    """
class AllocationFacadeQuery(_AllocationFacadeQuery, _AllocationFacadeResolver):
    """
    Combines _AllocationFacadeQuery with its resolver methods _AllocationFacadeResolver
    """
class AnalyticsDashboardQuery(_AnalyticsDashboardQuery, _AnalyticsDashboardResolver):
    """
    Combines _AnalyticsDashboardQuery with its resolver methods _AnalyticsDashboardResolver
    """
class BalanceDashboardQuery(_BalanceDashboardQuery, _BalanceDashboardResolver):
    """
    Combines _BalanceDashboardQuery with its resolver methods _BalanceDashboardQuery
    """
class DashboardFacadeQuery(_DashboardFacadeQuery, _DashboardFacadeResolver):
    """
    Combines _DashboardFacadeQuery with its resolver methods _DashboardFacadeResolver
    """
class UserAccountQuery(_UserAccountQuery, _UserAccountResolver):
    """
    Combines _UserAccountQuery with its resolver methods _UserAccountResolver
    """
    
from .base import Query

__all__ = [
    'BalanceFundQuery',
    'BalanceJarQuery',
    'IncomeTransactionQuery',
    'ExpenseTransactionQuery',
    'SavingStrategyQuery',
    'TransactionScheduleQuery',
    'AllocationFacadeQuery',
    'AnalyticsDashboardQuery',
    'BalanceDashboardQuery',
    'DashboardFacadeQuery',
    'UserAccountQuery',
    'Query'
]