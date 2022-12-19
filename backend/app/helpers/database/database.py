
from app.helpers import Logger, LogType
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import Config as database_config

database_log = Logger(LogType.DATABASE)
from app import app, app_config

db = SQLAlchemy(app)
database_log.log_info("Database object db was created.")

# create a scoped session to manage database transactions
Session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=db.engine))
database_log.log_info("Database object db was created.")
engine = create_engine(
    app_config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
metadata = MetaData(naming_convention=database_config.convention)
Base = declarative_base(metadata=metadata)
Base.metadata.bind = engine
