# Importation des fichiers




from controleurNetcdfviewer import controleurNetcdfviewer




# Importation des bibliothèques




from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QVBoxLayout, QGroupBox




# Définition de la classe vueNetcdfviewer




class vueNetcdfviewer(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vueconversion = parent
        self.controleurnetcdfviewer = controleurNetcdfviewer(self)
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        """_summary_
        Initialisation de la vue
        """
        
        # Layout associé à l'instance de la classe vueNetcdfviewer
        self.vuenetcdfviewer_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("NetCDF Viewer")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_textarea = QPlainTextEdit()
        
        self.groupbox_textarea.setReadOnly(True)
        
        self.groupbox_layout.addWidget(self.groupbox_textarea)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuenetcdfviewer_layout.addWidget(self.groupbox)




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
    mainwindow.setCentralWidget(vueNetcdfviewer(vueconversion))
    mainwindow.show()
    sys.exit(app.exec())
