# Définition de la classe controleurCatalogviewer




class controleurCatalogviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogviewer):
        
        self.vuecatalogviewer = vuecatalogviewer
        self.modelecatalog = self.vuecatalogviewer.vuecatalog.modelecatalog

    
    # Définition des méthodes


    def load_catalog(self):
        
        # Mise à jour du catalogue dans la vue
        self.vuecatalogviewer.vuecatalogviewer_textarea.setPlainText("")
        
        catalog = self.modelecatalog.read_json()
            
        # Accès à chaque valeur de chaque attribut du catalogue
        variable_catalog = catalog['variable']
        dimension_catalog = catalog['dimension']
        global_attribute_catalog = catalog['global_attribute']
        
        # Affichage des dimensions du catalogue
        self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str("\nDimensions :\n"))
        for dimension in dimension_catalog:
            self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str(f"\t{dimension}"))
        
        # Affichage des variables du catalogue
        self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText("\nVariable :")
        for variable_name, variable_data in variable_catalog.items():
            self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str("\n\tVariable Name : ") + str(variable_name))
            self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str("\tDimension :") + str(variable_data['dimension']))
            self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str("\tVariable Information :"))
            for attribute_name, attribute_value in variable_data['attribute'].items():
                self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str(f"\t\t{attribute_name} : {attribute_value}"))
        
        # Affichage des attributs globaux du catalogue
        self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str("\nGlobal Information :\n"))
        for global_attribute_name, global_attribute_value in global_attribute_catalog.items():
            self.vuecatalogviewer.vuecatalogviewer_textarea.appendPlainText(str(f"\t{global_attribute_name} : {global_attribute_value}"))
