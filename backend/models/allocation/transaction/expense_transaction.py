from app import db
from .abstract_transaction import AbstractTransaction
from graphene import Field, Int, ObjectType, String


class ExpenseTransaction(AbstractTransaction):
    class Meta:
        model = db.ExpenseTransaction
        interfaces = (ObjectType,)
