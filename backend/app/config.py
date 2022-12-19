import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    This class holds configuration options for the Flask app.
    """
    # Set the environment to development or production
    ENV = os.getenv("APP_STAGE")
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Set the database URI based on the environment
    if ENV == 'production':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')
