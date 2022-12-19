import app
from app import app, view_func
from app.helpers.database import Session

app.add_url_rule('/graphql', view_func=view_func)


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
