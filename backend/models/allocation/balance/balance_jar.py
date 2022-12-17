from app import db
from .abstract_balance import AbstractBalance
from graphene import Field, Int, ObjectType, String


class BalanceJar(AbstractBalance):
    class Meta:
        model = db.BalanceJar
        interfaces = (ObjectType,)
