from app.helpers.database import AnalyticsDashboardConnection
from graphene import ObjectType

from .abstract_dashboard import AbstractDahboard


class AnalyticsDashboard(AbstractDahboard):
    class Meta:
        model = AnalyticsDashboardConnection
        interfaces = (ObjectType,)
        
    def my_abstract_method(self):
        pass