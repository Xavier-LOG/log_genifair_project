# Importation des bibliothèques




import json
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import pyqtSignal, QObject




# Définition de la classe controleurCatalogtype




class controleurCatalogtype(QObject):
    
    
    signal = pyqtSignal(str)


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogtype):
        
        super().__init__()
        self.vuecatalogtype = vuecatalogtype
        self.modelecatalog = self.vuecatalogtype.vuecatalog.modelecatalog
        self.controleurlogs = self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs
    
    
    # Définition des méthodes
    
    
    def trajectory_catalog(self):
        
        if self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked():
            self.controleurlogs.log("Trajectory catalog has been selected.\n")
            self.controleurlogs.addColoredText("Trajectory catalog has been selected.\n", "green")
            self.modelecatalog.catalog_path = './trajectory_catalog.json'
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
        else:
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
            
    
    
    def timeseries_catalog(self):
        
        if self.vuecatalogtype.groupbox_time_series_catalog_checkbox.isChecked():
            self.controleurlogs.log("Timeseries catalog has been selected.\n")
            self.controleurlogs.addColoredText("Timeseries catalog has been selected.\n", "green")
            self.modelecatalog.catalog_path = './timeseries_catalog.json'
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
        else:
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
    
    
    def profil_catalog(self):
        
        if self.vuecatalogtype.groupbox_profil_catalog_checkbox.isChecked():
            self.controleurlogs.log("Profil catalog has been selected.\n")
            self.controleurlogs.addColoredText("Profil catalog has been selected.\n", "green")
            self.modelecatalog.catalog_path = './profil_catalog.json'
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
        else:
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
    
    
    def sampling_catalog(self):
        
        if self.vuecatalogtype.groupbox_sampling_catalog_checkbox.isChecked():
            self.controleurlogs.log("Sampling catalog has been selected.\n")
            self.controleurlogs.addColoredText("Sampling catalog has been selected.\n", "green")
            self.modelecatalog.catalog_path = './sampling_catalog.json'
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
        else:
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
    
    
    def confirm(self):
        
        self.controleurlogs.log("Catalog type confirmed. Please, set catalog settings or confirm catalog to process data.\n")
        self.controleurlogs.addColoredText("Catalog type confirmed. Please, set catalog settings or confirm catalog to process data.\n", "green")
        self.signal.emit("load_catalog")
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.setEnabled(True)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.setEnabled(True)
        self.vuecatalogtype.vuecatalog.save_button.setEnabled(True)
        self.vuecatalogtype.vuecatalog.confirm_button.setEnabled(True)
        self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
        self.vuecatalogtype.groupbox_restore_button.setEnabled(True)
        self.vuecatalogtype.groupbox_open_button.setEnabled(True)
    
    
    def cancel(self):
        
        self.controleurlogs.log("Catalog has been cancelled. Please, choose a new catalog type to proceed.\n")
        self.controleurlogs.addColoredText("Catalog has been cancelled. Please, choose a new catalog type to proceed.\n", "orange")
        self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.groupbox_profil_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.groupbox_sampling_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.setEnabled(False)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.setEnabled(False)
        self.vuecatalogtype.vuecatalog.save_button.setEnabled(False)
        self.vuecatalogtype.vuecatalog.confirm_button.setEnabled(False)
        self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.groupbox_profil_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
        self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
        self.vuecatalogtype.groupbox_open_button.setEnabled(False)
        self.vuecatalogtype.vuecatalog.vuemainwindow.tabwidget.setTabEnabled(1, False)
        self.vuecatalogtype.vuecatalog.vuemainwindow.tabwidget.setCurrentIndex(0)
        self.vuecatalogtype.vuecatalog.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.clearContents()
        self.vuecatalogtype.vuecatalog.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setRowCount(20)
        self.vuecatalogtype.vuecatalog.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setColumnCount(20)
        self.vuecatalogtype.vuecatalog.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setHorizontalHeaderLabels([str(i + 1) for i in range(20)])
        self.vuecatalogtype.vuecatalog.vuemainwindow.vueconversion.vuenetcdfviewer.groupbox_textarea.setPlainText("")
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuefileviewer.groupbox_textarea.setPlainText("")
        
    
    def restore(self):
        
        catalog = {}
        if self.modelecatalog.catalog_path == "./trajectory_catalog.json" or self.modelecatalog.catalog_path == "./timeseries_catalog.json" or self.modelecatalog.catalog_path == "./profil_catalog.json" or self.modelecatalog.catalog_path == "./sampling_catalog.json":            
            with open(self.modelecatalog.catalog_path[:-5] + '_save.json', 'r') as f:
                catalog = json.load(f)
            with open(self.modelecatalog.catalog_path, 'w') as f:
                json.dump(catalog, f, indent = 4)
            self.controleurlogs.log("Default catalog has been restored for the selected catalog. Please, set catalog settings or confirm catalog to process data.")
            self.controleurlogs.addColoredText("Default catalog has been restored for the selected catalog. Please, set catalog settings or confirm catalog to process data.\n", "green")
            self.signal.emit("load_catalog")
    
    
    def open(self):
        
        file_path, _ = QFileDialog.getOpenFileName(self.vuecatalogtype, "Open JSON file", "", "JSON file (*.json)")
        if file_path:
            if file_path.endswith(".json"):
                self.modelecatalog.catalog_path = file_path
                self.controleurlogs.log("Selected catalog has been opened. Please, set catalog settings or confirm catalog to process data.\n")
                self.controleurlogs.addColoredText("Selected catalog has been opened. Please, set catalog settings or confirm catalog to process data.\n", "green")
                self.signal.emit("load_catalog")
