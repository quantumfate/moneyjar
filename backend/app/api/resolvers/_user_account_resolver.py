from app.api.resolvers import _AbstractBaseResolver
from app.models import UserAccount


class _UserAccountResolver(_AbstractBaseResolver):
    """
    This class will not be imported by other modules. _UserAccountResolver defines resolve
    methods that will be combined with _UserAccountQuery.
    """
    def resolve_all_user_accounts(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass