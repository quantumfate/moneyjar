from app import db
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType


class TransactionSchedule(SQLAlchemyObjectType):
    class Meta:
        model = db.TransactionSchedule
        interfaces = (ObjectType,)
