from graphene_sqlalchemy import SQLAlchemyObjectType

from backend.models.allocation.transaction_schedule import TransactionSchedule


class TransactionScheduleSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = TransactionSchedule
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
