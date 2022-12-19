import abc

from graphene_sqlalchemy import SQLAlchemyObjectType


class AbstractBalance(SQLAlchemyObjectType):
    class Meta:
        abstract = True
            
    __abstract__ = True
    def __init__(self):
        super().__init__()

    
    @abc.abstractmethod
    def my_abstract_method(self):
        pass
