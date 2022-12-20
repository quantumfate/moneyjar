from app.models import BalanceDashboard

from ._abstract_dashboard_resolver import _AbstractDashboardResolver


class _BalanceDashboardResolver(_AbstractDashboardResolver):
    """
    This class will not be imported by other modules. _BalanceDashboardResolver defines resolve
    methods that will be combined with _BalanceDashboardQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass