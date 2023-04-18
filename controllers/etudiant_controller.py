from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from services.etudiant_service import get_all_etudiants, get_etudiant, add_etudiant, update_etudiant, delete_etudiant
from flask_jwt_extended import jwt_required

api = Namespace('etudiants', description='Endpoints pour la gestion des étudiants')

etudiant_model = api.model('Etudiant', {
    'nom': fields.String(required=True),
    'prenom': fields.String(required=True),
    'date_naissance': fields.String(required=True),
    'numero_matricule': fields.String(required=True),
    'id_classe': fields.String(required=True),
    'id_filiere': fields.String(required=True)
})

@api.route('/', methods=['GET'])
class GetsEtudiants(Resource):
    @jwt_required()
    def get(self):
        etudiants = get_all_etudiants()
        return jsonify([{'id': etudiant.id, 'nom': etudiant.nom, 'prenom': etudiant.prenom,
                     'date_naissance': etudiant.date_naissance, 'numero_matricule': etudiant.numero_matricule,
                     'id_classe': etudiant.id_classe, 'id_filiere': etudiant.id_filiere} for etudiant in etudiants])
    
@api.route('/<id>', methods=['GET'])
class GetEtudiant(Resource):
    @jwt_required()
    def get(self):
        etudiant = get_etudiant(id)
        if not etudiant:
            return jsonify({'message': 'Étudiant introuvable'})
        return jsonify({'id': etudiant.id, 'nom': etudiant.nom, 'prenom': etudiant.prenom,
                     'date_naissance': etudiant.date_naissance, 'numero_matricule': etudiant.numero_matricule,
                     'id_classe': etudiant.id_classe, 'id_filiere': etudiant.id_filiere})

@api.route('/add/', methods=['POST'])
class AddEtudiant(Resource):
    @jwt_required()
    @api.expect(etudiant_model)
    def post(self):
        nom = request.json.get('nom')
        prenom = request.json.get('prenom')
        date_naissance = request.json.get('date_naissance')
        numero_matricule = request.json.get('numero_matricule')
        id_classe = request.json.get('id_classe')
        id_filiere = request.json.get('id_filiere')
        add_etudiant(nom, prenom, date_naissance, numero_matricule, id_classe, id_filiere)
        return jsonify({'message': 'Étudiant ajouté avec succès!'})

@api.route('/update/<id>', methods=['PUT'])
class UpdateEtudiant(Resource):
    @jwt_required()
    @api.expect(etudiant_model)
    def put(self, id):
        etudiant = get_etudiant(id)
        if not etudiant:
            return jsonify({'message': 'Étudiant introuvable'})
        nom = request.json.get('nom')
        prenom = request.json.get('prenom')
        date_naissance = request.json.get('date_naissance')
        numero_matricule = request.json.get('numero_matricule')
        id_classe = request.json.get('id_classe')
        id_filiere = request.json.get('id_filiere')
        update_etudiant(id, nom, prenom, date_naissance, numero_matricule, id_classe, id_filiere)
        return jsonify({'message': 'Étudiant mis à jour avec succès!'})

@api.route('/delete/<id>', methods=['DELETE'])
class DeleteEtudiant(Resource):
    @jwt_required()
    def delete(self, id):
        etudiant = get_etudiant(id)
        if not etudiant:
            return jsonify({'message': 'Étudiant introuvable'})
        delete_etudiant(id)
        return jsonify({'message': 'Étudiant supprimé avec succès!'})