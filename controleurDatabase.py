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
        self.table_dict = {}

    
    # Définition des méthodes


    def toggle_host_visibility(self):
        
        if self.vuedatabase.groupbox_connection_host_checkbox.isChecked() == False:
            self.vuedatabase.groupbox_connection_host_lineedit.setVisible(True)
        else:
            self.vuedatabase.groupbox_connection_host_lineedit.setVisible(False)
    
    
    def toggle_port_visibility(self):
        
        if self.vuedatabase.groupbox_connection_port_checkbox.isChecked() == False:
            self.vuedatabase.groupbox_connection_port_lineedit.setVisible(True)
        else:
            self.vuedatabase.groupbox_connection_port_lineedit.setVisible(False)


    def toggle_password_visibility(self):
        
        if self.vuedatabase.groupbox_connection_checkbox.isChecked() == True:
            self.vuedatabase.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.vuedatabase.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)


    def connect(self):
    
        try:
            
            if self.vuedatabase.groupbox_connection_host_checkbox.isChecked() == True:
                host_variable = "127.0.0.1"
            if self.vuedatabase.groupbox_connection_port_checkbox.isChecked() == True:
                port_variable = "5432"
            
            # Connexion à la base de données
            self.connection = psycopg2.connect(
                host = host_variable,
                database = self.vuedatabase.groupbox_connection_database_name_lineedit.text(),
                user = self.vuedatabase.groupbox_connection_username_lineedit.text(),
                password = self.vuedatabase.groupbox_connection_password_lineedit.text(),
                port = port_variable
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
                        checkbox.stateChanged.connect(lambda state, name = str(table): self.column_settings(name))
                        self.vuedatabase.groupbox_table_layout.addWidget(checkbox)
                    self.vuedatabase.groupbox_connection_button.setEnabled(False)
                    self.vuedatabase.groupbox_table.setEnabled(True)
    
    
    def column_settings(self, name):
        
        if self.cursor:
            
            # Exécuter une requête SQL pour récupérer tous les noms de colonne de la table
            self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name LIKE '{name}'")

            # Récupérer les résultats de la requête
            columns = self.cursor.fetchall()
            
            if columns:
                for column in columns:
                    column = column[0]
                    checkbox = QCheckBox(str(column))
                    checkbox.setObjectName(str(name))
                    checkbox.setChecked(True)
                    self.vuedatabase.groupbox_column_layout.addWidget(checkbox)
                self.vuedatabase.groupbox_table.setEnabled(False)
                self.vuedatabase.groupbox_column.setEnabled(True)
    
    
    def unselect_all_columns(self):
        
        for i in range(0, self.vuedatabase.groupbox_column_layout.count()):
            if isinstance(self.vuedatabase.groupbox_column_layout.itemAt(i).widget(), QCheckBox):
                if self.vuedatabase.groupbox_column_layout.itemAt(i).widget().isChecked() == True:
                    self.vuedatabase.groupbox_column_layout.itemAt(i).widget().setChecked(False)
    
    
    def column_confirm(self):
        
        for i in range(0, self.vuedatabase.groupbox_column_layout.count()):
            if isinstance(self.vuedatabase.groupbox_column_layout.itemAt(i).widget(), QCheckBox):
                if self.vuedatabase.groupbox_column_layout.itemAt(i).widget().isChecked() == True:
                    if self.vuedatabase.groupbox_column_layout.itemAt(i).widget().objectName() in list(self.table_dict.keys()):
                        self.table_dict[self.vuedatabase.groupbox_column_layout.itemAt(i).widget().objectName()].append(self.vuedatabase.groupbox_column_layout.itemAt(i).widget().text())
                    else:
                        self.table_dict[self.vuedatabase.groupbox_column_layout.itemAt(i).widget().objectName()] = []
        for i in reversed(range(3, self.vuedatabase.groupbox_column_layout.count())):
            widget = self.vuedatabase.groupbox_column_layout.itemAt(i).widget()
            if widget is not None:
                self.vuedatabase.groupbox_column_layout.removeWidget(widget)
                widget.deleteLater()
        for i in reversed(range(2, self.vuedatabase.groupbox_table_layout.count())):
            widget = self.vuedatabase.groupbox_table_layout.itemAt(i).widget()
            if widget is not None:
                if isinstance(self.vuedatabase.groupbox_table_layout.itemAt(i).widget(), QCheckBox):
                    if self.vuedatabase.groupbox_table_layout.itemAt(i).widget().isChecked() == True:
                        self.vuedatabase.groupbox_table_layout.removeWidget(widget)
                        widget.deleteLater()
        self.vuedatabase.groupbox_column.setEnabled(False)
        self.vuedatabase.groupbox_table.setEnabled(True)
    
    
    def table_confirm(self):
        
        self.vuedatabase.groupbox_connection_button.setEnabled(False)
        self.vuedatabase.groupbox_table.setEnabled(False)
        self.vuedatabase.groupbox_button.setEnabled(True)
    
    
    def import_data(self):
    
        dataframe_list = []
    
        if self.cursor and len(self.table_dict) > 0:
    
            for table, columns in self.table_dict.items():
            
                columns = ', '.join(columns)
                # Exécuter une requête SQL pour récupérer les 1000 premières lignes de la première table
                self.cursor.execute(f"SELECT {columns} FROM {table} FETCH FIRST 1000 ROWS ONLY;")
            
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
    