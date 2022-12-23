from app.helpers.database import BalanceDashboardConnection
from app.models import (AllocationFacade, BalanceFund, BalanceJar,
                        ExpenseTransaction, IncomeTransaction, SavingStrategy,
                        TransactionSchedule)
from graphene import Field, List, ObjectType
from sqlalchemy.dialects.postgresql import UUID

from .abstract_dashboard import AbstractDashboard


class BalanceDashboard(AbstractDashboard):
    class Meta:
        model = BalanceDashboardConnection
        interfaces = (ObjectType,)
    
    balance_dahboard_id = Field(UUID, required=True)

    def get_allocation_facade(self) -> AllocationFacade:
        pass
    def get_income_transactions(self, time_window: callable=None) -> List(IncomeTransaction):
        pass
    
    def get_expense_transactions(self, time_window: callable=None) -> List(ExpenseTransaction):
        pass
    
    def get_balance_jars(self) -> List(BalanceJar):
        pass
    
    def get_balance_funds(self) -> List(BalanceFund):
        pass
    
    def get_transaction_schedules(self) -> List(TransactionSchedule):
        pass
    
    def get_saving_strategies(self) -> List(SavingStrategy):
        pass