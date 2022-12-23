# from sqlalchemy.orm import query
from app import db
from app.helpers import AbstractUtils
from app.helpers.database import (AbstractDashboardUtils,
                                  BalanceDashboardConnection, database_log)


class BalanceDashboardUtils(AbstractDashboardUtils):
    
    def filter_data(self, data: list, filter_func: callable) -> list:
        pass


    def sort_data(self, data: list, sort_func: callable) -> list:
        pass