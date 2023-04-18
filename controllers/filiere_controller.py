from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from services.filiere_service import get_all_filieres, get_filiere, add_filiere, update_filiere, delete_filiere
from flask_jwt_extended import jwt_required


api = Namespace('filieres', description='Endpoints pour la gestion des filières')

filiere_model = api.model('Filiere', {
    'libelle': fields.String(required=True),
})

@api.route('/', methods=['GET'])
class GetsFilieres(Resource):
    @jwt_required()
    def get(self):
        filieres = get_all_filieres()
        return jsonify([{'id': filiere.id, 'libelle': filiere.libelle} for filiere in filieres])
    
@api.route('/<id>', methods=['GET'])
class GetFiliere(Resource):
    @jwt_required()
    def get(self):
        filiere = get_filiere(id)
        if not filiere:
            return jsonify({'message': 'Filière introuvable'})
        return jsonify({'id': filiere.id, 'libelle':filiere.libelle})

@api.route('/add/', methods=['POST'])
class AddFiliere(Resource):
    @jwt_required()
    @api.expect(filiere_model)
    def post(self):
        libelle = request.json.get('libelle')
        add_filiere(libelle=libelle)
        return jsonify({'message': 'Filière ajoutée avec succès!'})

@api.route('/update/<id>', methods=['PUT'])
class UpdateFiliere(Resource):
    @jwt_required()
    @api.expect(filiere_model)
    def put(self, id):
        filiere = get_filiere(id)
        if not filiere:
            return jsonify({'message': 'Filière introuvable'})
        libelle = request.json.get('libelle')
        update_filiere(libelle=libelle)
        return jsonify({'message': 'Filière mise à jour avec succès!'})

@api.route('/delete/<id>', methods=['DELETE'])
class DeleteFiliere(Resource):
    @jwt_required()
    def delete(self, id):
        filiere = get_filiere(id)
        if not filiere:
            return jsonify({'message': 'Filière introuvable'})
        delete_filiere(id)
        return jsonify({'message': 'Filière supprimée avec succès!'})