from models.models import Filiere, db

def add_filiere(libelle):
    new_filiere = Filiere(libelle=libelle)
    db.session.add(new_filiere)
    db.session.commit()

def get_all_filieres():
    return Filiere.query.all()

def get_filiere(id):
    return Filiere.query.get(id)

def update_filiere(id, libelle):
    filiere = Filiere.query.get(id)
    filiere.libelle = libelle
    db.session.commit()

def delete_filiere(id):
    filiere = Filiere.query.get(id)
    db.session.delete(filiere)
    db.session.commit()