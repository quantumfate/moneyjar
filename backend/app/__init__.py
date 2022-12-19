from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

# initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/mydatabase'
db = SQLAlchemy(app)

from .api import *
from .helpers import *
from .models import *

# create a scoped session to manage database transactions
Session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=db.engine))
# define your GraphQL schema and resolvers
# create a GraphQL view
view_func = GraphQLView.as_view('graphql', schema=schema, resolvers=None)