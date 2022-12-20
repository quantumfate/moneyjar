
import graphene
from app.api.interfaces import BalanceInterface
from app.api.queries import BalanceDashboardQuery
from app.api.schemas import BalanceFundSchema
from graphene import ObjectType


class _BalanceFundQuery(ObjectType):

    class Meta:
        interfaces = (BalanceInterface,)

    user_account = graphene.Field(BalanceFundSchema, resolver=BalanceDashboardQuery)
