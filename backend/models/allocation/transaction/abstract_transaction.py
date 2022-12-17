import abc
from graphene_sqlalchemy import SQLAlchemyObjectType


class AbstractTransaction(SQLAlchemyObjectType, metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def my_abstract_method(self):
        pass
