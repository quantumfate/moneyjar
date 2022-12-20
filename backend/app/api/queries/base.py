import graphene
from app.api.queries import (AllocationFacadeQuery, AnalyticsDashboardQuery,
                             BalanceDashboardQuery, BalanceFundQuery,
                             BalanceJarQuery, DashboardFacadeQuery,
                             ExpenseTransactionQuery, IncomeTransactionQuery,
                             SavingStrategyQuery, TransactionScheduleQuery,
                             UserAccountQuery)


class Query(graphene.ObjectType):
    """
    This class defines the root Query object for the GraphQL API. 
    It combines all the Query and Resolver objects for each entity into a single root object. 
    When a GraphQL query is made, it is specified which field of the 
    Query object is being queried, and the corresponding QueryResolver will 
    be responsible for handling the request and returning the requested data.
    """
    balance_fund = graphene.Field(BalanceFundQuery)
    balance_jar = graphene.Field(BalanceJarQuery)
    income_transaction = graphene.Field(IncomeTransactionQuery)
    expense_transaction = graphene.Field(ExpenseTransactionQuery)
    saving_strategy = graphene.Field(SavingStrategyQuery)
    transaction_schedule = graphene.Field(TransactionScheduleQuery)
    allocation_facade = graphene.Field(AllocationFacadeQuery)
    analytics_dashboard = graphene.Field(AnalyticsDashboardQuery)
    balance_dashboard = graphene.Field(BalanceDashboardQuery)
    dashboard_facade = graphene.Field(DashboardFacadeQuery)
    user_account = graphene.Field(UserAccountQuery)
