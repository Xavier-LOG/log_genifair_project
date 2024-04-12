# Importation des fichiers




from controleurToolbar import controleurToolbar




# Importations des bibliothèques




import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QMenu




# Définition de la classe vueToolbar




class vueToolbar(QToolBar):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuemainwindow = parent
        self.init_ui()
        self.connect_signals()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.controleurtoolbar = controleurToolbar(self)
        self.menu_file = QMenu("")
        self.menu_file.setTitle("File")
        # Ajout d'une action dans le menu contextuel de File
        self.action_file = self.menu_file.addAction("Import File")
        self.menu_file_button = QPushButton("File")
        self.menu_file_button.setMenu(self.menu_file)
        self.addWidget(self.menu_file_button)
        
        self.menu_options = QMenu("")
        self.menu_options.setTitle("Options")
        # Ajout d'une action dans le menu contextuel de Options
        self.action_options = self.menu_options.addAction("Change Resolution")
        self.menu_options_button = QPushButton("Options")
        self.menu_options_button.setMenu(self.menu_options)
        self.addWidget(self.menu_options_button)
        
        self.menu_help = QMenu("")
        self.menu_help.setTitle("?")
        # Ajout d'une action dans le menu contextuel de Help
        self.action_help = self.menu_help.addAction("About")
        self.menu_help_button = QPushButton("?")
        self.menu_help_button.setMenu(self.menu_help)
        self.addWidget(self.menu_help_button)
        
        self.menu_file.setEnabled(False)
        
    
    def connect_signals(self):
        
        self.menu_file_button.clicked.connect(self.controleurtoolbar.file_clicked)
        self.menu_options_button.clicked.connect(self.controleurtoolbar.options_clicked)
        self.menu_help_button.clicked.connect(self.controleurtoolbar.help_clicked)
        self.action_file.triggered.connect(self.controleurtoolbar.import_option)
        self.action_options.triggered.connect(self.controleurtoolbar.resolution_option)
        self.action_help.triggered.connect(self.controleurtoolbar.about_option)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vuetoolbar = vueToolbar(vuemainwindow)
    controleurtoolbar = controleurToolbar(vuetoolbar)
    mainwindow.addToolBar(vuetoolbar)
    mainwindow.show()
    sys.exit(app.exec())
