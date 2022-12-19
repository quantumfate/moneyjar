from backend.models.allocation.transaction import ExpenseTransaction


class _ExpenseTransactionResolver:
    """
    This class will not be imported by other modules. class _ExpenseTransactionResolver defines resolve
    methods that will be combined with ExpenseTransactionQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
