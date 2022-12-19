from backend.models.allocation import TransactionSchedule


class _TransactionScheduleResolver:
    """
    This class will not be imported by other modules. class TransactionScheduleResolver defines resolve
    methods that will be combined with TransactionScheduleQuery.
    """
    def resolve_dashboard_facade(self, info):
        # Here, you can retrieve all user accounts from your database and return them
        # return UserAccount.query.all()
        pass
