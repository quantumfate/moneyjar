import abc

from app.helpers.database import AbstractDashboardConnection
from app.models import (BalanceFund, BalanceJar, ExpenseTransaction,
                        IncomeTransaction, SavingStrategy, TransactionSchedule)
from graphene import List
from graphene_sqlalchemy import SQLAlchemyObjectType


class AbstractDashboard(SQLAlchemyObjectType):
    class Meta:
        abstract = True
        model = AbstractDashboardConnection
    
    income_transactions = List(lambda: IncomeTransaction)
    expense_transactions = List(lambda: ExpenseTransaction)
    balance_jars = List(lambda: BalanceJar)
    balance_funds = List(lambda: BalanceFund)
    transaction_schedules = List(lambda: TransactionSchedule)
    saving_strategies = List(lambda: SavingStrategy)

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def get_income_transactions(self):
        pass
    
    @abc.abstractmethod
    def get_expense_transactions(self):
        pass
    
    @abc.abstractmethod
    def get_balance_jars(self):
        pass
    
    @abc.abstractmethod
    def get_balance_funds(self):
        pass
    
    @abc.abstractmethod
    def get_transaction_schedules(self):
        pass
    
    @abc.abstractmethod
    def get_saving_strategies(self):
        pass