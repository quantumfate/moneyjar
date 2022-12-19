import graphene
from app.api.queries import DashboardFacadeQueryResolver
from app.api.schemas import DashboardFacadeSchema
from graphene import List, ObjectType


class DashboardFacadeQuery(ObjectType):
   # Define a field for fetching a list of all user accounts
    all_user_accounts = List(lambda: DashboardFacadeSchema)
    user_account = graphene.Field(DashboardFacadeSchema, resolver=DashboardFacadeQueryResolver)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
