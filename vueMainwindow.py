# Importation des fichiers




from modeleMainwindow import modeleMainwindow
from vueToolbar import vueToolbar
from vueCatalog import vueCatalog




# Importation des bibliothèques




import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QGroupBox




# Définition de la classe vueMainwindow




class vueMainwindow(QMainWindow):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.modelemainwindow = modeleMainwindow()
        self.mainwindow_vuetoolbar = vueToolbar(self)
        self.mainwindow_vuecatalog = vueCatalog(self)
        self.init_ui()
        

    # Définition des méthodes


    def init_ui(self):
        
        self.setWindowTitle("Project")
        self.modelemainwindow.screen_width = QApplication.primaryScreen().availableGeometry().width()
        self.modelemainwindow.screen_height = QApplication.primaryScreen().availableGeometry().height()
        self.modelemainwindow.set_screen_resolution(int(QApplication.primaryScreen().availableGeometry().width()), int(QApplication.primaryScreen().availableGeometry().height() * 0.95))
        self.setMinimumSize(self.modelemainwindow.screen_width, self.modelemainwindow.screen_height)
        
        self.addToolBar(self.mainwindow_vuetoolbar)
        
        self.mainwindow_central_widget = QWidget()
        self.setCentralWidget(self.mainwindow_central_widget)
        
        self.mainwindow_layout = QHBoxLayout(self.mainwindow_central_widget)
        
        self.mainwindow_vuecatalog_tabwidget = QTabWidget()
        
        self.mainwindow_vuecatalog_tabwidget.addTab(self.mainwindow_vuecatalog, "Arrange Data")
        
        self.mainwindow_logs_groupbox = QGroupBox("Logs")
        self.mainwindow_logs_groupbox_layout = QVBoxLayout()
        self.mainwindow_logs_textarea = QPlainTextEdit()
        
        self.mainwindow_logs_groupbox.setMaximumWidth(int(self.modelemainwindow.screen_width * 0.25))
        self.mainwindow_logs_textarea.setReadOnly(True)
        
        self.mainwindow_logs_groupbox_layout.addWidget(self.mainwindow_logs_textarea)
        self.mainwindow_logs_groupbox.setLayout(self.mainwindow_logs_groupbox_layout)
        
        self.mainwindow_layout.addWidget(self.mainwindow_vuecatalog_tabwidget)
        self.mainwindow_layout.addWidget(self.mainwindow_logs_groupbox)




# Programme principal




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    vuemainwindow = vueMainwindow()
    vuemainwindow.show()
    sys.exit(app.exec())
    