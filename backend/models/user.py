from graphene import ObjectType, String, Int, Field
from graphene_sqlalchemy import SQLAlchemyObjectType
from app import db

class User(SQLAlchemyObjectType):
    class Meta:
        model = db.User
        interfaces = (ObjectType,)
    
    id = Int(required=True)
    name = String(required=True)
    email = String(required=True)