from models.models import Etudiant, db

def add_etudiant(nom, prenom, date_naissance, numero_matricule, id_classe, id_filiere):
    new_etudiant = Etudiant(nom=nom, prenom=prenom, date_naissance=date_naissance,
                            numero_matricule=numero_matricule, id_classe=id_classe, id_filiere=id_filiere)
    db.session.add(new_etudiant)
    db.session.commit()

def get_all_etudiants():
    return Etudiant.query.all()

def get_etudiant(id):
    return Etudiant.query.get(id)

def update_etudiant(id, nom, prenom, date_naissance, numero_matricule, id_classe, id_filiere):
    etudiant = Etudiant.query.get(id)
    etudiant.nom = nom
    etudiant.prenom = prenom
    etudiant.date_naissance = date_naissance
    etudiant.numero_matricule = numero_matricule
    etudiant.id_classe = id_classe
    etudiant.id_filiere = id_filiere
    db.session.commit()

def delete_etudiant(id):
    etudiant = Etudiant.query.get(id)
    db.session.delete(etudiant)
    db.session.commit()