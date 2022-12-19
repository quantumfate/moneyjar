from app import db
from graphene import ObjectType

from .abstract_transaction import AbstractTransaction


class IncomeTransaction(AbstractTransaction):
    class Meta:
        model = db.IncomeTransaction
        interfaces = (ObjectType,)

        
    def my_abstract_method(self):
        pass