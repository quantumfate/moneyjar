from app.helpers.database import AllocationFacadeConnection, db
from graphene import Field, Int, ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType


class AllocationFacade(SQLAlchemyObjectType):
    class Meta:
        model = db.AllocationFacadeConnection
        interfaces = (ObjectType,)
