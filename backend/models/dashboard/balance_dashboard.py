from app import db
from .abstract_dashboard import AbstractDahboard
from graphene import Field, Int, ObjectType, String


class BalanceDashboard(AbstractDahboard):
    class Meta:
        model = db.BalanceDashboard
        interfaces = (ObjectType,)
