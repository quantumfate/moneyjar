from app.models import BalanceFund

from ._abstract_balance_resolver import _AbstractBalanceResolver


class _BalanceFundResolver(_AbstractBalanceResolver):
    """
    This class will not be imported by other modules. class _BalanceFundResolver defines resolve
    methods that will be combined with _BalanceFundQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass