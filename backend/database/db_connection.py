import mysql.connector
from mysql.connector import Error

def test_connection():
    """Tester la connexion à la base de données MySQL"""
    connection = None  # Initialiser la variable connection en dehors du bloc try
    try:
        # Crée la connexion à la base de données
        connection = mysql.connector.connect(
            host='mysql-ewan.alwaysdata.net',      # Remplace par l'hôte de ta base de données (par défaut localhost si local)
            database='ewan_exo_brun',     # Nom de ta base de données
            user='ewan',       # Ton nom d'utilisateur MySQL
            password='Ewan123!'    # Ton mot de passe MySQL
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connecté à la base de données MySQL version {db_info}")
            
            # On peut également tester si une simple requête fonctionne
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Vous êtes connecté à la base de données : {record[0]}")
        
    except Error as e:
        print(f"Erreur de connexion à la base de données: {e}")
    
    finally:
        # Si la connexion est réussie, on la ferme à la fin
        if connection and connection.is_connected():  # Vérifier que la connexion existe et est ouverte
            connection.close()
            print("Connexion fermée")

# Exécuter le test de connexion
if __name__ == "__main__":
    test_connection()

