# from sqlalchemy.orm import query
from app import db
from app.helpers import AbstractUtils
from app.helpers.database import BalanceFundConnection, database_log


class BalanceFundUtils(AbstractUtils):
    def filter_data(self, data: list, filter_func: callable) -> list:
        pass


    def sort_data(self, data: list, sort_func: callable) -> list:
        pass