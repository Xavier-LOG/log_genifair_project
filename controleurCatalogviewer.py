# Importation des bibliothèques




import os




# Définition de la classe controleurCatalogviewer




class controleurCatalogviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogviewer):
        
        super().__init__()
        self.vuecatalogviewer = vuecatalogviewer

    
    # Définition des méthodes


    def load_catalog(self):
        
        # Mise à jour du catalogue dans la vue
        self.vuecatalogviewer.groupbox_textarea.setPlainText("")
        
        file_path: str = self.vuecatalogviewer.vuecatalog.modelecatalog.path_list_files[0]
        catalog = self.vuecatalogviewer.vuecatalog.modelecatalog.read_json()
            
        if catalog:
            
            catalog_name = file_path[:-5][2:].replace("_", " ").capitalize()
            
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n" + os.path.basename(catalog_name) + " : " + "\n")
            
            # Accès à chaque valeur de chaque attribut du catalogue
            variable_catalog = catalog['variable']
            dimension_catalog = catalog['dimension']
            global_attribute_catalog = catalog['global_attribute']
        
            # Affichage des dimensions du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText(str("\nDimensions :\n"))
            for dimension in dimension_catalog:
                self.vuecatalogviewer.groupbox_textarea.appendPlainText(str(f"\t{dimension}"))
        
            # Affichage des variables du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\nVariables :")
            for variable_name, variable_data in variable_catalog.items():
                self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n\t" + str(variable_name) + "(" + str(variable_data['dimension']) + ")")
                self.vuecatalogviewer.groupbox_textarea.appendPlainText(str("\tVariable Information :"))
                for attribute_name, attribute_value in variable_data['attribute'].items():
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText(str(f"\t\t{attribute_name} : {attribute_value}"))
        
            # Affichage des attributs globaux du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText(str("\nGlobal Information :\n"))
            for global_attribute_name, global_attribute_value in global_attribute_catalog.items():
                self.vuecatalogviewer.groupbox_textarea.appendPlainText(str(f"\t{global_attribute_name} : {global_attribute_value}"))
            
            self.vuecatalogviewer.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog has been loaded.\n")
            self.vuecatalogviewer.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog has been loaded.\n", "green")
