from app import db
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType


class SavingStrategy(SQLAlchemyObjectType):
    class Meta:
        model = db.SavingStrategy
        interfaces = (ObjectType,)
