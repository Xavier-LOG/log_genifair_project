# Importation des fichiers




from controleurFileviewer import controleurFileviewer




# Importation des bibliothèques




from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QVBoxLayout, QGroupBox




# Définition de la classe vueFileviewer




class vueFileviewer(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuemainwindow = parent
        self.controleurfileviewer = controleurFileviewer(self)
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        # Layout associé à l'instance de la classe vueFileviewer
        self.vuefileviewer_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("File Viewer")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_textarea = QPlainTextEdit()
        
        self.groupbox_textarea.setReadOnly(True)
        
        self.groupbox_layout.addWidget(self.groupbox_textarea)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuefileviewer_layout.addWidget(self.groupbox)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    mainwindow.setCentralWidget(vueFileviewer(vuemainwindow))
    mainwindow.show()
    sys.exit(app.exec())
