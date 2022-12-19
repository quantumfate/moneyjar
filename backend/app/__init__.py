from app.helpers import Logger
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import Config as app_config

app_log = Logger("app_log")
# initialize Flask app and SQLAlchemy
app = Flask(__name__)
app_log.log_info("Flask app created.")
app.config['SQLALCHEMY_DATABASE_URI'] = app_config.SQLALCHEMY_DATABASE_URI

import app.helpers.database

from .api import *
from .helpers import *

# from .models import *

# create a scoped session to manage database transactions

view_func = GraphQLView.as_view('graphql', schema=schema, resolvers=None)
