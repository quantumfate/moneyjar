import os

from dotenv import load_dotenv

load_dotenv()



class Config():

    # Current path
    LOG_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    LOG_FILE_NAME = 'app.log'
    LOG_API_DIR = 'api'
    LOG_API_FILE_NAME = 'api.log'
    LOG_DB_DIR = 'database'
    LOG_DB_FILE_NAME = 'db.log'
    LOG_MODELS_DIR = 'models'
    LOG_MODELS_FILE_NAME = 'models.log'
    LOG_TESTS_DIR = 'tests'
    LOG_TESTS_FILE_NAME = 'tests.log'
    
