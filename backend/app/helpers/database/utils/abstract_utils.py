import abc


class AbstractUtils(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def filter_data(self, data: list, filter_func: callable) -> list:
        pass

    @abc.abstractmethod
    def sort_data(self, data: list, sort_func: callable) -> list:
        pass