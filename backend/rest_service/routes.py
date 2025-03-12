# backend/rest_service/routes.py
from flask_restx import Namespace, Resource, fields
from flask import Blueprint, jsonify
import mysql.connector
from mysql.connector import Error

# Définir un Blueprint pour organiser les routes
api_routes = Namespace('api', description='Opérations liées à l\'index égalité hommes-femmes')

# Configuration de la connexion à la base de données
def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql-ewan.alwaysdata.net',
        database='ewan_exo_brun',
        user='ewan',
        password='Ewan123!'
    )
    return connection

# Modèle Swagger pour une structure
structure_model = api_routes.model('Structure', {
    'SIREN': fields.String(required=True, description='Le SIREN de la structure'),
    'Raison Sociale': fields.String(description='La raison sociale de l\'entreprise'),
    'Année': fields.Integer(description='L\'année de l\'index'),
    'Note Index': fields.String(description='La note de l\'index d\'égalité')
})

# Route pour récupérer toutes les entrées de la base de données
@api_routes.route('/structures')
class StructuresList(Resource):
    def get(self):
        """Récupérer toutes les structures"""
        try:
            # Connexion à la base de données
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)  # Pour retourner les résultats sous forme de dictionnaire
            cursor.execute("SELECT * FROM index_egalite_fh")  # Remplace par ta table
            result = cursor.fetchall()
            
            # Fermer la connexion à la base de données
            cursor.close()
            connection.close()
            
            return jsonify(result)  # Retourne les données en format JSON

        except Error as e:
            return jsonify({"error": str(e)}), 500

# Route pour récupérer une structure spécifique par SIREN
@api_routes.route('/structures/<siren>')
@api_routes.doc(params={'siren': 'Le SIREN de la structure'})
class StructureBySiren(Resource):
    @api_routes.marshal_with(structure_model)  # Utilisation du modèle pour la réponse
    def get(self, siren):
        """Récupérer une structure par son SIREN"""
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM index_egalite_fh WHERE SIREN = %s", (siren,))
            result = cursor.fetchone()  # On utilise fetchone() car il y a un seul résultat pour un SIREN donné
            
            cursor.close()
            connection.close()
            
            if result:
                return jsonify(result)
            else:
                return jsonify({"error": "Structure non trouvée"}), 404
        except Error as e:
            return jsonify({"error": str(e)}), 500
