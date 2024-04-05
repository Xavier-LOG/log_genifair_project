# Importation des bibliothèques




import json




# Importation des fichiers




from controleurCatalogviewer import controleurCatalogviewer




# Définition de la classe controleurCatalogtype




class controleurCatalogtype:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogtype):
        
        self.vuecatalogtype = vuecatalogtype
        self.modelecatalog = self.vuecatalogtype.vuecatalog.modelecatalog
        self.controleurcatalogviewer = controleurCatalogviewer(self.vuecatalogtype.vuecatalog.vuecatalogviewer)
    
    
    # Définition des méthodes
    
    
    def trajectory_catalog(self):
        
        if self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.isChecked():
            self.modelecatalog.catalog_name = 'trajectory_catalog.json'
            self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
        else:
            self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
            
    
    
    def timeseries_catalog(self):
        
        if self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.isChecked():
            self.modelecatalog.catalog_name = 'timeseries_catalog.json'
            self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
        else:
            self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
    
    
    def profil_catalog(self):
        
        if self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.isChecked():
            self.modelecatalog.catalog_name = 'profil_catalog.json'
            self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
        else:
            self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(True)
            self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
            self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
    
    
    def confirm(self):
        
        self.controleurcatalogviewer.load_catalog()
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.setEnabled(True)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.setEnabled(True)
        self.vuecatalogtype.vuecatalog.vuecatalog_save_button.setEnabled(True)
        self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(True)
        self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(True)
    
    
    def cancel(self):
        
        self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setChecked(False)
        self.vuecatalogtype.vuecatalog.vuecatalogviewer.setEnabled(False)
        self.vuecatalogtype.vuecatalog.vuecatalogsettings.setEnabled(False)
        self.vuecatalogtype.vuecatalog.vuecatalog_save_button.setEnabled(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_trajectory_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.vuecatalogtype_groupbox_time_series_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.vuecatalogtype_groupbox_profil_catalog_checkbox.setEnabled(True)
        self.vuecatalogtype.vuecatalogtype_groupbox_confirm_button.setEnabled(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_cancel_button.setEnabled(False)
        self.vuecatalogtype.vuecatalogtype_groupbox_catalog_restore_button.setEnabled(False)
    
    
    def restore(self):
        
        # Chargement le fichier JSON
        with open('./' + self.modelecatalog.catalog_name[:-5] + '_save.json', 'r') as f:
            catalog = json.load(f)
        
        # Ecriture du fichier JSON 
        with open('./' + self.modelecatalog.catalog_name, "w") as f:
            json.dump(catalog, f, indent = 4)
        
        self.controleurcatalogviewer.load_catalog()
