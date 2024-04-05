# Importation des fichiers




from controleurCatalogviewer import controleurCatalogviewer




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPlainTextEdit, QGroupBox




# Définition de la classe vueCatalogviewer




class vueCatalogviewer(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuecatalog = parent
        self.controleurcatalogviewer = controleurCatalogviewer(self)
        self.init_ui()


    # Définition des méthodes
    
    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueCatalogviewer
        self.vuecatalogviewer_layout = QVBoxLayout(self)
        
        self.vuecatalogviewer_groupbox = QGroupBox("Catalog Viewer")
        self.vuecatalogviewer_groupbox_layout = QVBoxLayout()
        self.vuecatalogviewer_textarea = QPlainTextEdit()
        
        self.vuecatalogviewer_textarea.setReadOnly(True)
        
        self.vuecatalogviewer_groupbox_layout.addWidget(self.vuecatalogviewer_textarea)
        self.vuecatalogviewer_groupbox.setLayout(self.vuecatalogviewer_groupbox_layout)
        
        self.vuecatalogviewer_layout.addWidget(self.vuecatalogviewer_groupbox)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    from vueCatalog import vueCatalog
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vuecatalog = vueCatalog(vuemainwindow)
    mainwindow.setCentralWidget(vueCatalogviewer(vuecatalog))
    mainwindow.show()
    sys.exit(app.exec())
