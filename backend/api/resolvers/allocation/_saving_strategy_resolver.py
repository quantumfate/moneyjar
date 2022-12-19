from backend.models.allocation import SavingStrategy


class _SavingStrategyResolver:
    """
    This class will not be imported by other modules. class _SavingStrategyResolver defines resolve
    methods that will be combined with SavingStrategyQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
