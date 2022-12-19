from app import db
from graphene import ObjectType

from .abstract_dashboard import AbstractDahboard


class BalanceDashboard(AbstractDahboard):
    class Meta:
        model = db.BalanceDashboard
        interfaces = (ObjectType,)
        
    def my_abstract_method(self):
        pass