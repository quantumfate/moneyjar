from app import db

def query_all_users():
    return db.session.query(db.User).all()

def add_new_user(name, email):
    new_user = db.User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id, name, email):
    user = db.session.query(db.User).get(user_id)
    user.name = name
    user.email = email
    db.session.commit()
    return user

def delete_user(user_id):
    user = db.session.query(db.User).get(user_id)
    db.session.delete(user)
    db.session.commit()
    return user
