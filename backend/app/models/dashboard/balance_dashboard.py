from app.helpers.database import BalanceDashboardConnection
from graphene import Field, ObjectType
from sqlalchemy.dialects.postgresql import UUID

from .abstract_dashboard import AbstractDashboard


class BalanceDashboard(AbstractDashboard):
    class Meta:
        model = BalanceDashboardConnection
        interfaces = (ObjectType,)
    
    balance_dahboard_id = Field(UUID, required=True)
    
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