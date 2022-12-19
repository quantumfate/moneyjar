from app import db
from graphene import ObjectType

from .abstract_balance import AbstractBalance


class BalanceFund(AbstractBalance):
    class Meta:
        model = db.BalanceFund
        interfaces = (ObjectType,)

    def my_abstract_method(self):
        pass
