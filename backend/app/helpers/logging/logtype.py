from enum import Enum

from .config import Config


class LogType(Enum):
    """
    Defines available Log options and provides directory names.
    """
    API = Config.LOG_API_DIR
    DATABASE = Config.LOG_DB_DIR
    MODEL = Config.LOG_MODELS_DIR
    TEST = Config.LOG_TESTS_DIR
    APP = Config.LOG_DIRECTORY