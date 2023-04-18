from flask import Flask, jsonify
from flask_restx import Api
from flask_jwt_extended import JWTManager
from models.user import db
from controllers.auth_controller import api as auth_ns
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("TRACK_MODIFICATIONS")
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
db.init_app(app)
jwt = JWTManager(app)
api = Api(app)

# Ajout du namespace auth
api.add_namespace(auth_ns)

@app.route('/')
def index():
    return jsonify({'message': 'Bienvenue dans notre application !'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)