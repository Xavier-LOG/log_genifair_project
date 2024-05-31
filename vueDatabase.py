# Importation des fichiers




from controleurDatabase import controleurDatabase




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QGroupBox, QTableWidget, QLabel, QCheckBox, QLineEdit




# Définition de la classe vueDatabase




class vueDatabase(QWidget):

    
    # Constructeur par défaut

    
    def __init__(self):
        
        super().__init__()
        self.controleurdatabase = controleurDatabase(self)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes

    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueDatabase
        self.vuedatabase_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Database")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_connectiontableviewer = QGroupBox()
        self.groupbox_connectiontable_layout = QHBoxLayout()
        
        self.groupbox_connection = QGroupBox("Database Connection")
        self.groupbox_connection_layout = QVBoxLayout()
        
        self.groupbox_connection_host_lineedit = QLineEdit("IP Address")
        self.groupbox_connection_database_name_lineedit = QLineEdit("Database Name")
        self.groupbox_connection_username_lineedit = QLineEdit("Username")
        self.groupbox_connection_password_lineedit = QLineEdit()
        self.groupbox_connection_checkbox = QCheckBox("Show Password")
        self.groupbox_connection_button = QPushButton("Connect")
        
        # Configuration de l'affichage du texte en mode mot de passe
        self.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_host_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_database_name_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_username_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_password_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_checkbox)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_button)
        
        self.groupbox_connection.setLayout(self.groupbox_connection_layout)
        
        self.groupbox_table = QGroupBox("Table")
        self.groupbox_table_layout = QVBoxLayout()
        
        self.groupbox_table_label = QLabel("Select Table")
        self.groupbox_table_confirm_button = QPushButton("Confirm")
        
        self.groupbox_table.setEnabled(False)
        
        self.groupbox_table_layout.addWidget(self.groupbox_table_label)
        self.groupbox_table_layout.addWidget(self.groupbox_table_confirm_button)
        
        self.groupbox_table.setLayout(self.groupbox_table_layout)
        
        self.groupbox_connectiontable_layout.addWidget(self.groupbox_connection)
        self.groupbox_connectiontable_layout.addWidget(self.groupbox_table)
        
        self.groupbox_connectiontableviewer.setLayout(self.groupbox_connectiontable_layout)
        
        self.groupbox_button = QPushButton("Import Data")
        
        self.groupbox_button.setEnabled(False)
        
        self.groupbox_layout.addWidget(self.groupbox_connectiontableviewer)
        self.groupbox_layout.addWidget(self.groupbox_button)
        
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuedatabase_layout.addWidget(self.groupbox)

    
    def connect_signals(self):
        
        self.groupbox_connection_button.clicked.connect(self.controleurdatabase.connect)
        self.groupbox_connection_checkbox.stateChanged.connect(self.controleurdatabase.toggle_password_visibility)
        self.groupbox_table_confirm_button.clicked.connect(self.controleurdatabase.table_confirm)
        self.groupbox_button.clicked.connect(self.controleurdatabase.import_data)




# Programme principal




if __name__ == "__main__":
    
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    mainwindow.setCentralWidget(vueDatabase())
    mainwindow.show()
    sys.exit(app.exec())
