
import graphene
from graphene import ObjectType

from backend.api.queries import TransactionScheduleQueryResolver
from backend.api.schemas import TransactionScheduleSchema


class TransactionScheduleQuery(ObjectType):
   # Define a field for fetching a list of all user accounts
    user_account = graphene.Field(TransactionScheduleSchema, resolver=TransactionScheduleQueryResolver)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
