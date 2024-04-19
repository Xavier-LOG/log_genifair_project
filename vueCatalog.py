# Importation des fichiers




from modeleCatalog import modeleCatalog
from vueCatalogtype import vueCatalogtype
from vueCatalogviewer import vueCatalogviewer
from vueCatalogsettings import vueCatalogsettings
from controleurCatalog import controleurCatalog




# Importation des bibliothèques




from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QGroupBox




# Définition de la classe vueCatalog




class vueCatalog(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuemainwindow = parent
        self.modelecatalog = modeleCatalog()
        self.vuecatalogtype = vueCatalogtype(self)
        self.vuecatalogviewer = vueCatalogviewer(self)
        self.vuecatalogsettings = vueCatalogsettings(self)
        self.controleurcatalog = controleurCatalog(self)
        self.vuecatalogviewer.setEnabled(False)
        self.vuecatalogsettings.setEnabled(False)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes
    
    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueCatalog
        self.vuecatalog_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Catalog")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_viewersettings_layout = QHBoxLayout()

        self.groupbox_viewersettings_layout.addWidget(self.vuecatalogviewer)
        self.groupbox_viewersettings_layout.addWidget(self.vuecatalogsettings)

        self.groupbox_save_button = QPushButton("Save Catalog")
        self.groupbox_confirm_button = QPushButton("Confirm Catalog")
        
        self.groupbox_save_button.setEnabled(False)
        self.groupbox_confirm_button.setEnabled(False)

        self.groupbox_layout.addWidget(self.vuecatalogtype)
        self.groupbox_layout.addLayout(self.groupbox_viewersettings_layout)
        self.groupbox_layout.addWidget(self.groupbox_save_button)
        self.groupbox_layout.addWidget(self.groupbox_confirm_button)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuecatalog_layout.addWidget(self.groupbox)
    
    
    def connect_signals(self):
        
        self.groupbox_save_button.clicked.connect(self.controleurcatalog.save)
        self.groupbox_confirm_button.clicked.connect(self.controleurcatalog.confirm)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    mainwindow.setCentralWidget(vueCatalog(vuemainwindow))
    mainwindow.show()
    sys.exit(app.exec())
