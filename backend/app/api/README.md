# API

This folder contains the code for the GraphQL API of the app. It is structured as follows:

## [Interfaces](/backend/app/api/interfaces/)

This folder contains interface types that are used in the GraphQL schema. An interface type is a abstract type that defines a set of fields that a concrete type must include in order to implement the interface.

## [Mutations](/backend/app/api/mutations/)

This folder contains the code for GraphQL mutations, which are used to modify data on the server. Each subfolder within mutations corresponds to a specific entity or resource in the app, and contains the code for the mutations that operate on that entity or resource.

## Queries and Resolvers

- queries and resolvers are defined in private classes and the implementation is inherited by their
respective public Query class that is made available by the query module:

```python
__all__ = [
    'BalanceFundQuery',
    'BalanceJarQuery',
    'IncomeTransactionQuery',
    'ExpenseTransactionQuery',
    'SavingStrategyQuery',
    'TransactionScheduleQuery',
    'AllocationFacadeQuery',
    'AnalyticsDashboardQuery',
    'BalanceDashboardQuery',
    'DashboardFacadeQuery',
    'UserAccountQuery',
    'Query'
]
```

- each query inherits a field `uuid` and a resolver method `resolve_uuid` form the [global interface](/backend/app/api/interfaces/global_interface.py):

```python
class GlobalInterface(graphene.Interface):
    uuid = graphene.UUID(required=True)
    
    def resolve_uuid(self, info):
        return self.uuid
```

```python
class _UserAccountQuery(ObjectType):
    class Meta:
        interfaces = (GlobalInterface,)
```

## [Queries](/backend/app/api/queries/)

This folder contains the code for GraphQL queries, which are used to request data from the server. Like mutations, each subfolder within queries corresponds to a specific entity or resource in the app, and contains the code for the queries that operate on that entity or resource.

### [Resolvers](/backend/app/api/resolvers/)

This folder contains the code for resolvers, which are responsible for actually fetching the data that is requested by a GraphQL query or mutation. Each subfolder within resolvers corresponds to a specific entity or resource in the app, and contains the code for the resolvers that operate on that entity or resource.

## [Schemas](/backend/app/api/schemas/)

This folder contains the code for the GraphQL schema, which defines the types, fields, and operations that are available in the API. Each subfolder within schemas corresponds to a specific entity or resource in the app, and contains the code for the types and fields that represent that entity or resource in the schema.
