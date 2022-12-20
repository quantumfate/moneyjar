from app.models import BalanceJar

from ._abstract_balance_resolver import _AbstractBalanceResolver


class _BalanceJarResolver(_AbstractBalanceResolver):
    """
    This class will not be imported by other modules. class _BalanceJarResolver defines resolve
    methods that will be combined with _BalanceJarQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass