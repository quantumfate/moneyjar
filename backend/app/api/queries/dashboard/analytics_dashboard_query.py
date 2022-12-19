
import graphene
from app.api.queries import AllocationFacadeQueryResolver
from app.api.schemas import AnalyticsDashboardSchema
from graphene import ObjectType


class AnalyticsDashboardQuery(ObjectType):
   # Define a field for fetching a list of all user accounts
    user_account = graphene.Field(AnalyticsDashboardSchema, resolver=AllocationFacadeQueryResolver)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
