import abc

from app.api.resolvers import _AbstractBaseResolver


class _AbstractTransactionResolver(_AbstractBaseResolver, metaclass=abc.ABCMeta):
    class Meta:
        abstract = True

