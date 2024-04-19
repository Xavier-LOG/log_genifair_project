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
        self.groupbox_textarea = QPlainTextEdit()
        self.controleurcatalogviewer = controleurCatalogviewer(self)
        self.init_ui()


    # Définition des méthodes
    
    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueCatalogviewer
        self.vuecatalogviewer_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Catalog Viewer")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_textarea.setReadOnly(True)
        
        self.groupbox_layout.addWidget(self.groupbox_textarea)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuecatalogviewer_layout.addWidget(self.groupbox)




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
