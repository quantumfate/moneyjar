import abc

from app.api.resolvers import _AbstractBaseResolver


class _AbstractBalanceResolver(_AbstractBaseResolver, metaclass=abc.ABCMeta):
    class Meta:
        abstract = True

