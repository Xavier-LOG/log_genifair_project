# Importation des fichiers




from controleurConversionsettings import controleurConversionsettings




# Importation des bibliothèques




from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox




# Définition de la classe vueConversionsettings




class vueConversionsettings(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vueconversion = parent
        self.controleurconversionsettings = controleurConversionsettings(self)
        self.init_ui()
        self.connect_signals()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        """_summary_
        Initialisation de la vue
        """
        
        # Layout associé à l'instance de la classe vueConversionsettings
        self.vueconversionsettings_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Conversion Settings")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_convert_button = QPushButton("Convert to NetCDF")
        
        self.groupbox_layout.addWidget(self.groupbox_convert_button)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vueconversionsettings_layout.addWidget(self.groupbox)
    
    
    def connect_signals(self):
        
        """_summary_
        Connexion des signaux
        """
        
        self.groupbox_convert_button.clicked.connect(self.controleurconversionsettings.convert)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    from vueConversion import vueConversion
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vueconversion = vueConversion(vuemainwindow)
    mainwindow.setCentralWidget(vueConversionsettings(vueconversion))
    mainwindow.show()
    sys.exit(app.exec())
