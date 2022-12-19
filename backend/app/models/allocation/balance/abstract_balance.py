import abc

from app.helpers.database import AbstractBalanceConnection, db
from graphene_sqlalchemy import SQLAlchemyObjectType


class AbstractBalance(SQLAlchemyObjectType):
    class Meta:
        abstract = True
        model = db.AbstractBalanceConnection
            
    __abstract__ = True
    def __init__(self):
        super().__init__()

    
    @abc.abstractmethod
    def my_abstract_method(self):
        pass
