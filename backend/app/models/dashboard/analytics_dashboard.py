from app import db
from graphene import ObjectType

from .abstract_dashboard import AbstractDahboard


class AnalyticsDashboard(AbstractDahboard):
    class Meta:
        model = db.AnalyticsDashboard
        interfaces = (ObjectType,)
        
    def my_abstract_method(self):
        pass