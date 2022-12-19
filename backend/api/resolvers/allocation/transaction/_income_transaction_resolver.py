from backend.models.allocation.transaction import IncomeTransaction


class _IncomeTransactionResolver:
    """
    This class will not be imported by other modules. class _IncomeTransactionResolver defines resolve
    methods that will be combined with IncomeTransactionQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
