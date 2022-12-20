from app.api.resolvers import _AbstractBaseResolver
from app.models import AllocationFacade


class _AllocationFacadeResolver(_AbstractBaseResolver):
    """
    This class will not be imported by other modules. _AllocationFacadeResolver defines resolve
    methods that will be combined with _AllocationFacadeQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    
    def resolve_type(self, instance):
        pass