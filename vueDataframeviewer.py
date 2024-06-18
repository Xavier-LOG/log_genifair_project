# Importation des fichiers




from controleurDataframeviewer import controleurDataframeviewer




# Importation des bibliothèques




from PyQt6.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QGroupBox




# Définition de la classe vueDataframeviewer




class vueDataframeviewer(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vueconversion = parent
        self.controleurdataframeviewer = controleurDataframeviewer(self)
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        """_summary_
        Initialisation de la vue
        """
        
        # Layout associé à l'instance de la classe vueDataframeviewer
        self.vuedataframeviewer_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Dataframe Viewer")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_tablewidget = QTableWidget()
        
        # Désactivation de l'édition pour tout le tablewidget
        self.groupbox_tablewidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.groupbox_tablewidget.setRowCount(20)
        self.groupbox_tablewidget.setColumnCount(20)
        
        self.groupbox_layout.addWidget(self.groupbox_tablewidget)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuedataframeviewer_layout.addWidget(self.groupbox)




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
    mainwindow.setCentralWidget(vueDataframeviewer(vueconversion))
    mainwindow.show()
    sys.exit(app.exec())
