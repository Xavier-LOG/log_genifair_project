# Importation des fichiers




from vueToolbar import vueToolbar
from vueNetcdf import vueNetCDF
from modeleMainwindow import modeleMainwindow




# Importation des bibliothèques




from typing_extensions import Self
import xarray as xr
import pandas as pd
import numpy as np
from datetime import datetime, date, time
import re
import os
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QVBoxLayout, QPlainTextEdit, QHBoxLayout, QTableWidget, QListWidget, QScrollBar, QSlider, QComboBox, QLabel, QFileDialog, QPushButton, QMdiSubWindow
from PyQt6.QtCore import Qt




# Définition de la classe vueMainwindow




class vueMainwindow(QMainWindow):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()
        

    # Définition des méthodes


    def init_ui(self):
        
        self.setWindowTitle("Project")
        modeleMainwindow.screen_width = QApplication.primaryScreen().availableGeometry().width()
        modeleMainwindow.screen_height = QApplication.primaryScreen().availableGeometry().height()
        modeleMainwindow.set_screen_resolution(int(QApplication.primaryScreen().availableGeometry().width() * 0.40), int(QApplication.primaryScreen().availableGeometry().height() * 0.90))
        self.setMinimumSize(modeleMainwindow.screen_width, modeleMainwindow.screen_height)
        
        self.mainwindow_vuetoolbar = vueToolbar(self)
        self.addToolBar(self.mainwindow_vuetoolbar)
        
        self.mainwindow_central_widget = QWidget()
        self.setCentralWidget(self.mainwindow_central_widget)
        
        self.mainwindow_layout = QVBoxLayout(self.mainwindow_central_widget)
        self.mainwindow_tabwidget = QTabWidget()
        self.mainwindow_vuenetcdf = vueNetCDF()
        
        self.mainwindow_tabwidget.addTab(self.mainwindow_vuenetcdf, "Arrange Data")
        
        self.mainwindow_label = QLabel("Logs")
        self.mainwindow_textarea = QPlainTextEdit()
        
        self.mainwindow_textarea.setReadOnly(True)
        for log in modeleMainwindow.logs:
            self.mainwindow_textarea.appendPlainText(str(log))
        
        self.mainwindow_layout.addWidget(self.mainwindow_tabwidget)
        self.mainwindow_layout.addWidget(self.mainwindow_label)
        self.mainwindow_layout.addWidget(self.mainwindow_textarea)




# Programme principal




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    vuemainwindow = vueMainwindow()
    vuemainwindow.show()
    sys.exit(app.exec())
    