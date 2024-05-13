# Importations des bibliothèques




import psycopg2
from psycopg2 import sql




# Définition de la classe Database




class Database:
    
    
    # Constructeur par défaut
    
    
    def __init__(self, host, database, user, password):
        
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None


    # Définition des méthodes


    def connect(self):
        
        self.conn = psycopg2.connect(host = self.host, database = self.database, user = self.user, password = self.password)


    def disconnect(self):
        
        if self.conn is not None:
            self.conn.close()


    def execute_query(self, query):
        
        if self.conn is None:
            raise Exception("Connection to database is not established.")
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()


    def create_table(self, table_name, columns):
        
        query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(sql.SQL("{} {}").format(
                sql.Identifier(column_name),
                sql.SQL(column_type)
            ) for column_name, column_type in columns.items())
        )
        self.execute_query(query)


    def grant_privileges(self, username, privileges, table_name):
        
        query = sql.SQL("GRANT {} ON {} TO {}").format(
            sql.SQL(', ').join(sql.SQL(privilege) for privilege in privileges),
            sql.Identifier(table_name),
            sql.Identifier(username)
        )
        self.execute_query(query)


    def revoke_privileges(self, username, privileges, table_name):
        
        query = sql.SQL("REVOKE {} ON {} FROM {}").format(
            sql.SQL(', ').join(sql.SQL(privilege) for privilege in privileges),
            sql.Identifier(table_name),
            sql.Identifier(username)
        )
        self.execute_query(query)




# Programme principal




if __name__ == '__main__':
    
    # Exemple d'utilisation de la classe Database
    db = Database(host="localhost", database="", user="", password="")
    db.connect()

    # Création d'une table
    columns = {"id": "SERIAL PRIMARY KEY", "name": "VARCHAR(255)", "age": "INTEGER"}
    db.create_table("users", columns)

    # Accord de privilèges à un utilisateur
    db.grant_privileges("user1", ["SELECT", "INSERT", "UPDATE", "DELETE"], "users")

    # Révocation de privilèges à un utilisateur
    db.revoke_privileges("user1", ["INSERT", "UPDATE", "DELETE"], "users")

    # Déconnexion de la base de données
    db.disconnect()
    