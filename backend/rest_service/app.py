# backend/rest_service/app.py
from flask import Flask
from flask_restx import Api
from routes import api_routes

# Création de l'application Flask
app = Flask(__name__)

# Initialisation de l'API Swagger avec Flask-RESTX
api = Api(app, version='1.0', title='Exercice API',
          description='Documentation de l\'API REST pour l\'index égalité hommes-femmes')

# Enregistrement des routes API
api.add_namespace(api_routes)  # Utilise la méthode add_namespace au lieu de register_blueprint

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # L'API sera disponible sur http://localhost:5000
