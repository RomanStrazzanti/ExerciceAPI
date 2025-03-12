# backend/rest_service/app.py
from flask import Flask
from routes import api_routes

app = Flask(__name__)

# Enregistrement des routes API
app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # L'API sera disponible sur http://localhost:5000
