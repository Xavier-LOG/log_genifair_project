# Importation des fichiers




from controleurArrangementtype import controleurArrangementtype




# Importation des bibliothèques




from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QCheckBox, QGroupBox




# Définition de la classe vueArrangementtype




class vueArrangementtype(QWidget):

    
    # Constructeur par défaut

    
    def __init__(self, parent):
        
        super().__init__(parent)        
        self.vuearrangement = parent
        self.controleurarrangementtype = controleurArrangementtype(self)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes

    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueArrangementtype
        self.vuearrangementtype_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("Arrangement Type")
        self.groupbox_layout = QVBoxLayout()
        
        self.groupbox_checkbox_layout = QHBoxLayout()
        self.groupbox_trajectory_arrangement_checkbox = QCheckBox("Trajectory Arrangement")
        self.groupbox_time_series_arrangement_checkbox = QCheckBox("Time Series Arrangement")
        self.groupbox_profile_arrangement_checkbox = QCheckBox("Profile Arrangement")
        self.groupbox_sample_arrangement_checkbox = QCheckBox("Sample Arrangement")
        
        self.groupbox_trajectory_arrangement_checkbox.setEnabled(True)
        self.groupbox_time_series_arrangement_checkbox.setEnabled(True)
        self.groupbox_profile_arrangement_checkbox.setEnabled(True)
        self.groupbox_sample_arrangement_checkbox.setEnabled(True)
        
        self.groupbox_checkbox_layout.addWidget(self.groupbox_trajectory_arrangement_checkbox)
        self.groupbox_checkbox_layout.addWidget(self.groupbox_time_series_arrangement_checkbox)
        self.groupbox_checkbox_layout.addWidget(self.groupbox_profile_arrangement_checkbox)
        self.groupbox_checkbox_layout.addWidget(self.groupbox_sample_arrangement_checkbox)
        
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
        
        self.vuearrangementtype_layout.addWidget(self.groupbox)

    
    def connect_signals(self):
        
        self.groupbox_trajectory_arrangement_checkbox.toggled.connect(self.controleurarrangementtype.trajectory_arrangement)
        self.groupbox_time_series_arrangement_checkbox.toggled.connect(self.controleurarrangementtype.timeseries_arrangement)
        self.groupbox_profile_arrangement_checkbox.toggled.connect(self.controleurarrangementtype.profile_arrangement)
        self.groupbox_sample_arrangement_checkbox.toggled.connect(self.controleurarrangementtype.sample_arrangement)
        self.groupbox_confirm_button.clicked.connect(self.controleurarrangementtype.confirm)
        self.groupbox_cancel_button.clicked.connect(self.controleurarrangementtype.cancel)
        self.groupbox_restore_button.clicked.connect(self.controleurarrangementtype.restore)
        self.groupbox_open_button.clicked.connect(self.controleurarrangementtype.open)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    from vueArrangement import vueArrangement
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vuearrangement = vueArrangement(vuemainwindow)
    mainwindow.setCentralWidget(vueArrangementtype(vuearrangement))
    mainwindow.show()
    sys.exit(app.exec())
