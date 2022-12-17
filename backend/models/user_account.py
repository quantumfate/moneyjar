from app import db
from graphene import Field, UUID, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType
from .dashboard_facade import DashboardFacade
from helpers.database.connections.user_account_connection import UserAccountConnection


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
    password = Field(String, required=True)

    