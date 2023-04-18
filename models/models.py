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


class Classe(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50))
    etudiants = db.relationship('Etudiant', backref='classe', lazy=True)


class Filiere(db.Model):
    __tablename__ = 'filieres'
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50))
    etudiants = db.relationship('Etudiant', backref='filiere', lazy=True)

class Etudiant(db.Model):
    __tablename__ = 'etudiants'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    date_de_naissance = db.Column(db.Date)
    numero_matricule = db.Column(db.String(20))
    filiere_id = db.Column(db.Integer, db.ForeignKey('filieres.id'))
    classe_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
