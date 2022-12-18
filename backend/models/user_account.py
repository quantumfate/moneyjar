import Argon2
from app import db
from graphene import Field, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from helpers.database.connections.user_account_connection import \
    UserAccountConnection
from sqlalchemy.dialects.postgresql import UUID

from .dashboard_facade import DashboardFacade


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
