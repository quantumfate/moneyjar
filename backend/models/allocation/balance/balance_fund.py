from app import db
from .abstract_balance import AbstractBalance
from graphene import Field, Int, ObjectType, String


class BalanceFund(AbstractBalance):
    class Meta:
        model = db.BalanceFund
        interfaces = (ObjectType,)
