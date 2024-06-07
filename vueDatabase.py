# Importation des fichiers




from controleurDatabase import controleurDatabase




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QScrollArea, QGroupBox, QLabel, QCheckBox, QLineEdit




# Définition de la classe vueDatabase




class vueDatabase(QWidget):

    
    # Constructeur par défaut

    
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Database")
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
        self.groupbox_connectiontablecolumn_layout = QHBoxLayout()
        
        self.groupbox_connection = QGroupBox("Database Connection")
        self.groupbox_connection_layout = QVBoxLayout()
        
        self.groupbox_connection_host_checkbox = QCheckBox("Default Address")
        self.groupbox_connection_host_lineedit = QLineEdit()
        self.groupbox_connection_port_checkbox = QCheckBox("Default Port")
        self.groupbox_connection_port_lineedit = QLineEdit()
        self.groupbox_connection_database_name_lineedit = QLineEdit()
        self.groupbox_connection_username_lineedit = QLineEdit()
        self.groupbox_connection_password_lineedit = QLineEdit()
        self.groupbox_connection_checkbox = QCheckBox("Show Password")
        self.groupbox_connection_button = QPushButton("Connect")
        
        self.groupbox_connection_host_lineedit.setPlaceholderText("IP Address")
        self.groupbox_connection_port_lineedit.setPlaceholderText("Port")
        self.groupbox_connection_database_name_lineedit.setPlaceholderText("Database Name")
        self.groupbox_connection_username_lineedit.setPlaceholderText("Username")
        self.groupbox_connection_password_lineedit.setPlaceholderText("Password")
        self.groupbox_connection_host_checkbox.setChecked(True)
        self.groupbox_connection_host_lineedit.setVisible(False)
        self.groupbox_connection_port_checkbox.setChecked(True)
        self.groupbox_connection_port_lineedit.setVisible(False)
        # Configuration de l'affichage du texte en mode mot de passe
        self.groupbox_connection_password_lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_host_checkbox)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_host_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_port_checkbox)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_port_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_database_name_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_username_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_password_lineedit)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_checkbox)
        self.groupbox_connection_layout.addWidget(self.groupbox_connection_button)
        
        self.groupbox_connection.setLayout(self.groupbox_connection_layout)
        
        self.groupbox_table_scrollarea = QScrollArea()
        self.groupbox_table = QGroupBox("Table")
        self.groupbox_table_layout = QVBoxLayout()
        
        self.groupbox_table_label = QLabel("Select Table")
        self.groupbox_table_confirm_button = QPushButton("Confirm")
        
        self.groupbox_table.setEnabled(False)
        
        self.groupbox_table_layout.addWidget(self.groupbox_table_label)
        self.groupbox_table_layout.addWidget(self.groupbox_table_confirm_button)
        
        self.groupbox_table.setLayout(self.groupbox_table_layout)
        
        self.groupbox_table_scrollarea.setWidgetResizable(True)
        self.groupbox_table_scrollarea.setWidget(self.groupbox_table)
        
        self.groupbox_column_scrollarea = QScrollArea()
        self.groupbox_column = QGroupBox("Column")
        self.groupbox_column_layout = QVBoxLayout()
        
        self.groupbox_column_label = QLabel("Select Column")
        self.groupbox_column_button = QPushButton("Unselect All")
        self.groupbox_column_confirm_button = QPushButton("Confirm")
        
        self.groupbox_column.setEnabled(False)
        
        self.groupbox_column_layout.addWidget(self.groupbox_column_label)
        self.groupbox_column_layout.addWidget(self.groupbox_column_button)
        self.groupbox_column_layout.addWidget(self.groupbox_column_confirm_button)
        
        self.groupbox_column.setLayout(self.groupbox_column_layout)
        
        self.groupbox_column_scrollarea.setWidgetResizable(True)
        self.groupbox_column_scrollarea.setWidget(self.groupbox_column)
        
        self.groupbox_connectiontablecolumn_layout.addWidget(self.groupbox_connection)
        self.groupbox_connectiontablecolumn_layout.addWidget(self.groupbox_table_scrollarea)
        self.groupbox_connectiontablecolumn_layout.addWidget(self.groupbox_column_scrollarea)
        
        self.groupbox_connectiontableviewer.setLayout(self.groupbox_connectiontablecolumn_layout)
        
        self.groupbox_button = QPushButton("Import Data")
        
        self.groupbox_button.setEnabled(False)
        
        self.groupbox_layout.addWidget(self.groupbox_connectiontableviewer)
        self.groupbox_layout.addWidget(self.groupbox_button)
        
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuedatabase_layout.addWidget(self.groupbox)

    
    def connect_signals(self):
        
        self.groupbox_connection_host_checkbox.stateChanged.connect(self.controleurdatabase.toggle_host_visibility)
        self.groupbox_connection_port_checkbox.stateChanged.connect(self.controleurdatabase.toggle_port_visibility)
        self.groupbox_connection_button.clicked.connect(self.controleurdatabase.connect)
        self.groupbox_connection_checkbox.stateChanged.connect(self.controleurdatabase.toggle_password_visibility)
        self.groupbox_table_confirm_button.clicked.connect(self.controleurdatabase.table_confirm)
        self.groupbox_column_button.clicked.connect(self.controleurdatabase.unselect_all_columns)
        self.groupbox_column_confirm_button.clicked.connect(self.controleurdatabase.column_confirm)
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
