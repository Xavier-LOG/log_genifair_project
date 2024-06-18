# Importation des fichiers




from modeleMainwindow import modeleMainwindow
from vueLogs import vueLogs
from vueFilesettings import vueFilesettings
from vueToolbar import vueToolbar
from vueCatalog import vueCatalog
from vueFileviewer import vueFileviewer
from vueConversion import vueConversion




# Importation des bibliothèques




import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QMdiSubWindow, QTabWidget, QVBoxLayout, QHBoxLayout




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
        self.vuefilesettings = vueFilesettings(self)
        self.vuetoolbar = vueToolbar(self)
        self.vuecatalog = vueCatalog(self)
        self.vuefileviewer = vueFileviewer(self)
        self.vueconversion = vueConversion(self)
        self.init_ui()
        

    # Définition des méthodes


    def init_ui(self):
        
        """_summary_
        Initialisation de la vue de la fenêtre principale
        """
        
        self.setWindowTitle("NetCDF LOG Wimereux Software")
        self.addToolBar(self.vuetoolbar)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.vuemainwindow_horizontal_layout = QHBoxLayout(self.central_widget)
        
        self.vuemainwindow_vertical_filesettingstabwidget_layout = QVBoxLayout()
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.vuecatalog, "Arrange Data")
        self.tabwidget.addTab(self.vueconversion, "Process Data")
        self.tabwidget.setTabEnabled(1, False)
        
        self.vuemainwindow_vertical_filesettingstabwidget_layout.addWidget(self.vuefilesettings)
        self.vuemainwindow_vertical_filesettingstabwidget_layout.addWidget(self.tabwidget)
        
        self.vuemainwindow_vertical_logsfileviewer_layout = QVBoxLayout()
        
        self.vuelogs.setMaximumWidth(int(self.modelemainwindow.screen_width * 0.25))
        self.vuefileviewer.setMaximumWidth(int(self.modelemainwindow.screen_width * 0.25))
        
        self.vuemainwindow_vertical_logsfileviewer_layout.addWidget(self.vuelogs)
        self.vuemainwindow_vertical_logsfileviewer_layout.addWidget(self.vuefileviewer)
        
        self.vuemainwindow_horizontal_layout.addLayout(self.vuemainwindow_vertical_filesettingstabwidget_layout)
        self.vuemainwindow_horizontal_layout.addLayout(self.vuemainwindow_vertical_logsfileviewer_layout)


    def closeEvent(self, event):
        
        """_summary_
        Gestion de la fermeture des sous-fenêtres lors de la fermeture de la fenêtre principale
        """
        
        # Fermeture des sous-fenêtres
        if isinstance(self.vuetoolbar.controleurtoolbar.vuedatabase, QWidget):
            if self.vuetoolbar.controleurtoolbar.vuedatabase.isVisible():
                self.vuetoolbar.controleurtoolbar.vuedatabase.close()
        if isinstance(self.vuetoolbar.controleurtoolbar.about_window, QMdiSubWindow):
            if self.vuetoolbar.controleurtoolbar.about_window.isVisible():
                self.vuetoolbar.controleurtoolbar.about_window.close()
                
        # Acceptation de l'évènement de fermeture de la fenêtre principale
        event.accept()




# Programme principal




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    vuemainwindow = vueMainwindow()
    vuemainwindow.show()
    sys.exit(app.exec())
    