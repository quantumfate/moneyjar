
import graphene
from graphene import ObjectType

from backend.api.queries import IncomeTransactionQueryResolver
from backend.api.schemas import IncomeTransactionSchema


class IncomeTransactionQuery(ObjectType):
   # Define a field for fetching a list of all user accounts
    user_account = graphene.Field(IncomeTransactionSchema, resolver=IncomeTransactionQueryResolver)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
