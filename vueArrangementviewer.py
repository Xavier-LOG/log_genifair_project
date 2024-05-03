# Importation des fichiers




from controleurArrangementviewer import controleurArrangementviewer




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPlainTextEdit, QGroupBox




# Définition de la classe vueArrangementviewer




class vueArrangementviewer(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuearrangement = parent
        self.groupbox_textarea = QPlainTextEdit()
        self.controleurarrangementviewer = controleurArrangementviewer(self)
        self.init_ui()


    # Définition des méthodes
    
    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueArrangementviewer
        self.vuearrangementviewer_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Arrangement Viewer")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_textarea.setReadOnly(True)
        
        self.groupbox_layout.addWidget(self.groupbox_textarea)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuearrangementviewer_layout.addWidget(self.groupbox)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    from vueArrangement import vueArrangement
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vuearrangement = vueArrangement(vuemainwindow)
    mainwindow.setCentralWidget(vueArrangementviewer(vuearrangement))
    mainwindow.show()
    sys.exit(app.exec())
