from app import db
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType


class DashboardFacade(SQLAlchemyObjectType):
    class Meta:
        model = db.DashboardFacade
        interfaces = (ObjectType,)
