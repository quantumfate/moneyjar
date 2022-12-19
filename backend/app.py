from api import schema
from api.resolvers import resolvers
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from helpers.database.connections import *
from helpers.database.utils import *
from sqlalchemy.orm import scoped_session, sessionmaker

# initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/mydatabase'
db = SQLAlchemy(app)

# create a scoped session to manage database transactions
Session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=db.engine))

# define your GraphQL schema and resolvers

# create a GraphQL view
view_func = GraphQLView.as_view('graphql', schema=schema, resolvers=resolvers)
app.add_url_rule('/graphql', view_func=view_func)

# define a context manager to manage database sessions


@app.context_manager
def session_scope():
    """Provide a transactional scope around a series of database operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


# import your models and database utilities

# define any additional routes or functionality for your Flask app

@app.route('/')
def index():
    return 'Welcome to my GraphQL API!'


if __name__ == '__main__':
    app.run()
