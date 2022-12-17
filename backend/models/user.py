from app import db
from flask_bcrypt import generate_password_hash
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType

class User(SQLAlchemyObjectType):
    class Meta:
        model = db.User
        interfaces = (ObjectType,)