from app import db
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType


class UserAccount(SQLAlchemyObjectType):
    class Meta:
        model = db.User
        interfaces = (ObjectType,)
