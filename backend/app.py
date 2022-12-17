from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene import ObjectType, String, Schema
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.resolvers import Query
from api.schema import User
from backend.helpers.database.connections.user_account_connection import User as UserUtil

# Create a Flask app and add a route for the GraphQL endpoint
app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=Schema(query=Query)))

# Define a query class that represents the available queries in your schema
class Query(SQLAlchemyObjectType):
    class Meta:
        model = UserUtil
        interfaces = (ObjectType,)

schema = Schema(query=Query)

# Run the Flask app
if __name__ == '__main__':
    app.run()