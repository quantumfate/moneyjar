from app import db
from graphene import ObjectType

from .abstract_transaction import AbstractTransaction


class ExpenseTransaction(AbstractTransaction):
    class Meta:
        model = db.ExpenseTransaction
        interfaces = (ObjectType,)

        
    def my_abstract_method(self):
        pass