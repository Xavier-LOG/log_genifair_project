# Importation des fichiers




from controleurToolbar import controleurToolbar




# Importations des bibliothèques




import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QMenu
from PyQt6.QtCore import pyqtSignal




# Définition




class vueToolbar(QToolBar):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.mainwindow = parent
        self.init_ui()
        self.connect_signals()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.controleurToolbar = controleurToolbar(self)
        self.vuetoolbar_file = QMenu("")
        self.vuetoolbar_file.setTitle("File")
        # Ajout d'une action dans le menu contextuel de File
        self.action_file = self.vuetoolbar_file.addAction("Import File")
        self.vuetoolbar_file_button = QPushButton("File")
        self.vuetoolbar_file_button.setMenu(self.vuetoolbar_file)
        self.addWidget(self.vuetoolbar_file_button)
        
        self.vuetoolbar_options = QMenu("")
        self.vuetoolbar_options.setTitle("Options")
        # Ajout d'une action dans le menu contextuel de Options
        self.action_options = self.vuetoolbar_options.addAction("Change Resolution")
        self.vuetoolbar_options_button = QPushButton("Options")
        self.vuetoolbar_options_button.setMenu(self.vuetoolbar_options)
        self.addWidget(self.vuetoolbar_options_button)
        
        self.vuetoolbar_help = QMenu("")
        self.vuetoolbar_help.setTitle("?")
        # Ajout d'une action dans le menu contextuel de Help
        self.action_help = self.vuetoolbar_help.addAction("About")
        self.vuetoolbar_help_button = QPushButton("?")
        self.vuetoolbar_help_button.setMenu(self.vuetoolbar_help)
        self.addWidget(self.vuetoolbar_help_button)
        
    
    def connect_signals(self):
        
        self.vuetoolbar_file_button.clicked.connect(self.controleurToolbar.file_clicked)
        self.vuetoolbar_options_button.clicked.connect(self.controleurToolbar.options_clicked)
        self.vuetoolbar_help_button.clicked.connect(self.controleurToolbar.help_clicked)
        self.action_file.triggered.connect(self.controleurToolbar.import_option)
        self.action_options.triggered.connect(self.controleurToolbar.resolution_option)
        self.action_help.triggered.connect(self.controleurToolbar.about_option)




# Programme principal




if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuetoolbar = vueToolbar(mainwindow)
    controleurtoolbar = controleurToolbar(vuetoolbar)
    mainwindow.addToolBar(vuetoolbar)
    mainwindow.show()
    sys.exit(app.exec())
