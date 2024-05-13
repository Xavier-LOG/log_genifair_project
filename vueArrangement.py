# Importation des fichiers




from modeleArrangement import modeleArrangement
from vueArrangementtype import vueArrangementtype
from vueArrangementviewer import vueArrangementviewer
from vueArrangementsettings import vueArrangementsettings
from controleurArrangement import controleurArrangement




# Importation des bibliothèques




from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QGroupBox




# Définition de la classe vueArrangement




class vueArrangement(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuemainwindow = parent
        self.modelearrangement = modeleArrangement()
        self.vuearrangementtype = vueArrangementtype(self)
        self.vuearrangementviewer = vueArrangementviewer(self)
        self.vuearrangementsettings = vueArrangementsettings(self)
        self.controleurarrangement = controleurArrangement(self)
        self.vuearrangementviewer.setEnabled(False)
        self.vuearrangementsettings.setEnabled(False)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes
    
    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueArrangement
        self.vuearrangement_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Catalog")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_viewersettings_layout = QHBoxLayout()

        self.groupbox_viewersettings_layout.addWidget(self.vuearrangementviewer)
        self.groupbox_viewersettings_layout.addWidget(self.vuearrangementsettings)

        self.groupbox_save_button = QPushButton("Save Catalog")
        self.groupbox_confirm_button = QPushButton("Confirm Catalog")
        
        self.groupbox_save_button.setEnabled(False)
        self.groupbox_confirm_button.setEnabled(False)

        self.groupbox_layout.addWidget(self.vuearrangementtype)
        self.groupbox_layout.addLayout(self.groupbox_viewersettings_layout)
        self.groupbox_layout.addWidget(self.groupbox_save_button)
        self.groupbox_layout.addWidget(self.groupbox_confirm_button)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuearrangement_layout.addWidget(self.groupbox)
    
    
    def connect_signals(self):
        
        self.groupbox_save_button.clicked.connect(self.controleurarrangement.save)
        self.groupbox_confirm_button.clicked.connect(self.controleurarrangement.confirm)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    mainwindow.setCentralWidget(vueArrangement(vuemainwindow))
    mainwindow.show()
    sys.exit(app.exec())
