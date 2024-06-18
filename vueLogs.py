# Importation des fichiers




from controleurLogs import controleurLogs




# Importation des bibliothèques




from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QVBoxLayout, QGroupBox




# Définition de la classe vueLogs




class vueLogs(QWidget):
    
    
    # Constructeur par défaut

    
    def __init__(self, parent):
        
        super().__init__(parent)        
        self.vuemainwindow = parent
        self.controleurlogs = controleurLogs(self)
        self.init_ui()
    
    
    # Définition des méthodes


    def init_ui(self):
        
        """_summary_
        Initialisation de la vue
        """
        
        # Layout associé à l'instance de la classe vueLogs
        self.vuelogs_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Logs")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_textarea = QPlainTextEdit()
        
        self.groupbox_textarea.setReadOnly(True)
        
        self.groupbox_layout.addWidget(self.groupbox_textarea)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuelogs_layout.addWidget(self.groupbox)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    mainwindow.setCentralWidget(vueLogs(vuemainwindow))
    mainwindow.show()
    sys.exit(app.exec())
