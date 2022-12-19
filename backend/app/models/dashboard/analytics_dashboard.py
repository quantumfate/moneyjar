from app.helpers.database import AnalyticsDashboardConnection, db
from graphene import ObjectType

from .abstract_dashboard import AbstractDahboard


class AnalyticsDashboard(AbstractDahboard):
    class Meta:
        model = db.AnalyticsDashboardConnection
        interfaces = (ObjectType,)
        
    def my_abstract_method(self):
        pass