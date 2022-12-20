import graphene
from app.api.interfaces import GlobalInterface
from app.api.queries import UserAccountQuery
from app.api.schemas.user_account_schema import UserAccountSchema
from graphene import List, ObjectType


class _UserAccountQuery(ObjectType):
    class Meta:
        interfaces = (GlobalInterface,)
   # Define a field for fetching a list of all user accounts
    all_user_accounts = List(lambda: UserAccountSchema)
    user_account = graphene.Field(UserAccountSchema, resolver=UserAccountQuery)
   