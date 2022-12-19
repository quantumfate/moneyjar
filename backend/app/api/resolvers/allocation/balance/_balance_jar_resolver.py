from app.models import BalanceJar


class _BalanceJarResolver:
    """
    This class will not be imported by other modules. class _BalanceJarResolver defines resolve
    methods that will be combined with BalanceJarQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
