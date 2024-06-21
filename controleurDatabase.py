# Importation des bibliothèques




import psycopg2
import pandas as pd
from PyQt6.QtWidgets import QLineEdit, QCheckBox
from PyQt6.QtCore import QObject, pyqtSignal
from cryptography.fernet import Fernet
import base64




# Définition de la classe controleurDatabase




class controleurDatabase(QObject):


    signal = pyqtSignal(list)


    # Constructeur par défaut
        
    
    def __init__(self, vuedatabase):
        
        super().__init__()
        self.vuedatabase = vuedatabase
        self.key = ""
        self.connection = None
        self.cursor = None
        self.table_dict = {}

    
    # Définition des méthodes


    def toggle_host_visibility(self):
        
        """_summary_
        Gestion de la visibilité de la ligne de saisie pour saisir l'adresse IP
        """
        
        # Si l'hôte est décoché
        if self.vuedatabase.groupbox_connection_host_checkbox.isChecked() == False:
            # Affichage de la ligne de saisie pour saisir l'adresse IP
            self.vuedatabase.groupbox_connection_host_lineedit.setVisible(True)
        # Sinon
        else:
            # La ligne de saisie pour saisir l'adresse IP reste cachée
            self.vuedatabase.groupbox_connection_host_lineedit.setVisible(False)
    
    
    def toggle_port_visibility(self):
        
        """_summary_
        Gestion de la visibilité de la ligne de saisie pour saisir le port de la base de données
        """
        
        # Si le port est décoché
        if self.vuedatabase.groupbox_connection_port_checkbox.isChecked() == False:
            # Affichage de la ligne de saisie pour saisir le port
            self.vuedatabase.groupbox_connection_port_lineedit.setVisible(True)
        # Sinon
        else:
            # La ligne de saisie pour saisir le port reste cachée
            self.vuedatabase.groupbox_connection_port_lineedit.setVisible(False)


    def toggle_password_visibility(self):

        """_summary_
        Gestion de la visibilité du mot de passe de l'utilisateur
        """

        # Si la visibilité du mot de passe est coché        
        if self.vuedatabase.groupbox_connection_checkbox.isChecked() == True:
            # Le mot de passe est visible
            self.vuedatabase.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Normal)
        # Sinon
        else:
            # Le mot de passe est caché
            self.vuedatabase.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)


    def toggle_key_visibility(self):
        
        """_summary_
        Gestion de la visibilité de la ligne de saisie pour saisir la clé
        """
        
        # Si le port est décoché
        if self.vuedatabase.groupbox_connection_key_checkbox.isChecked() == True:
            # Affichage de la ligne de saisie pour saisir la clé
            self.vuedatabase.groupbox_connection_key_lineedit.setVisible(True)
        # Sinon
        else:
            # La ligne de saisie pour saisir la clé reste cachée
            self.vuedatabase.groupbox_connection_key_lineedit.setVisible(False)


    def connect(self):

        """_summary_
        Connexion à la base de données et affichage des noms des tables de la base de données
        """
    
        try:
            
            # Si l'hôte est coché
            if self.vuedatabase.groupbox_connection_host_checkbox.isChecked() == True:
                # L'hôte est localhost
                host_variable = "127.0.0.1"
            # Si le port est coché
            if self.vuedatabase.groupbox_connection_port_checkbox.isChecked() == True:
                # Le port par défaut est 5432
                port_variable = "5432"
            # Si la clé est cochée
            if self.vuedatabase.groupbox_connection_key_checkbox.isChecked() == True:
                # Clé
                self.key = self.vuedatabase.groupbox_connection_key_lineedit.text()
            
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

        """_summary_
        Déconnexion
        """

        if self.connection is not None:
            # Fermeture de la connexion
            self.connection.close()


    def load_data(self):
    
        """_summary_
        Affichage des noms des tables de la base de données et connexion
        """
    
        if self.connection is not None:
            # Création d'un curseur pour exécuter des requêtes SQL
            self.cursor = self.connection.cursor()

            # Si le curseur existe            
            if self.cursor:
                # Exécuter une requête SQL pour récupérer tous les noms de tables
                self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

                # Récupérer les résultats de la requête
                tables = self.cursor.fetchall()
            
                # Si les tables existent
                if tables:
                    # Parcours de chaque table
                    for table in tables:
                        # Récupération du nom de la table
                        table = table[0]
                        # Création d'une case à cocher pour chaque nom de table
                        checkbox = QCheckBox(str(table))
                        # Connexion de la case à cocher aux paramètres de colonne de la table pour afficher les colonnes à sélectionner
                        checkbox.stateChanged.connect(lambda state, name = str(table): self.column_settings(name))
                        self.vuedatabase.groupbox_table_layout.addWidget(checkbox)
                    self.vuedatabase.groupbox_connection_button.setEnabled(False)
                    self.vuedatabase.groupbox_table.setEnabled(True)
    
    
    def column_settings(self, name):
        
        """_summary_
        Affichage des noms de colonne de la table
        """
        
        if self.cursor:
            
            # Exécuter une requête SQL pour récupérer tous les noms de colonne de la table
            self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name LIKE '{name}'")

            # Récupérer les résultats de la requête
            columns = self.cursor.fetchall()
            
            # Si les colonnes de la table existent
            if columns:
                # Parcours de chaque colonne
                for column in columns:
                    # Récupération du nom de la colonne
                    column = column[0]
                    # Création d'une case à cocher pour chaque nom de colonne
                    checkbox = QCheckBox(str(column))
                    # Création d'un identifiant unique pour la case
                    checkbox.setObjectName(str(name))
                    # La case est déjà cochée (on considère que l'utilisateur récupère par défaut toutes les colonnes de la table)
                    checkbox.setChecked(True)
                    self.vuedatabase.groupbox_column_layout.addWidget(checkbox)
                self.vuedatabase.groupbox_table.setEnabled(False)
                self.vuedatabase.groupbox_column.setEnabled(True)
    
    
    def unselect_all_columns(self):
        
        """_summary_
        Décochage de toutes les cases cochées
        """
        
        # Parcours des indices du layout des colonnes de la table
        for i in range(0, self.vuedatabase.groupbox_column_layout.count()):
            # Si le i-ème widget du layout des colonnes de la table est une case à cocher
            if isinstance(self.vuedatabase.groupbox_column_layout.itemAt(i).widget(), QCheckBox):
                # Si le widget est coché
                if self.vuedatabase.groupbox_column_layout.itemAt(i).widget().isChecked() == True:
                    # Le widget est décoché
                    self.vuedatabase.groupbox_column_layout.itemAt(i).widget().setChecked(False)
    
    
    def column_confirm(self):
        
        """_summary_
        Confirmation de la sélection des colonnes de la table pour passer à la prochaine sélection si une autre table est choisie
        """
        
        # Parcours des indices du layout des colonnes de la table
        for i in range(0, self.vuedatabase.groupbox_column_layout.count()):
            # Si le i-ème widget du layout des colonnes de la table est une case à cocher
            if isinstance(self.vuedatabase.groupbox_column_layout.itemAt(i).widget(), QCheckBox):
                # Si le widget est coché
                if self.vuedatabase.groupbox_column_layout.itemAt(i).widget().isChecked() == True:
                    # Si l'identifiant de la case à cocher est dans la liste des clés du dictionnaire des tables
                    if self.vuedatabase.groupbox_column_layout.itemAt(i).widget().objectName() in list(self.table_dict.keys()):
                        # Ajout du nom de la colonne dans la liste des noms de colonne sélectionnés de la table choisie
                        self.table_dict[self.vuedatabase.groupbox_column_layout.itemAt(i).widget().objectName()].append(self.vuedatabase.groupbox_column_layout.itemAt(i).widget().text())
                    # Sinon
                    else:
                        # Ajout d'une valeur nulle
                        self.table_dict[self.vuedatabase.groupbox_column_layout.itemAt(i).widget().objectName()] = []
        # Pour chaque case à cocher du layout des colonnes de la table (sans compter les boutons)
        for i in reversed(range(3, self.vuedatabase.groupbox_column_layout.count())):
            # Le widget est la case à cocher
            widget = self.vuedatabase.groupbox_column_layout.itemAt(i).widget()
            # Si le widget existe
            if widget is not None:
                # Suppression du widget du layout
                self.vuedatabase.groupbox_column_layout.removeWidget(widget)
                widget.deleteLater()
        # Pour chaque case à cocher du layout des tables (sans compter les boutons)
        for i in reversed(range(2, self.vuedatabase.groupbox_table_layout.count())):
            # Le widget est la case à cocher
            widget = self.vuedatabase.groupbox_table_layout.itemAt(i).widget()
            # Si le widget existe
            if widget is not None:
                # Si le widget est une case à cocher
                if isinstance(self.vuedatabase.groupbox_table_layout.itemAt(i).widget(), QCheckBox):
                    # Si la case à cocher est cochée
                    if self.vuedatabase.groupbox_table_layout.itemAt(i).widget().isChecked() == True:
                        # Suppression du widget du layout
                        self.vuedatabase.groupbox_table_layout.removeWidget(widget)
                        widget.deleteLater()
        self.vuedatabase.groupbox_column.setEnabled(False)
        self.vuedatabase.groupbox_table.setEnabled(True)
    
    
    def table_confirm(self):
    
        """_summary_
        Dégrisage de la confirmation de la sélection actuelle de tables
        """
        
        self.vuedatabase.groupbox_connection_button.setEnabled(False)
        self.vuedatabase.groupbox_table.setEnabled(False)
        self.vuedatabase.groupbox_button.setEnabled(True)
    
        
    def import_data(self):
    
        """_summary_
        Importation des données
        """
    
        dataframe_list = []
    
        if self.cursor and len(self.table_dict) > 0:
    
            # Parcours de chaque table et de sa liste contenant les colonnes sélectionnées
            for table, columns in self.table_dict.items():
            
                # Conversion de la liste des noms de colonne en chaîne de caractères
                columns = ', '.join(columns)
                # Exécuter une requête SQL pour récupérer les 100 premières lignes des colonnes sélectionnées de la table choisie
                self.cursor.execute(f"SELECT {columns} FROM {table} FETCH FIRST 100 ROWS ONLY;")
            
                # Récupérer les résultats de la requête
                rows = self.cursor.fetchall()
            
                # Initialisation d'une variable représentant la liste des lignes filtrées    
                filtered_rows = []
                
                # Parcours de chaque ligne
                for row in rows:
                    # Initialisation d'une variable représentant la ligne filtrée
                    filtered_row = []
                    # Parcours de chaque valeur de la ligne
                    for value in row:
                        # Si la valeur est une chaîne de caractères et qu'elle est cryptée
                        if isinstance(value, str) and controleurDatabase.is_encrypted(value):
                            # Décryptage de la valeur
                            decrypted_value = controleurDatabase.decrypt_data(value.encode(), self.key)
                            # Ajout de la valeur dans la ligne filtrée
                            filtered_row.append(decrypted_value)
                        # Si la valeur n'est pas un tableau
                        elif (isinstance(value, list) or isinstance(value, tuple)):
                            filtered_row.append(None)
                        # Sinon
                        else:
                            # Ajout de la valeur dans la ligne filtrée
                            filtered_row.append(value)
                    # Conversion de la ligne filtrée en tuple
                    filtered_rows.append(tuple(filtered_row))
                
                if self.cursor.description:
                    # Ajout du dataframe contenant les noms de colonne et les lignes filtrées à la liste des dataframes
                    dataframe_list.append(pd.DataFrame(filtered_rows, columns=[desc[0] for desc in self.cursor.description]))
            
            # Fermeture du curseur
            self.cursor.close()
            self.disconnect()
            
            # Emission du signal vers controleurToolbar pour récupérer les dataframes
            self.signal.emit(["", dataframe_list])
    
        # Fermeture de la vue    
        self.vuedatabase.close()
    
    
    # Définition des méthodes statiques
    
    
    @staticmethod
    def decrypt_data(encrypted_data, key):
    
        """_summary_
        Décryptage de la donnée chiffrée avec la clé
        Returns:
            _type_: _description_
        """
        
        # Création de l'objet Fernet avec la clé de décryptage fournie pour préparer l'objet afin de déchiffrer la donnée chiffrée
        fernet = Fernet(key)
        # Déchiffrage de la donnée chiffrée avec la méthode decrypt de l'objet fernet et conversion en chaîne de caractères
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        
        # Retourne la donnée décryptée
        return decrypted_data


    @staticmethod
    def is_encrypted(data):
    
        """_summary_
        Vérification de la donnée
        Returns:
            _type_: _description_
        """
    
        try:
            # Si la donnée est encodée en base64 et si elle a une longueur attendue
            base64_bytes = base64.b64decode(data, validate=True)
            # Retourne la longueur
            return len(base64_bytes) > 0
        except Exception:
            return False
    