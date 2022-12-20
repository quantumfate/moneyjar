from app.helpers.database import BalanceDashboardConnection
from graphene import ObjectType

from .abstract_dashboard import AbstractDahboard


class BalanceDashboard(AbstractDahboard):
    class Meta:
        model = BalanceDashboardConnection
        interfaces = (ObjectType,)
        
    def my_abstract_method(self):
        pass