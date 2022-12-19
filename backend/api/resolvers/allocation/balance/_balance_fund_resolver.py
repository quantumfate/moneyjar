from backend.models.allocation.balance import BalanceFund


class _BalanceFundResolver:
    """
    This class will not be imported by other modules. class _BalanceFundResolver defines resolve
    methods that will be combined with BalanceFundQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
