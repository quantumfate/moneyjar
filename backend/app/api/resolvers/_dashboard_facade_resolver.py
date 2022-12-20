from app.api.resolvers import _AbstractBaseResolver
from app.models import DashboardFacade


class _DashboardFacadeResolver(_AbstractBaseResolver):
    """
    This class will not be imported by other modules. _DashboardFacadeResolver defines resolve
    methods that will be combined with _DashboardFacadeQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass