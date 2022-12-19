from app import db
from graphene import Field, Int, ObjectType, String

from .abstract_balance import AbstractBalance


class BalanceJar(AbstractBalance):
    class Meta:
        model = db.BalanceJar
        interfaces = (ObjectType,)

    def my_abstract_method(self):
        pass
