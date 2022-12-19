
import graphene
from app.api.queries import BalanceJarQueryResolver
from app.api.schemas import BalanceJarSchema
from graphene import ObjectType


class BalanceJarQuery(ObjectType):
   # Define a field for fetching a list of all user accounts
    user_account = graphene.Field(BalanceJarSchema, resolver=BalanceJarQueryResolver)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
