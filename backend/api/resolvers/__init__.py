# Import all the queries

from ._allocation_facade_resolver import _AllocationFacadeResolver
from ._dashboard_facade_resolver import _DashboardFacadeResolver
from ._user_account_resolver import _UserAccountResolver
from .allocation import *
from .dashboard import *

# Only Expose the QueryResolver classes to the outside
__all__ = [
    ''
]