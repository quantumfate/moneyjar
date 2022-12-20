import abc

import graphene
from app.models import AbstractBalance


class _AbstractBaseResolver(graphene.ObjectType, metaclass=abc.ABCMeta):
    class Meta:
        abstract = True

    @abc.abstractmethod
    def resolve_type(self, instance):
        pass