from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from services.classe_service import get_all_classes, get_classe, add_classe, update_classe, delete_classe
from flask_jwt_extended import jwt_required


api = Namespace('classes', description='Endpoints pour la gestion des classes')

classe_model = api.model('Classe', {
    'libelle': fields.String(required=True),
})

@api.route('/', methods=['GET'])
class GetsClasses(Resource):
    @jwt_required()
    def get(self):
        classes = get_all_classes()
        return jsonify([{'id': classe.id, 'libelle': classe.libelle} for classe in classes])
    
@api.route('/<id>', methods=['GET'])
class GetClasse(Resource):
    @jwt_required()
    def get(self):
        classe = get_classe(id)
        if not classe:
            return jsonify({'message': 'Classe introuvable'})
        return jsonify({'id': classe.id, 'libelle':classe.libelle})

@api.route('/add/', methods=['POST'])
class AddClasse(Resource):
    @jwt_required()
    @api.expect(classe_model)
    def post(self):
        libelle = request.json.get('libelle')
        add_classe(libelle=libelle)
        return jsonify({'message': 'Étudiant ajoutée avec succès!'})

@api.route('/update/<id>', methods=['PUT'])
class UpdateClasse(Resource):
    @jwt_required()
    @api.expect(classe_model)
    def put(self, id):
        classe = get_classe(id)
        if not classe:
            return jsonify({'message': 'Classe introuvable'})
        libelle = request.json.get('libelle')
        update_classe(libelle=libelle)
        return jsonify({'message': 'Classe mise à jour avec succès!'})

@api.route('/delete/<id>', methods=['DELETE'])
class DeleteClasse(Resource):
    @jwt_required()
    def delete(self, id):
        classe = get_classe(id)
        if not classe:
            return jsonify({'message': 'Classe introuvable'})
        delete_classe(id)
        return jsonify({'message': 'Classe supprimée avec succès!'})