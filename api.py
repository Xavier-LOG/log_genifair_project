import psycopg2

# Informations de connexion à la base de données
host = "127.0.0.1"
database = "db"
user = "user"
password = "password"

# Connexion à la base de données
conn = psycopg2.connect(host=host, database=database, user=user, password=password)

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Exemple de requête SELECT
cur.execute("SELECT * FROM coordinates")

# Récupération des résultats
rows = cur.fetchall()
for row in rows:
    print(row)

# Fermeture du curseur et de la connexion
cur.close()
conn.close()
