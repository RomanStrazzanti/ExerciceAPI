from flask import Flask
from flask_jsonrpc import JSONRPC
import mysql.connector
import os

app = Flask(__name__)
jsonrpc = JSONRPC(app, "/api/rpc")

# Connexion à MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql-ewan.alwaysdata.net"),
        user=os.getenv("DB_USER", "ewan"),
        password=os.getenv("DB_PASSWORD", "Ewan123!"),
        database=os.getenv("DB_NAME", "ewan_exo_brun")
    )

@jsonrpc.method("get_egapro", result_type=dict)
def get_egapro(siren: str) -> dict:  # Déclare explicitement le type de retour comme un dict
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Exécuter la requête SQL sur la table index_egalite_fh
        cursor.execute("SELECT * FROM index_egalite_fh WHERE siren = %s", (siren,))
        data = cursor.fetchone()
        conn.close()

        # Vérifier si un résultat est trouvé
        if data:
            # Retourner un dictionnaire avec les données récupérées
            return {
                "siren": data[0],
                "nom": data[1],
                "index": data[2],
                "champ4": data[3],
                "champ5": data[4],
                "champ6": data[5],
                "champ7": data[6],
                "champ8": data[7],
                "champ9": data[8],
                "champ10": data[9],
                "champ11": data[10],
                "champ12": data[11],
                "champ13": data[12],
                "champ14": data[13],
                "champ15": data[14],
                "champ16": data[15],
                "champ17": data[16],
                "champ18": data[17],
            }
        else:
            # Retourner un dictionnaire avec une clé d'erreur si aucune donnée n'est trouvée
            return {"error": "Entreprise non trouvée"}
    
    except Exception as e:
        # Si une erreur survient, retourner un dictionnaire d'erreur
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

# Recherche de données par numéro de siren dans le body
### Requete a faire : url : http://localhost:5001/api/rpc en post, body : {  "jsonrpc": "2.0", "method": "get_egapro",  "params": {    "siren": "351667928"  },  "id": 1} (bien pensé de mettre le body en raw et json)
# Header ne pas oublié : Key: Content-Type, value: application/json

 




