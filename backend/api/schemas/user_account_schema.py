# Define the UserAccountType using the SQLAlchemyObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType

from backend.models.user_account import UserAccount


class UserAccountSchema(SQLAlchemyObjectType):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'email')
