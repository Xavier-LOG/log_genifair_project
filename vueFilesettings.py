# Importation des fichiers




from controleurFilesettings import controleurFilesettings




# Importation des bibliothèques




from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QSlider, QGroupBox
from PyQt6.QtCore import Qt




# Définition de la classe vueFilesettings




class vueFilesettings(QWidget):

    
    # Constructeur par défaut

    
    def __init__(self, parent):
        
        super().__init__(parent)        
        self.vuemainwindow = parent
        self.controleurfilesettings = controleurFilesettings(self)
        self.init_ui()
        self.connect_signals()


    # Définition des méthodes

    
    def init_ui(self):

        # Layout associé à l'instance de la classe vueFilesettings
        self.vuefilesettings_layout = QVBoxLayout(self)
        
        self.groupbox = QGroupBox("File Settings")
        self.groupbox_layout = QVBoxLayout()
        self.groupbox_label_layout = QHBoxLayout()
        self.groupbox_button_layout = QHBoxLayout()
        
        self.groupbox_slider = QSlider(Qt.Orientation.Horizontal)
        self.groupbox_slider_label_value1 = QLabel("100")
        self.groupbox_slider_label_value2 = QLabel("1000")
        self.groupbox_slider_label_value3 = QLabel("10000")
        self.groupbox_slider_label_value4 = QLabel("UNLIMITED")
        self.groupbox_confirm_button = QPushButton("Confirm")
        self.groupbox_cancel_button = QPushButton("Cancel")
        
        self.groupbox_slider.setMinimum(0)
        self.groupbox_slider.setMaximum(3)
        self.groupbox_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.groupbox_slider.setTickInterval(1)
        self.groupbox_slider.setSingleStep(1)
        
        self.groupbox_slider.setEnabled(True)
        self.groupbox_confirm_button.setEnabled(True)
        self.groupbox_cancel_button.setEnabled(False)
        
        self.groupbox_label_layout.addWidget(self.groupbox_slider_label_value1)
        self.groupbox_label_layout.addStretch(1)
        self.groupbox_label_layout.addWidget(self.groupbox_slider_label_value2)
        self.groupbox_label_layout.addStretch(1)
        self.groupbox_label_layout.addWidget(self.groupbox_slider_label_value3)
        self.groupbox_label_layout.addStretch(1)
        self.groupbox_label_layout.addWidget(self.groupbox_slider_label_value4)
        
        self.groupbox_button_layout.addWidget(self.groupbox_confirm_button)
        self.groupbox_button_layout.addWidget(self.groupbox_cancel_button)
        
        self.groupbox_layout.addWidget(self.groupbox_slider)
        self.groupbox_layout.addLayout(self.groupbox_label_layout)
        self.groupbox_layout.addLayout(self.groupbox_button_layout)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuefilesettings_layout.addWidget(self.groupbox)

    
    def connect_signals(self):
        
        self.groupbox_confirm_button.clicked.connect(self.controleurfilesettings.confirm)
        self.groupbox_cancel_button.clicked.connect(self.controleurfilesettings.cancel)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    from vueFilesettings import vueFilesettings
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vuefilesettings = vueFilesettings(vuemainwindow)
    mainwindow.setCentralWidget(vueFilesettings(vuefilesettings))
    mainwindow.show()
    sys.exit(app.exec())
