# Importation des fichiers




from modeleMainwindow import modeleMainwindow
from vueToolbar import vueToolbar
from vueArrangement import vueArrangement
from vueLogs import vueLogs
from vueFileviewer import vueFileviewer
from vueConversion import vueConversion




# Importation des bibliothèques




import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout




# Définition de la classe vueMainwindow




class vueMainwindow(QMainWindow):
    
    
    # Constructeur par défaut

    
    def __init__(self):
        
        super().__init__()        
        self.modelemainwindow = modeleMainwindow()
        self.modelemainwindow.screen_width = QApplication.primaryScreen().availableGeometry().width()
        self.modelemainwindow.screen_height = QApplication.primaryScreen().availableGeometry().height()
        self.modelemainwindow.set_screen_resolution(int(QApplication.primaryScreen().availableGeometry().width()), int(QApplication.primaryScreen().availableGeometry().height() * 0.95))
        self.setMinimumSize(self.modelemainwindow.screen_width, self.modelemainwindow.screen_height)
        self.vuelogs = vueLogs(self)
        self.vuetoolbar = vueToolbar(self)
        self.vueArrangement = vueArrangement(self)
        self.vuefileviewer = vueFileviewer(self)
        self.vueconversion = vueConversion(self)
        self.init_ui()
        

    # Définition des méthodes


    def init_ui(self):
        
        self.setWindowTitle("Project")
        self.addToolBar(self.vuetoolbar)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.vuemainwindow_horizontal_layout = QHBoxLayout(self.central_widget)
        
        self.vuemainwindow_vertical_tabwidget_layout = QVBoxLayout()
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.vueArrangement, "Arrange Data")
        self.tabwidget.addTab(self.vueconversion, "Process Data")
        self.tabwidget.setTabEnabled(1, False)
        
        self.vuemainwindow_vertical_tabwidget_layout.addWidget(self.tabwidget)
        
        self.vuemainwindow_vertical_logsfileviewer_layout = QVBoxLayout()
        
        self.vuelogs.setMaximumWidth(int(self.modelemainwindow.screen_width * 0.25))
        self.vuefileviewer.setMaximumWidth(int(self.modelemainwindow.screen_width * 0.25))
        
        self.vuemainwindow_vertical_logsfileviewer_layout.addWidget(self.vuelogs)
        self.vuemainwindow_vertical_logsfileviewer_layout.addWidget(self.vuefileviewer)
        
        self.vuemainwindow_horizontal_layout.addLayout(self.vuemainwindow_vertical_tabwidget_layout)
        self.vuemainwindow_horizontal_layout.addLayout(self.vuemainwindow_vertical_logsfileviewer_layout)




# Programme principal




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    vuemainwindow = vueMainwindow()
    vuemainwindow.show()
    sys.exit(app.exec())
    