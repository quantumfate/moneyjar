# import Argon2
from app.helpers.database import UserAccountConnection
from app.models import DashboardFacade
from graphene import Field, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.dialects.postgresql import BYTEA, UUID


class UserAccount(SQLAlchemyObjectType):

    class Meta:
        model = UserAccountConnection
        interfaces = (ObjectType,)

    user_account_id = Field(UUID, required=True)
    dashboard_facade = Field(lambda: DashboardFacade)
    user_name = Field(String, required=True)
    forename = Field(String, required=True)
    surname = Field(String, required=True)
    email = Field(String, required=True)
    password_hash = Field(BYTEA, required=True)
    allocation_salt = Field(BYTEA, required=True)
