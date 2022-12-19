# from sqlalchemy.orm import query
from helpers.database.base import database_log
from helpers.database.connections.user_account_connection import \
    UserAccountConnection

from backend.app import db, session


class UserAccountUtils:

    @classmethod
    def query_all_users(self):
        return session.query(UserAccountConnection).all()

    def add_new_user(name, email):
        database_log.log_info("New User added.")
        new_user = UserAccountConnection(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(user_id, name, email):
        user = db.session.query(UserAccountConnection).get(user_id)
        user.name = name
        user.email = email
        db.session.commit()
        return user

    def delete_user(user_id):
        user = db.session.query(UserAccountConnection).get(user_id)
        db.session.delete(user)
        db.session.commit()
        return user

    def edit_user_password(user_id, password):
        user = db.session.query(UserAccountConnection).get(user_id)
        user.set_password(password)
