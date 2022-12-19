from app.models import AnalyticsDashboard


class _AnalyticsDashboardResolver:
    """
    This class will not be imported by other modules. class _AnalyticsDashboardResolver defines resolve
    methods that will be combined with AnalyticsDashboardQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
