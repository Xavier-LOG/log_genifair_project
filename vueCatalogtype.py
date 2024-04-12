# Importation des fichiers




from controleurCatalogtype import controleurCatalogtype




# Importation des bibliothèques




from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QCheckBox, QGroupBox




# Définition de la classe vueCatalogtype




class vueCatalogtype(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuecatalog = parent
        self.controleurcatalogtype = controleurCatalogtype(self)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes
    
    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueCatalogtype
        self.vuecatalogtype_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Catalog Type")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_checkbox_layout = QHBoxLayout()
        self.groupbox_trajectory_catalog_checkbox = QCheckBox("Trajectory Catalog")
        self.groupbox_time_series_catalog_checkbox = QCheckBox("Time Series Catalog")
        self.groupbox_profil_catalog_checkbox = QCheckBox("Profil Catalog")
        self.groupbox_sampling_catalog_checkbox = QCheckBox("Sampling Catalog")
        
        self.groupbox_trajectory_catalog_checkbox.setEnabled(True)
        self.groupbox_time_series_catalog_checkbox.setEnabled(True)
        self.groupbox_profil_catalog_checkbox.setEnabled(True)
        self.groupbox_sampling_catalog_checkbox.setEnabled(True)
        
        self.groupbox_checkbox_layout.addWidget(self.groupbox_trajectory_catalog_checkbox)
        self.groupbox_checkbox_layout.addWidget(self.groupbox_time_series_catalog_checkbox)
        self.groupbox_checkbox_layout.addWidget(self.groupbox_profil_catalog_checkbox)
        self.groupbox_checkbox_layout.addWidget(self.groupbox_sampling_catalog_checkbox)
        
        self.groupbox_button_layout = QHBoxLayout()
        self.groupbox_confirm_button = QPushButton("Confirm")
        self.groupbox_cancel_button = QPushButton("Cancel")
        
        self.groupbox_confirm_button.setEnabled(False)
        self.groupbox_cancel_button.setEnabled(False)
        
        self.groupbox_button_layout.addWidget(self.groupbox_confirm_button)
        self.groupbox_button_layout.addWidget(self.groupbox_cancel_button)
        
        self.groupbox_open_layout = QHBoxLayout()
        self.groupbox_restore_button = QPushButton("Restore")
        self.groupbox_open_button = QPushButton("Open")
        
        self.groupbox_restore_button.setEnabled(False)
        self.groupbox_open_button.setEnabled(False)
        
        self.groupbox_open_layout.addWidget(self.groupbox_restore_button)
        self.groupbox_open_layout.addWidget(self.groupbox_open_button)
        
        self.groupbox_layout.addLayout(self.groupbox_checkbox_layout)
        self.groupbox_layout.addLayout(self.groupbox_button_layout)
        self.groupbox_layout.addLayout(self.groupbox_open_layout)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuecatalogtype_layout.addWidget(self.groupbox)
    
    
    def connect_signals(self):
        
        self.groupbox_trajectory_catalog_checkbox.toggled.connect(self.controleurcatalogtype.trajectory_catalog)
        self.groupbox_time_series_catalog_checkbox.toggled.connect(self.controleurcatalogtype.timeseries_catalog)
        self.groupbox_profil_catalog_checkbox.toggled.connect(self.controleurcatalogtype.profil_catalog)
        self.groupbox_sampling_catalog_checkbox.toggled.connect(self.controleurcatalogtype.sampling_catalog)
        self.groupbox_confirm_button.clicked.connect(self.controleurcatalogtype.confirm)
        self.groupbox_cancel_button.clicked.connect(self.controleurcatalogtype.cancel)
        self.groupbox_restore_button.clicked.connect(self.controleurcatalogtype.restore)
        self.groupbox_open_button.clicked.connect(self.controleurcatalogtype.open)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    from vueCatalog import vueCatalog
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vuecatalog = vueCatalog(vuemainwindow)
    mainwindow.setCentralWidget(vueCatalogtype(vuecatalog))
    mainwindow.show()
    sys.exit(app.exec())
