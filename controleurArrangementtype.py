# Importation des bibliothèques




import json
from PyQt6.QtWidgets import QFileDialog




# Définition de la classe controleurArrangementtype




class controleurArrangementtype:


    # Constructeur par défaut
        
    
    def __init__(self, vuearrangementtype):
        
        super().__init__()        
        self.vuearrangementtype = vuearrangementtype
    
    
    # Définition des méthodes
    
    
    def trajectory_arrangement(self):
        
        if self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.isChecked():
            self.vuearrangementtype.vuearrangement.modelearrangement.path_list_files[0] = "./trajectory_catalog.json"
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(True)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(True)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Trajectory catalog has been selected.\n")
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Trajectory catalog has been selected.\n", "green")
        else:
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(False)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(False)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
    
    
    def timeseries_arrangement(self):
        
        if self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.isChecked():
            self.vuearrangementtype.vuearrangement.modelearrangement.path_list_files[0] = "./timeseries_catalog.json"
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(True)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(True)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Timeseries catalog has been selected.\n")
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Timeseries catalog has been selected.\n", "green")
        else:
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(False)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(False)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
    
    
    def profile_arrangement(self):
        
        if self.vuearrangementtype.groupbox_profile_arrangement_checkbox.isChecked():
            self.vuearrangementtype.vuearrangement.modelearrangement.path_list_files[0] = "./profile_catalog.json"
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(True)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(True)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Profile catalog has been selected.\n")
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Profile catalog has been selected.\n", "green")
        else:
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(False)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(False)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
    
    
    def sample_arrangement(self):
        
        if self.vuearrangementtype.groupbox_sample_arrangement_checkbox.isChecked():
            self.vuearrangementtype.vuearrangement.modelearrangement.path_list_files[0] = "./sample_catalog.json"
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(False)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(True)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(True)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Sample catalog has been selected.\n")
            self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Sample catalog has been selected.\n", "green")
        else:
            self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(True)
            self.vuearrangementtype.groupbox_confirm_button.setEnabled(False)
            self.vuearrangementtype.groupbox_cancel_button.setEnabled(False)
            self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
            self.vuearrangementtype.groupbox_open_button.setEnabled(False)
    
    
    def confirm(self):
        
        self.vuearrangementtype.vuearrangement.vuearrangementviewer.setEnabled(True)
        self.vuearrangementtype.vuearrangement.vuearrangementsettings.setEnabled(True)
        self.vuearrangementtype.vuearrangement.vuearrangementsettings.button.setEnabled(False)
        self.vuearrangementtype.vuearrangement.groupbox_save_button.setEnabled(True)
        self.vuearrangementtype.vuearrangement.groupbox_confirm_button.setEnabled(False)
        self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(False)
        self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(False)
        self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(False)
        self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(False)
        self.vuearrangementtype.groupbox_confirm_button.setEnabled(False)
        self.vuearrangementtype.groupbox_cancel_button.setEnabled(True)
        self.vuearrangementtype.groupbox_restore_button.setEnabled(True)
        self.vuearrangementtype.groupbox_open_button.setEnabled(True)
        self.vuearrangementtype.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuetoolbar.menu_file_button.setEnabled(True)
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog type confirmed. Please, set catalog settings or confirm catalog to process data.\n")
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog type confirmed. Please, set catalog settings or confirm catalog to process data.\n", "green")
    
    
    def cancel(self):
        
        self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setChecked(False)
        self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setChecked(False)
        self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setChecked(False)
        self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setChecked(False)
        self.vuearrangementtype.vuearrangement.vuearrangementviewer.setEnabled(False)
        self.vuearrangementtype.vuearrangement.vuearrangementsettings.setEnabled(False)
        self.vuearrangementtype.vuearrangement.vuearrangementsettings.button.setEnabled(False)
        self.vuearrangementtype.vuearrangement.groupbox_save_button.setEnabled(False)
        self.vuearrangementtype.vuearrangement.groupbox_confirm_button.setEnabled(False)
        self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.setEnabled(True)
        self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.setEnabled(True)
        self.vuearrangementtype.groupbox_profile_arrangement_checkbox.setEnabled(True)
        self.vuearrangementtype.groupbox_sample_arrangement_checkbox.setEnabled(True)
        self.vuearrangementtype.groupbox_confirm_button.setEnabled(False)
        self.vuearrangementtype.groupbox_cancel_button.setEnabled(False)
        self.vuearrangementtype.groupbox_restore_button.setEnabled(False)
        self.vuearrangementtype.groupbox_open_button.setEnabled(False)
        self.vuearrangementtype.vuearrangement.vuemainwindow.tabwidget.setTabEnabled(1, False)
        self.vuearrangementtype.vuearrangement.vuemainwindow.tabwidget.setCurrentIndex(0)
        self.vuearrangementtype.vuearrangement.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.clearContents()
        self.vuearrangementtype.vuearrangement.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setRowCount(20)
        self.vuearrangementtype.vuearrangement.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setColumnCount(20)
        self.vuearrangementtype.vuearrangement.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setHorizontalHeaderLabels([str(i + 1) for i in range(20)])
        self.vuearrangementtype.vuearrangement.vuemainwindow.vueconversion.vuenetcdfviewer.groupbox_textarea.setPlainText("")
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuefileviewer.groupbox_textarea.setPlainText("")
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuetoolbar.menu_file_button.setEnabled(False)
        self.vuearrangementtype.vuearrangement.modelearrangement.path_list_files = ["", []]
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuetoolbar.controleurtoolbar.file_list = []
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list = []
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog has been cancelled. Please, choose a new catalog type to proceed.\n")
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog has been cancelled. Please, choose a new catalog type to proceed.\n", "orange")
    
    
    def restore(self):
        
        arrangement = {}
        if self.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.isChecked():
            arrangement_path = './trajectory_catalog.json'
        elif self.vuearrangementtype.groupbox_time_series_arrangement_checkbox.isChecked():
            arrangement_path = './timeseries_catalog.json'
        elif self.vuearrangementtype.groupbox_profile_arrangement_checkbox.isChecked():
            arrangement_path = './profile_catalog.json'
        elif self.vuearrangementtype.groupbox_sample_arrangement_checkbox.isChecked():
            arrangement_path = './sample_catalog.json'
            
        with open(arrangement_path[:-5] + "_save.json", 'r') as f:
            arrangement = json.load(f)
        with open(self.vuearrangementtype.vuearrangement.modelearrangement.path_list_files[0], 'w') as f:
            json.dump(arrangement, f, indent = 4)
        self.vuearrangementtype.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Default catalog has been restored for the selected catalog. Please, set catalog settings or confirm catalog to process data.")
        self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Default catalog has been restored for the selected catalog. Please, set catalog settings or confirm catalog to process data.", "green")
    
    
    def open(self):
        
        file_path, _ = QFileDialog.getOpenFileName(self.vuearrangementtype, "Open JSON file", "", "JSON file (*.json)")
        if file_path:
            if file_path.endswith(".json"):
                self.vuearrangementtype.vuearrangement.modelearrangement.path_list_files[0] = str(file_path)
                self.vuearrangementtype.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Selected catalog has been opened. Please, set catalog settings or confirm catalog to process data.\n")
                self.vuearrangementtype.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Selected catalog has been opened. Please, set catalog settings or confirm catalog to process data.\n", "green")