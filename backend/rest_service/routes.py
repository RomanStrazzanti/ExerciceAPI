# backend/rest_service/routes.py
from flask import Blueprint, jsonify
import mysql.connector
from mysql.connector import Error

# Définir un Blueprint pour organiser les routes
api_routes = Blueprint('api', __name__, url_prefix='/api')

# Configuration de la connexion à la base de données
def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql-ewan.alwaysdata.net',
        database='ewan_exo_brun',
        user='ewan',
        password='Ewan123!'
    )
    return connection

# Route pour récupérer toutes les entrées de la base de données
@api_routes.route('/structures', methods=['GET'])
def get_structures():
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


@api_routes.route('/structures/<siren>', methods=['GET'])
def get_structure_by_siren(siren):
    try:
        # Connexion à la base de données
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Exécute la requête pour récupérer les résultats par SIREN
        cursor.execute("SELECT * FROM index_egalite_fh WHERE SIREN = %s", (siren,))

        # On utilise fetchone() car il y a un seul résultat pour un SIREN donné
        result = cursor.fetchone()

        # Assurer que tous les résultats sont récupérés avant de fermer la connexion
        cursor.fetchall()  # Vider tous les résultats non lus

        # Fermer le curseur et la connexion
        cursor.close()
        connection.close()

        # Retourner le résultat trouvé ou une erreur si aucun résultat
        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "Structure non trouvée"}), 404
    except Error as e:
        return jsonify({"error": str(e)}), 500


