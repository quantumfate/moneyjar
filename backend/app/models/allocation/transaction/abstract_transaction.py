import abc

from app.helpers.database import AbstractTransactionConnection, db
from graphene_sqlalchemy import SQLAlchemyObjectType


class AbstractTransaction(SQLAlchemyObjectType):
    class Meta:
        abstract = True
        model = db.AbstractTransactionConnection
        
    __abstract__ = True
    def __init__(self):
        super().__init__()
  
    @abc.abstractmethod
    def my_abstract_method(self):
        pass
