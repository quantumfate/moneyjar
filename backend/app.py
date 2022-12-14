from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema

# Define a query class that represents the available queries in your schema
class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))

    # This method defines the behavior of the "hello" query
    def resolve_hello(self, info, name):
        return f'Hello {name}!'

# Create a Flask app and add a route for the GraphQL endpoint
app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=Schema(query=Query)))

# Run the Flask app
if __name__ == '__main__':
    app.run()
