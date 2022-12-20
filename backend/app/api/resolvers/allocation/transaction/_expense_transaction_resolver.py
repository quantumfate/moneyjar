from app.models import ExpenseTransaction

from ._abstract_transaction_resolver import _AbstractTransactionResolver


class _ExpenseTransactionResolver(_AbstractTransactionResolver):
    """
    This class will not be imported by other modules. class _ExpenseTransactionResolver defines resolve
    methods that will be combined with _ExpenseTransactionQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass