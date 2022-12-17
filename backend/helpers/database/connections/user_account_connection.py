from app import db
from utils.user_account_utils import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import BYTEA
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String, JSON


class UserAccountConnection(db.Model):
    __tablename__ = 'user_account'

    user_account_id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False)
