import graphene
from app.api.interfaces import GlobalInterface
from app.api.queries import AllocationFacadeQuery
from app.api.schemas import AllocationFacadeSchema
from graphene import List, ObjectType


class _AllocationFacadeQuery(ObjectType):
    class Meta:
        interfaces = (GlobalInterface,)
   # Define a field for fetching a list of all user accounts
    all_user_accounts = List(lambda: AllocationFacadeSchema)
    user_account = graphene.Field(AllocationFacadeSchema, resolver=AllocationFacadeQuery)
    # # Define a resolver function for the all_user_accounts field
    # def resolve_all_user_accounts(self, info):
    #     # Use the query attribute of the SQLAlchemy session to fetch all user accounts from the database
    #     return UserAccount.query.all()
