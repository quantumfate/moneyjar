from app.api.resolvers import _AbstractBaseResolver
from app.models import TransactionSchedule


class _TransactionScheduleResolver(_AbstractBaseResolver):
    """
    This class will not be imported by other modules. class TransactionScheduleResolver defines resolve
    methods that will be combined with _TransactionScheduleQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
    def resolve_type(self, instance):
        pass