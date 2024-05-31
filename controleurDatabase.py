# Importation des bibliothèques




import psycopg2
import pandas as pd
from PyQt6.QtWidgets import QLineEdit, QCheckBox
from PyQt6.QtCore import QObject, pyqtSignal




# Définition de la classe controleurDatabase




class controleurDatabase(QObject):


    signal = pyqtSignal(list)


    # Constructeur par défaut
        
    
    def __init__(self, vuedatabase):
        
        super().__init__()
        self.vuedatabase = vuedatabase
        self.connection = None
        self.cursor = None
        self.table_list = []

    
    # Définition des méthodes


    def toggle_password_visibility(self):
        
        if self.vuedatabase.groupbox_connection_checkbox.isChecked() == True:
            self.vuedatabase.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.vuedatabase.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)


    def connect(self):
    
        try:
            # Connexion à la base de données
            self.connection = psycopg2.connect(
                host = self.vuedatabase.groupbox_connection_host_lineedit.text(),
                database = self.vuedatabase.groupbox_connection_database_name_lineedit.text(),
                user = self.vuedatabase.groupbox_connection_username_lineedit.text(),
                password = self.vuedatabase.groupbox_connection_password_lineedit.text()
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
            self.cursor = self.connection.cursor()
            
            if self.cursor:
                # Exécuter une requête SQL pour récupérer tous les noms de tables
                self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

                # Récupérer les résultats de la requête
                tables = self.cursor.fetchall()
            
                if tables:
                    for table in tables:
                        table = table[0]
                        checkbox = QCheckBox(str(table))
                        self.vuedatabase.groupbox_table_layout.addWidget(checkbox)
                    self.vuedatabase.groupbox_connection_button.setEnabled(False)
                    self.vuedatabase.groupbox_table.setEnabled(True)
                    self.vuedatabase.groupbox_button.setEnabled(False)
    
    
    def table_confirm(self):
        
        for i in range(0, self.vuedatabase.groupbox_table_layout.count()):
            if isinstance(self.vuedatabase.groupbox_table_layout.itemAt(i).widget(), QCheckBox):
                if self.vuedatabase.groupbox_table_layout.itemAt(i).widget().isChecked():
                    self.table_list.append(self.vuedatabase.groupbox_table_layout.itemAt(i).widget().text())
        
        self.vuedatabase.groupbox_connection_button.setEnabled(False)
        self.vuedatabase.groupbox_table.setEnabled(False)
        self.vuedatabase.groupbox_button.setEnabled(True)
    
    
    def import_data(self):
    
        dataframe_list = []
    
        if self.cursor:
    
            for table in self.table_list:
            
                # Exécuter une requête SQL pour récupérer les 1000 premières lignes de la première table
                self.cursor.execute(f"SELECT * FROM {table} FETCH FIRST 1000 ROWS ONLY;")
            
                # Récupérer les résultats de la requête
                rows = self.cursor.fetchall()
                
                filtered_rows = []
                
                for row in rows:
                    filtered_row = []
                    for value in row:
                        if (isinstance(value, list) or isinstance(value, tuple)) and len(value) > 0:
                            filtered_row.append(value[0])
                        else:
                            filtered_row.append(value)
                    filtered_rows.append(filtered_row)
                
                if self.cursor.description:
                    dataframe_list.append(pd.DataFrame(filtered_rows, columns=[desc[0] for desc in self.cursor.description]))
            
            # Fermeture du curseur
            self.cursor.close()
            self.disconnect()
            
        self.signal.emit(["", dataframe_list])
        
        self.vuedatabase.close()
    