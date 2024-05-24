# Importation des bibliothèques




import psycopg2




# Définition de la classe controleurDatabase




class controleurDatabase:


    # Constructeur par défaut
        
    
    def __init__(self, vuedatabase):
        
        super().__init__()
        self.vuedatabase = vuedatabase
        self.host = self.vuedatabase.host_lineedit.text()
        self.database = self.vuedatabase.database_name_lineedit.text()
        self.user = self.vuedatabase.username_lineedit.text()
        self.password = self.vuedatabase.password_lineedit.text()
        self.connection = None

    
    # Définition des méthodes


    def connect(self):
    
        try:
            # Connexion à la base de données
            self.connection = psycopg2.connect(
                host = self.host,
                database = self.database,
                user = self.user,
                password = self.password
            )
            self.load_data()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def disconnect(self):

        if self.connection is not None:
            # Fermeture de la connexion
            self.connection.close()


    def load_data(self):
    
        if self.connection is not None:
            # Création d'un curseur pour exécuter des requêtes SQL
            cursor = self.connection.cursor()
            
            # Exécuter une requête SQL pour récupérer tous les noms de tables
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

            # Récupérer les résultats de la requête
            tables = cursor.fetchall()
            
            for table in tables:
            
                table = table[0]
                # Exécuter une requête SQL pour récupérer les 2 premières lignes de la première table
                cursor.execute(f"SELECT * FROM {table} FETCH FIRST 2 ROWS ONLY;")
            
                # Récupérer les résultats de la requête
                rows = cursor.fetchall()
                
                print(rows)
            
            # Fermeture du curseur
            cursor.close()
            self.disconnect()
    