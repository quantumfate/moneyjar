from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from graphene import ObjectType, String, Schema
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.resolvers import Query
from backend.helpers.database.connections.user_connection import User as UserUtil
from .config import Config

# Create a Flask app and add a route for the GraphQL endpoint
app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(Config) # Load configuration


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=Schema(query=Query)))

schema = Schema(query=Query)

# Run the Flask app
if __name__ == '__main__':
    app.run()