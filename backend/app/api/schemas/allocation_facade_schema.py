from app.models import AllocationFacade
from graphene_sqlalchemy import SQLAlchemyObjectType


class AllocationFacadeSchema(SQLAlchemyObjectType):

    # Define the UserAccountType using the SQLAlchemyObjectType
    class Meta:
        model = AllocationFacade
        # Specify which fields of the UserAccount model should be exposed in the GraphQL API
        fields = ('id', 'username', 'email', 'password_hash')
