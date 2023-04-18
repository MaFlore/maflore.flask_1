from flask import jsonify, request
from flask_restx import Namespace, Resource, fields
from models.user import User
from services.user_service import create_user, find_user_by_email, verify_password
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Namespace('auth', description='Endpoints pour la gestion de l\'authentification')

signup_model = api.model('Signup', {
    'nom': fields.String(required=True),
    'prenom': fields.String(required=True),
    'motdepasse': fields.String(required=True),
    'email': fields.String(required=True)
})

login_model = api.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

@api.route('/signup')
class Signup(Resource):
    @api.expect(signup_model)
    def post(self):
        nom = request.json.get('nom')
        prenom = request.json.get('prenom')
        motdepasse = request.json.get('motdepasse')
        email = request.json.get('email')

        # Vérification que l'utilisateur n'existe pas déjà dans la base de données
        existing_user = find_user_by_email(email)
        if existing_user:
            return {'message': 'Cet utilisateur existe déjà.'}, 400
        create_user(nom, prenom, motdepasse, email)
        return {'message': 'Utilisateur crée avec succès.'}, 201


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        user = find_user_by_email(email)
        if not user or not verify_password(user, password):
            return {'message': 'Identifiants incorrects.'}, 401
        
        # Génération du token JWT pour l'utilisateur authentifié
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200


@api.route('/protected')
class Protected(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        
        return {'message': 'Bienvenue ' + user.prenom + ' ' + user.nom + '.'}, 200

