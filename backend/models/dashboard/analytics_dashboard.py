from app import db
from .abstract_dashboard import AbstractDahboard
from graphene import Field, Int, ObjectType, String


class AnalyticsDashboard(AbstractDahboard):
    class Meta:
        model = db.AnalyticsDashboard
        interfaces = (ObjectType,)
