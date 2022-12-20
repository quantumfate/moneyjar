
import graphene
from app.api.interfaces import DashboardInterface
from app.api.queries import AllocationFacadeQuery
from app.api.schemas import AnalyticsDashboardSchema
from graphene import ObjectType


class _AnalyticsDashboardQuery(ObjectType):
    class Meta:
        interfaces = (DashboardInterface,)
   # Define a field for fetching a list of all user accounts
    user_account = graphene.Field(AnalyticsDashboardSchema, resolver=AllocationFacadeQuery)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
