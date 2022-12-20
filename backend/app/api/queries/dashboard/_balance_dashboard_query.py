
import graphene
from app.api.interfaces import DashboardInterface
from app.api.queries import BalanceJarQuery
from app.api.schemas import BalanceDashboardSchema
from graphene import ObjectType


class _BalanceDashboardQuery(ObjectType):
    class Meta:
        interfaces = (DashboardInterface,)
   # Define a field for fetching a list of all user accounts
    user_account = graphene.Field(BalanceDashboardSchema, resolver=BalanceJarQuery)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
