from app import db
from .abstract_transaction import AbstractTransaction
from graphene import Field, Int, ObjectType, String


class IncomeTransaction(AbstractTransaction):
    class Meta:
        model = db.IncomeTransaction
        interfaces = (ObjectType,)
