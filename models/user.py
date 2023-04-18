from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Définition de la classe User avec les attributs nom, prenom, motdepasse, email
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    motdepasse = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

