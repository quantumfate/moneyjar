import logging
import os
from enum import Enum

from .config import Config as log_config


class Logger:
    """
    Author: Leon Connor Holm leon-holm@outlook.de

    A class for creating logger instances that write log messages to a file.

    The logger has three log levels: info, warning, and error. The log level can be specified when creating an
    instance of the logger, or it can be left at the default level (info).

    The log file can be specified when creating an instance of the logger, or it can be left at the default location
    (the same directory as the Logger module).

    Examples:
    - Create a logger with the default log level and log file path:
        logger = Logger(__name__)
    - Create a logger with a custom log level and default log file path:
        logger = Logger.from_custom_level(__name__, logging.DEBUG)
    - Create a logger with a custom log file path and default log level:
        logger = Logger(__name__, log_type=LogType.API)
    - Create a logger with a custom log level and log file path:
        logger = Logger(__name__, log_type=LogType.API, level=logging.DEBUG)

    Attributes:
    - LogType (Enum): The log types.
    - logger (Logger): The logger instance.
    - log_file_paths (dict): A dictionary of file paths for different log types.
    """
    class LogType(Enum):
        API = log_config.LOG_API_DIR
        DATABASE = log_config.LOG_DB_DIR
        MODEL = log_config.LOG_MODELS_DIR
        TEST = log_config.LOG_TESTS_DIR
        APP = log_config.LOG_DIRECTORY

    log_file_paths = {
        LogType.API: os.path.join(
            log_config.LOG_DIRECTORY, LogType.API, log_config.LOG_API_FILE_NAME),
        LogType.DATABASE: os.path.join(
            log_config.LOG_DIRECTORY, LogType.DATABASE, log_config.LOG_DB_FILE_NAME),
        LogType.MODEL: os.path.join(
            log_config.LOG_DIRECTORY, LogType.MODEL, log_config.LOG_MODELS_FILE_NAME),
        LogType.TEST: os.path.join(
            log_config.LOG_DIRECTORY, LogType.TEST, log_config.LOG_TESTS_FILE_NAME),
        LogType.APP: os.path.join(
            log_config.LOG_DIRECTORY, log_config.LOG_FILE_NAME),
    }

    def __init__(self, name, logtype=LogType.APP, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create the log file in the Logger module directory
        file_handler = self._get_default_filehandler(logtype)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    @classmethod
    def _get_default_filehandler(cls, log_type):
        """
        Returns the file handler for the specified log type.

        Parameters:
        - log_type (LogType): The type of log to get the file handler for.

        Returns:
        - A file handler for the specified log type. If the log type is not found, a default file handler is returned.
        """
        try:
            return logging.FileHandler(cls.log_file_paths[log_type])
        except KeyError:
            return logging.FileHandler(cls._DEFAULT_PATH)

    @classmethod
    def from_custom_level(cls, name, level):
        """
        Alternative constructor for creating a Logger instance with a custom log level.

        Parameters:
        - name (str): The name of the logger.
        - level (int): The log level to use for the logger.

        Returns:
        - A new Logger instance with the specified log level.
        """
        return cls(name, level)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)
