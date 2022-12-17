from contextlib import contextmanager
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from .config import Config

engine = create_engine(Config.db_url, convert_unicode=True)
metadata = MetaData(naming_convention=Config.convention)
Base = declarative_base(metadata=metadata)
Base.metadata.bind = engine