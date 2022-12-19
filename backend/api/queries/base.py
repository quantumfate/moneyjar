import graphene

from backend.api.queries import (AllocationFacadeQueryResolver,
                                 AnalyticsDashboardQueryResolver,
                                 BalanceDashboardQueryResolver,
                                 BalanceFundQueryResolver,
                                 BalanceJarQueryResolver,
                                 DashboardFacadeQueryResolver,
                                 ExpenseTransactionQueryResolver,
                                 IncomeTransactionQueryResolver,
                                 SavingStrategyQueryResolver,
                                 TransactionScheduleQueryResolver,
                                 UserAccountQueryResolver)


class Query(graphene.ObjectType):
    """
    This class defines the root Query object for the GraphQL API. 
    It combines all the QueryResolver objects for each entity into a single root object. 
    When a GraphQL query is made, it is specified which field of the 
    Query object is being queried, and the corresponding QueryResolver will 
    be responsible for handling the request and returning the requested data.
    """
    balance_fund = graphene.Field(BalanceFundQueryResolver)
    balance_jar = graphene.Field(BalanceJarQueryResolver)
    income_transaction = graphene.Field(IncomeTransactionQueryResolver)
    expense_transaction = graphene.Field(ExpenseTransactionQueryResolver)
    saving_strategy = graphene.Field(SavingStrategyQueryResolver)
    transaction_schedule = graphene.Field(TransactionScheduleQueryResolver)
    allocation_facade = graphene.Field(AllocationFacadeQueryResolver)
    analytics_dashboard = graphene.Field(AnalyticsDashboardQueryResolver)
    balance_dashboard = graphene.Field(BalanceDashboardQueryResolver)
    dashboard_facade = graphene.Field(DashboardFacadeQueryResolver)
    user_account = graphene.Field(UserAccountQueryResolver)
