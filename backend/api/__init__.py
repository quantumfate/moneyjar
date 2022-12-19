import graphene
from graphene import ObjectType, Schema

from backend.api.queries.queries import Query

# Attach the root query to the schema
schema = graphene.Schema(query=Query)
