# Importation des fichiers




from controleurCatalogviewer import controleurCatalogviewer




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPlainTextEdit, QGroupBox
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtCore import Qt




# Définition de la classe vueCatalogviewer




class vueCatalogviewer(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuecatalog = parent
        self.groupbox_textarea = QPlainTextEdit()
        self.groupbox_searchbar = QLineEdit()
        # Définit un raccourci clavier qui se déclenchera par la séquence de touches Ctrl+F
        self.shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.controleurcatalogviewer = controleurCatalogviewer(self)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes
    
    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueCatalogviewer
        self.vuecatalogviewer_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Catalog Viewer")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_textarea.setReadOnly(True)
        self.groupbox_textarea.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.groupbox_textarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        
        self.groupbox_searchbar.setPlaceholderText("Search Keyword")
        self.groupbox_searchbar.setVisible(False)
        
        self.groupbox_layout.addWidget(self.groupbox_textarea)
        self.groupbox_layout.addWidget(self.groupbox_searchbar)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuecatalogviewer_layout.addWidget(self.groupbox)
    
    
    def connect_signals(self):
        
        self.groupbox_searchbar.returnPressed.connect(self.controleurcatalogviewer.find_keyword)
        self.shortcut.activated.connect(self.controleurcatalogviewer.toggle_searchbar)




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
