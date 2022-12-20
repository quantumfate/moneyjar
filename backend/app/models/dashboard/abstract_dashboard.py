import abc

from app.helpers.database import AbstractDashboardConnection
from graphene_sqlalchemy import SQLAlchemyObjectType


class AbstractDahboard(SQLAlchemyObjectType):
    class Meta:
        abstract = True
        model = AbstractDashboardConnection
        
    __abstract__ = True
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def my_abstract_method(self):
        pass
