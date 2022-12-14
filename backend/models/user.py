from app import db
from flask_bcrypt import generate_password_hash
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = db.User
        interfaces = (ObjectType,)
    
    id = Int(required=True)
    name = String(required=True)
    user_name = String(requird=True)
    email = String(required=True)
    password = String(required=True)

    def __init__(self, name, user_name, email, password):
        self.name = name
        self.user_name = user_name
        self.email  = email
        # Generate a hashed password
        self.password = generate_password_hash(password)


    def save(self):
        """
        This method is used to store the user in the database.
        """
        # Save the user to the database
        db.session.add(self)
        db.session.commit()
