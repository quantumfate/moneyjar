import graphene
from app.api.queries import Query

# Attach the root query to the schema
schema = graphene.Schema(query=Query)
