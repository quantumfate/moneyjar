
import graphene
from app.api.interfaces import GlobalInterface
from app.api.queries import TransactionScheduleQuery
from app.api.schemas import TransactionScheduleSchema
from graphene import ObjectType


class _TransactionScheduleQuery(ObjectType):
    class Meta:
        interfaces = (GlobalInterface,)
   # Define a field for fetching a list of all user accounts
    user_account = graphene.Field(TransactionScheduleSchema, resolver=TransactionScheduleQuery)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
