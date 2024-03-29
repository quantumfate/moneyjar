from contextlib import contextmanager

from app import Config as app_config
from helpers.logging.logger import Logger, logging
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import Config as database_config

database_log = Logger(Logger.LogType.DATABASE, logging.DEBUG)

engine = create_engine(
    app_config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
metadata = MetaData(naming_convention=database_config.convention)
Base = declarative_base(metadata=metadata)
Base.metadata.bind = engine
