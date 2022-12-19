from app import db
from graphene import ObjectType

from .abstract_balance import AbstractBalance


class BalanceJar(AbstractBalance):
    class Meta:
        model = db.BalanceJar
        interfaces = (ObjectType,)

    def my_abstract_method(self):
        pass
