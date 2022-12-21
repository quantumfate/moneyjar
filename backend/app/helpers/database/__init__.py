"""
Author: Leon Connor Holm leon-holm@outlook.de

This is the database module that exposes the Base object as a declarative base.
If you make a class in this moduel extend
"""
from .config import Config
from .connections import *
from .database import Base, database_log, db, session
from .utils import *

__all__ = [
    'AbstractBalanceConnection',
    'AbstractTransactionConnection',
    'BalanceFundConnection',
    'BalanceJarConnection',
    'ExpenseTransactionConnection',
    'IncomeTransactionConnection',
    'SavingStrategyConnection',
    'TransactionScheduleConnection',
    'AbstractDashboardConnection',
    'AllocationFacadeConnection',
    'AnalyticsDashboardConnection',
    'BalanceDashboardConnection',
    'DashboardFacadeConnection',
    'UserAccountConnection',
    'database_log',
    'AbstractUtils',
    'BalanceFundUtils',
    'BalanceJarUtils',
    'ExpenseTransactionUtils',
    'IncomeTransactionUtils',
    'SavingStrategyUtils',
    'TransactionScheduleUtils',
    'AllocationFacadeUtils',
    'AnalyticsDashboardUtils',
    'BalanceDashboardUtils',
    'DashboardFacadeUtils',
    'UserAccountUtils',
    'db',
    'session'
]

from app.helpers import ClassImporter

importer = ClassImporter(__import__('app.helpers.database'))
connection_classes = importer[[
    'AbstractBalanceConnection',
    'AbstractTransactionConnection',
    'BalanceFundConnection',
    'BalanceJarConnection',
    'ExpenseTransactionConnection',
    'IncomeTransactionConnection',
    'SavingStrategyConnection',
    'TransactionScheduleConnection',
    'AbstractDashboardConnection',
    'AllocationFacadeConnection',
    'AnalyticsDashboardConnection',
    'BalanceDashboardConnection',
    'DashboardFacadeConnection',
    'UserAccountConnection'
    ]]

util_classes = importer[[
    'AbstractUtils',
    'BalanceFundUtils',
    'BalanceJarUtils',
    'ExpenseTransactionUtils',
    'IncomeTransactionUtils',
    'SavingStrategyUtils',
    'TransactionScheduleUtils',
    'AllocationFacadeUtils',
    'AnalyticsDashboardUtils',
    'BalanceDashboardUtils',
    'DashboardFacadeUtils',
    'UserAccountUtils'
    ]]