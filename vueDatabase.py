# Importation des fichiers




from controleurDatabase import controleurDatabase




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLineEdit




# Définition de la classe vueDatabase




class vueDatabase(QWidget):

    
    # Constructeur par défaut

    
    def __init__(self):
        
        super().__init__()
        self.host_lineedit = QLineEdit()
        self.database_name_lineedit = QLineEdit()
        self.username_lineedit = QLineEdit()
        self.password_lineedit = QLineEdit()
        self.controleurdatabase = controleurDatabase(self)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes

    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueDatabase
        self.vuedatabase_layout = QVBoxLayout(self)
        
        self.connexion_button = QPushButton("Connect")
        
        self.vuedatabase_layout.addWidget(self.host_lineedit)
        self.vuedatabase_layout.addWidget(self.database_name_lineedit)
        self.vuedatabase_layout.addWidget(self.username_lineedit)
        self.vuedatabase_layout.addWidget(self.password_lineedit)
        self.vuedatabase_layout.addWidget(self.connexion_button)

    
    def connect_signals(self):
        
        self.connexion_button.clicked.connect(self.controleurdatabase.connect)




# Programme principal




if __name__ == "__main__":
    
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    mainwindow.setCentralWidget(vueDatabase())
    mainwindow.show()
    sys.exit(app.exec())
