from graphene import ObjectType, String, Int, Field
from graphene_sqlalchemy import SQLAlchemyObjectType
from app import db
from flask_bcrypt import generate_password_hash

class MoneyJar(SQLAlchemyObjectType):
    class Meta:
        model = db.User
        interfaces = (ObjectType,)
    
    id = Int(required=True)
    name = String(required=True)
    email = String(required=True)
    password = String(required=True)

    def save(self):
        # Generate a hashed password
        self.password = generate_password_hash(self.password)
        # Save the user to the database
        db.session.add(self)
        db.session.commit()