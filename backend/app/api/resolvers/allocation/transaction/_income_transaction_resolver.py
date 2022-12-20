from app.models import IncomeTransaction

from ._abstract_transaction_resolver import _AbstractTransactionResolver


class _IncomeTransactionResolver(_AbstractTransactionResolver):
    """
    This class will not be imported by other modules. class _IncomeTransactionResolver defines resolve
    methods that will be combined with _IncomeTransactionQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass