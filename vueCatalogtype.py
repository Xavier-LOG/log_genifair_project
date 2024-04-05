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
        
        self.vuecatalogtype_groupbox = QGroupBox("Catalog Type")
        self.vuecatalogtype_groupbox_layout = QVBoxLayout()
        
        self.vuecatalogtype_groupbox_checkbox_layout = QHBoxLayout()
        self.vuecatalogtype_groupbox_trajectory_catalog_checkbox = QCheckBox("Trajectory Catalog")
        self.vuecatalogtype_groupbox_time_series_catalog_checkbox = QCheckBox("Time Series Catalog")
        self.vuecatalogtype_groupbox_profil_catalog_checkbox = QCheckBox("Profil Catalog")
        
        self.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(True)
        
        self.vuecatalogtype_groupbox_checkbox_layout.addWidget(self.vuecatalogtype_groupbox_trajectory_catalog_checkbox)
        self.vuecatalogtype_groupbox_checkbox_layout.addWidget(self.vuecatalogtype_groupbox_time_series_catalog_checkbox)
        self.vuecatalogtype_groupbox_checkbox_layout.addWidget(self.vuecatalogtype_groupbox_profil_catalog_checkbox)
        
        self.vuecatalogtype_groupbox_button_layout = QHBoxLayout()
        self.vuecatalogtype_groupbox_confirm_button = QPushButton("Confirm")
        self.vuecatalogtype_groupbox_cancel_button = QPushButton("Cancel")
        
        self.vuecatalogtype_groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
        
        self.vuecatalogtype_groupbox_button_layout.addWidget(self.vuecatalogtype_groupbox_confirm_button)
        self.vuecatalogtype_groupbox_button_layout.addWidget(self.vuecatalogtype_groupbox_cancel_button)
        
        self.vuecatalogtype_groupbox_catalog_restore_layout = QHBoxLayout()
        self.vuecatalogtype_groupbox_catalog_restore_button = QPushButton("Restore")
        
        self.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
        
        self.vuecatalogtype_groupbox_catalog_restore_layout.addWidget(self.vuecatalogtype_groupbox_catalog_restore_button)
        
        self.vuecatalogtype_groupbox_layout.addLayout(self.vuecatalogtype_groupbox_checkbox_layout)
        self.vuecatalogtype_groupbox_layout.addLayout(self.vuecatalogtype_groupbox_button_layout)
        self.vuecatalogtype_groupbox_layout.addLayout(self.vuecatalogtype_groupbox_catalog_restore_layout)
        self.vuecatalogtype_groupbox.setLayout(self.vuecatalogtype_groupbox_layout)
        
        self.vuecatalogtype_layout.addWidget(self.vuecatalogtype_groupbox)
    
    
    def connect_signals(self):
        
        self.vuecatalogtype_groupbox_trajectory_catalog_checkbox.toggled.connect(self.controleurcatalogtype.trajectory_catalog)
        self.vuecatalogtype_groupbox_time_series_catalog_checkbox.toggled.connect(self.controleurcatalogtype.timeseries_catalog)
        self.vuecatalogtype_groupbox_profil_catalog_checkbox.toggled.connect(self.controleurcatalogtype.profil_catalog)
        self.vuecatalogtype_groupbox_confirm_button.clicked.connect(self.controleurcatalogtype.confirm)
        self.vuecatalogtype_groupbox_cancel_button.clicked.connect(self.controleurcatalogtype.cancel)
        self.vuecatalogtype_groupbox_catalog_restore_button.clicked.connect(self.controleurcatalogtype.restore)




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
