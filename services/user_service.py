from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User, db

def create_user(nom, prenom, motdepasse, email):
    user = User(nom=nom, prenom=prenom, motdepasse=generate_password_hash(motdepasse), email=email)
    db.session.add(user)
    db.session.commit()

def find_user_by_email(email):
    return User.query.filter_by(email=email).first()

def verify_password(user, password):
    return check_password_hash(user.motdepasse, password)
