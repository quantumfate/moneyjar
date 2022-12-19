from app.helpers.database import BalanceDashboardConnection, db
from graphene import ObjectType

from .abstract_dashboard import AbstractDahboard


class BalanceDashboard(AbstractDahboard):
    class Meta:
        model = db.BalanceDashboardConnection
        interfaces = (ObjectType,)
        
    def my_abstract_method(self):
        pass