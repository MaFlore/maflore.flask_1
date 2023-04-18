from models.models import Classe, db

def add_classe(libelle):
    new_classe = Classe(libelle=libelle)
    db.session.add(new_classe)
    db.session.commit()

def get_all_classes():
    return Classe.query.all()

def get_classe(id):
    return Classe.query.get(id)

def update_classe(id, libelle):
    classe = Classe.query.get(id)
    classe.libelle = libelle
    db.session.commit()

def delete_classe(id):
    classe = Classe.query.get(id)
    db.session.delete(classe)
    db.session.commit()