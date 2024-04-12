# Importation des fichiers




from vueDataframeviewer import vueDataframeviewer
from vueConversionsettings import vueConversionsettings
from vueNetcdfviewer import vueNetcdfviewer




# Importation des bibliothèques




from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox




# Définition de la classe vueConversion




class vueConversion(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuemainwindow = parent
        self.vuedataframeviewer = vueDataframeviewer(self)
        self.vueconversionsettings = vueConversionsettings(self)
        self.vuenetcdfviewer = vueNetcdfviewer(self)
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        # Layout associé à l'instance de la classe vueConversion
        self.vueconversion_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Conversion")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_layout.addWidget(self.vuedataframeviewer)
        self.groupbox_layout.addWidget(self.vueconversionsettings)
        self.groupbox_layout.addWidget(self.vuenetcdfviewer)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vueconversion_layout.addWidget(self.groupbox)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    mainwindow.setCentralWidget(vueConversion(vuemainwindow))
    mainwindow.show()
    sys.exit(app.exec())
