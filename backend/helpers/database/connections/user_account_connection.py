from app import db, session
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from helpers.database.base import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import BYTEA, UUID
from sqlalchemy.orm import Session


class UserAccountConnection(Base, db.Model):
    __tablename__ = 'user_account'

    user_account_id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False)
    dashboard_facade_id = Column(UUID(as_uuid=True), ForeignKey(
        'dashboard_facade.dashboard_facade_id'))
    dashboard_facade = db.relationship(
        'DashboardFacadeConnection', uselist=False)
    user_name = Column("username", String, unique=True, nullable=False)
    forename = Column("forename", String, nullable=False)
    surname = Column("surname", String, nullable=False)
    email = Column("email", String, nullable=False)
    password_hash = Column("password_hash", BYTEA, nullable=False)
    allocation_salt = Column("allocation_salt", BYTEA, nullable=False)
