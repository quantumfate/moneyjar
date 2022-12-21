from app.helpers.database import AnalyticsDashboardConnection
from graphene import ObjectType

from .abstract_dashboard import AbstractDashboard


class AnalyticsDashboard(AbstractDashboard):
    class Meta:
        model = AnalyticsDashboardConnection
        interfaces = (ObjectType,)
        
    
    def get_income_transactions(self):
        pass
    
    def get_expense_transactions(self):
        pass
    
    def get_balance_jars(self):
        pass
    
    def get_balance_funds(self):
        pass
    
    def get_transaction_schedules(self):
        pass
    
    def get_saving_strategies(self):
        pass