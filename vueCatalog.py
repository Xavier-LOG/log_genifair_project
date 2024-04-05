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
        self.mainwindow = parent
        self.modelecatalog = modeleCatalog()
        # vueCatalogviewer doit être initialisé avant vueCatalogtype pour pouvoir charger le type de catalogue
        self.vuecatalogviewer = vueCatalogviewer(self)
        self.vuecatalogtype = vueCatalogtype(self)
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
        
        self.vuecatalog_groupbox = QGroupBox("Catalog")
        self.vuecatalog_groupbox_layout = QVBoxLayout()
        
        self.vuecatalog_groupbox_viewersettings_layout = QHBoxLayout()

        self.vuecatalog_groupbox_viewersettings_layout.addWidget(self.vuecatalogviewer)
        self.vuecatalog_groupbox_viewersettings_layout.addWidget(self.vuecatalogsettings)

        self.vuecatalog_save_button = QPushButton("Save Catalog")
        self.vuecatalog_confirm_button = QPushButton("Confirm Catalog")
        
        self.vuecatalog_save_button.setEnabled(False)
        self.vuecatalog_confirm_button.setEnabled(False)

        self.vuecatalog_groupbox_layout.addWidget(self.vuecatalogtype)
        self.vuecatalog_groupbox_layout.addLayout(self.vuecatalog_groupbox_viewersettings_layout)
        self.vuecatalog_groupbox_layout.addWidget(self.vuecatalog_save_button)
        self.vuecatalog_groupbox_layout.addWidget(self.vuecatalog_confirm_button)
        self.vuecatalog_groupbox.setLayout(self.vuecatalog_groupbox_layout)
        
        self.vuecatalog_layout.addWidget(self.vuecatalog_groupbox)
    
    
    def connect_signals(self):
        
        self.vuecatalog_save_button.clicked.connect(self.controleurcatalog.save)




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
