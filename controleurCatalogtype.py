# Importation des bibliothèques




import json
from PyQt6.QtWidgets import QFileDialog




# Définition de la classe controleurCatalogtype




class controleurCatalogtype:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogtype):
        
        super().__init__()        
        self.vuecatalogtype = vuecatalogtype
    
    
    # Définition des méthodes
    
    
    def trajectory_catalog(self):
        
        """_summary_
        Grisage et dégrisage de zones dans la vue lorsque le catalogue de type trajectoire est coché
        """
        
        # Si le catalogue de type trajectoire est coché
        if self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked():
            # Chemin du catalogue
            self.vuecatalogtype.vuecatalog.modelecatalog.path_list_files[0] = "./trajectory_catalog.json"
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Trajectory catalog has been selected.\n")
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Trajectory catalog has been selected.\n", "green")
        # Sinon
        else:
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
    
    
    def timeseries_catalog(self):
        
        """_summary_
        Grisage et dégrisage de zones dans la vue lorsque le catalogue de type série temporelle est coché
        """
        
        # Si le catalogue de type série temporelle est coché
        if self.vuecatalogtype.groupbox_time_series_catalog_checkbox.isChecked():
            # Chemin du catalogue
            self.vuecatalogtype.vuecatalog.modelecatalog.path_list_files[0] = "./timeseries_catalog.json"
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Timeseries catalog has been selected.\n")
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Timeseries catalog has been selected.\n", "green")
        # Sinon
        else:
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
    
    
    def profile_catalog(self):
        
        """_summary_
        Grisage et dégrisage de zones dans la vue lorsque le catalogue de type profil est coché
        """
        
        # Si le catalogue de type profil est coché
        if self.vuecatalogtype.groupbox_profile_catalog_checkbox.isChecked():
            # Chemin du catalogue
            self.vuecatalogtype.vuecatalog.modelecatalog.path_list_files[0] = "./profile_catalog.json"
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Profile catalog has been selected.\n")
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Profile catalog has been selected.\n", "green")
        # Sinon
        else:
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
    
    
    def sample_catalog(self):
        
        """_summary_
        Grisage et dégrisage de zones dans la vue lorsque le catalogue de type échantillonnage est coché
        """
        
        # Si le catalogue de type échantillonnage est coché
        if self.vuecatalogtype.groupbox_sample_catalog_checkbox.isChecked():
            # Chemin du fichier
            self.vuecatalogtype.vuecatalog.modelecatalog.path_list_files[0] = "./sample_catalog.json"
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Sample catalog has been selected.\n")
            self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Sample catalog has been selected.\n", "green")
        # Sinon
        else:
            # Grisage et dégrisage des zones nécessaires
            self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalogtype.groupbox_open_button.setEnabled(False)
    
    
    def confirm(self):
        
        """_summary_
        Grisage et dégrisage de zones dans la vue lorsque le catalogue choisi est confirmé
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.setEnabled(True)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.setEnabled(True)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.button.setEnabled(False)
        self.vuecatalogtype.vuecatalog.groupbox_save_button.setEnabled(True)
        self.vuecatalogtype.vuecatalog.groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype.groupbox_cancel_button.setEnabled(True)
        self.vuecatalogtype.groupbox_restore_button.setEnabled(True)
        self.vuecatalogtype.groupbox_open_button.setEnabled(True)
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuetoolbar.menu_file_button.setEnabled(True)
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog type confirmed. Please, set catalog settings or import file or folders to confirm catalog and process data.\n")
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog type confirmed. Please, set catalog settings or import file or folders to confirm catalog and process data.\n", "green")
    
    
    def cancel(self):
        
        """_summary_
        Réinitialisation
        """
        
        # Réinitialisation
        self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.groupbox_profile_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.groupbox_sample_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.setEnabled(False)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.setEnabled(False)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.button.setEnabled(False)
        self.vuecatalogtype.vuecatalog.groupbox_save_button.setEnabled(False)
        self.vuecatalogtype.vuecatalog.groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(True)
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
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuetoolbar.menu_file_button.setEnabled(False)
        self.vuecatalogtype.vuecatalog.modelecatalog.path_list_files = ["", []]
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuetoolbar.controleurtoolbar.file_list = []
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list = []
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog has been cancelled. Please, choose a new catalog type to proceed.\n")
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog has been cancelled. Please, choose a new catalog type to proceed.\n", "orange")
    
    
    def restore(self):
        
        """_summary_
        Restauration du catalogue choisi à partir de son type de catalogue
        """
        
        # Le catalogue est vide
        catalog = {}
        if self.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked():
            catalog_path = './trajectory_catalog.json'
        elif self.vuecatalogtype.groupbox_time_series_catalog_checkbox.isChecked():
            catalog_path = './timeseries_catalog.json'
        elif self.vuecatalogtype.groupbox_profile_catalog_checkbox.isChecked():
            catalog_path = './profile_catalog.json'
        elif self.vuecatalogtype.groupbox_sample_catalog_checkbox.isChecked():
            catalog_path = './sample_catalog.json'
            
        # Chargement du catalogue back-up
        with open(catalog_path[:-5] + "_save.json", 'r') as f:
            catalog = json.load(f)
        # Ecriture du catalogue à restorer
        with open(self.vuecatalogtype.vuecatalog.modelecatalog.path_list_files[0], 'w') as f:
            json.dump(catalog, f, indent = 4)
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Default catalog has been restored for the selected catalog. Please, set catalog settings or confirm catalog to process data.")
        self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Default catalog has been restored for the selected catalog. Please, set catalog settings or confirm catalog to process data.", "green")
    
    
    def open(self):
        
        """_summary_
        Ouverture d'un catalogue
        """
        
        # Ouverture d'une fenêtre permettant à l'utilisateur de sélectionner un catalogue à ouvrir
        file_path, _ = QFileDialog.getOpenFileName(self.vuecatalogtype, "Open JSON file", "", "JSON file (*.json)")
        # Si le chemin du catalogue existe
        if file_path:
            # Si le chemin du catalogue se termine au format JSON
            if file_path.endswith(".json"):
                self.vuecatalogtype.vuecatalog.modelecatalog.path_list_files[0] = str(file_path)
                self.vuecatalogtype.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Selected catalog has been opened. Please, set catalog settings or confirm catalog to process data.\n")
                self.vuecatalogtype.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Selected catalog has been opened. Please, set catalog settings or confirm catalog to process data.\n", "green")
