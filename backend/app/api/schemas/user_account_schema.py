# Define the UserAccountType using the SQLAlchemyObjectType
from app.models import UserAccount
from graphene_sqlalchemy import SQLAlchemyObjectType


class UserAccountSchema(SQLAlchemyObjectType):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'email')
