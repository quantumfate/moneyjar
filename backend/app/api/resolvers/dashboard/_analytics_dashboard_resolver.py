from app.models import AnalyticsDashboard

from ._abstract_dashboard_resolver import _AbstractDashboardResolver


class _AnalyticsDashboardResolver(_AbstractDashboardResolver):
    """
    This class will not be imported by other modules. class _AnalyticsDashboardResolver defines resolve
    methods that will be combined with _AnalyticsDashboardQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass