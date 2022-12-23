import abc
from dataclasses import Field

from app.helpers.database import AbstractDashboardConnection
from app.models import (AllocationFacade, BalanceFund, BalanceJar,
                        ExpenseTransaction, IncomeTransaction, SavingStrategy,
                        TransactionSchedule)
from graphene import Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy.dialects.postgresql import UUID


class AbstractDashboard(SQLAlchemyObjectType):
    class Meta:
        abstract = True
        model = AbstractDashboardConnection
    
    allocation_facade_id = Field(UUID, required=True)
    allocation_facade = Field(lambda: AllocationFacade)
    income_transactions = List(lambda: IncomeTransaction)
    expense_transactions = List(lambda: ExpenseTransaction)
    balance_jars = List(lambda: BalanceJar)
    balance_funds = List(lambda: BalanceFund)
    transaction_schedules = List(lambda: TransactionSchedule)
    saving_strategies = List(lambda: SavingStrategy)

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def get_allocation_facade(self) -> AllocationFacade:
        """
        Get the allocation facade for the dashboard.
        
        Returns:
            AllocationFacade
        """
    
    @abc.abstractmethod
    def get_income_transactions(self, time_window: callable=None) -> List(IncomeTransaction):
        """
        Get the income transactions for the dashboard.
        
        Args:
            time_window (callable, optional): A callable that filters the transactions by a specific time range.
                The callable should accept a single argument of type `datetime` and return a boolean indicating
                whether the transaction should be included in the results.
        
        Returns:
            List[IncomeTransaction]: The list of income transactions for the dashboard.
        """
    
    @abc.abstractmethod
    def get_expense_transactions(self, time_window: callable=None) -> List(ExpenseTransaction):
        """
        Get the expense transactions for the dashboard.
        
        Args:
            time_window (callable, optional): A callable that filters the transactions by a specific time range.
                The callable should accept a single argument of type `datetime` and return a boolean indicating
                whether the transaction should be included in the results.
        
        Returns:
            List[ExpenseTransaction]: The list of expense transactions for the dashboard.
        """
    
    @abc.abstractmethod
    def get_balance_jars(self) -> List(BalanceJar):
        """
        Get the balance jars for the dashboard.
        
        Returns:
            List[BalanceJar]: The list of balance jars for the dashboard.
        """
    
    @abc.abstractmethod
    def get_balance_funds(self) -> List(BalanceFund):
        """
        Get a list of `BalanceFund` objects belonging to the dashboard.

        Returns:
            List[BalanceFund]: A list of `BalanceFund` objects.
        """
    
    @abc.abstractmethod
    def get_transaction_schedules(self) -> List(TransactionSchedule):
        """
        Get a list of `TransactionSchedule` objects belonging to the dashboard.

        Returns:
            List[TransactionSchedule]: A list of `TransactionSchedule` objects.
        """
    
    @abc.abstractmethod
    def get_saving_strategies(self) -> List(SavingStrategy):
        """
        Get a list of `SavingStrategy` objects belonging to the dashboard.

        Returns:
            List[SavingStrategy]: A list of `SavingStrategy` objects.
        """