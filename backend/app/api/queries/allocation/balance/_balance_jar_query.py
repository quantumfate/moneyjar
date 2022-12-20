import graphene
from app.api.interfaces import BalanceInterface
from app.api.queries import BalanceJarQuery
from app.api.schemas import BalanceJarSchema
from graphene import ObjectType


class _BalanceJarQuery(ObjectType):
   
    class Meta:
        interfaces = (BalanceInterface,)
    user_account = graphene.Field(BalanceJarSchema, resolver=BalanceJarQuery)
