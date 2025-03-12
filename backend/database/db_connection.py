import mysql.connector
from mysql.connector import Error

def create_connection():
    """Établit une connexion à la base de données MySQL."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Remplace par ton hôte de base de données
            user="root",       # Ton utilisateur de base de données
            password="password",  # Ton mot de passe de base de données
            database="egapro"   # Nom de la base de données
        )
        if connection.is_connected():
            print("Connexion à la base de données réussie")
    except Error as e:
        print(f"Erreur de connexion : {e}")
    return connection

# Exemple d'utilisation
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()
