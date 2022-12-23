from datetime import datetime
from typing import Dict, Optional

from app.helpers.database import AnalyticsDashboardConnection
from app.models import (AbstractTransaction, AllocationFacade, BalanceFund,
                        BalanceJar, ExpenseTransaction, IncomeTransaction,
                        SavingStrategy, TransactionSchedule)
from graphene import Decimal, Field, Int, List, ObjectType, Scalar
from graphql.language import ast
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DateTime, TypeDecorator

from .abstract_dashboard import AbstractDashboard


class AnalyticsDashboard(AbstractDashboard):
    class Meta:
        model = AnalyticsDashboardConnection
        interfaces = (ObjectType,)
    
    class AnalyticsMap(Scalar):
        """
        A custom scalar type for storing a map of dates to expenses in GraphQL and SQLAlchemy.
    
        Attributes:
        serialize (callable): A method to serialize the map of dates to expenses.
        parse_literal (callable): A method to parse a literal value from the GraphQL AST.
        parse_value (callable): A method to parse a value from the GraphQL quer
        """
        @staticmethod
        def serialize(dt: datetime):
            return dt.isoformat()
        
        @staticmethod
        def parse_literal(node: ast.Node) -> Optional[datetime]:
            if isinstance(node, ast.StringValue):
                return datetime.fromisoformat(node.value)
        
        @staticmethod
        def parse_value(value: str) -> Optional[datetime]:
            return datetime.fromisoformat(value)
        
    balance_dahboard_id = Field(UUID, required=True)
    analytics_dashboard_id = Field(UUID, required=True)    
    analytics_map: Dict[datetime, List(AbstractTransaction)] = {}
    
    total_transactions = Field(Int)
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