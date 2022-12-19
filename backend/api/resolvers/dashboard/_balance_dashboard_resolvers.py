from backend.models.dashboard import BalanceDashboard


class _BalanceDashboardResolver:
    """
    This class will not be imported by other modules. _BalanceDashboardResolver defines resolve
    methods that will be combined with BalanceDashboardQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
