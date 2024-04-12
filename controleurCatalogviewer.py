# Définition de la classe controleurCatalogviewer




class controleurCatalogviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogviewer):
        
        super().__init__()
        self.vuecatalogviewer = vuecatalogviewer
        self.modelecatalog = self.vuecatalogviewer.vuecatalog.modelecatalog
        self.controleurlogs = self.vuecatalogviewer.vuecatalog.vuemainwindow.vuelogs.controleurlogs
        self.signal = self.vuecatalogviewer.vuecatalog.vuecatalogtype.controleurcatalogtype.signal
        self.signal.connect(self.load_catalog)

    
    # Définition des méthodes


    def load_catalog(self):
        
        # Mise à jour du catalogue dans la vue
        self.vuecatalogviewer.textarea.setPlainText("")
        
        catalog = self.modelecatalog.read_json()
            
        if catalog:

            self.controleurlogs.log("Catalog has been loaded.\n")
            self.controleurlogs.addColoredText("Catalog has been loaded.\n", "green")
            
            self.vuecatalogviewer.textarea.appendPlainText("\n" + self.vuecatalogviewer.vuecatalog.modelecatalog.catalog_path[:-5][2:].replace("_", " ").capitalize() + " : " + "\n")
            
            # Accès à chaque valeur de chaque attribut du catalogue
            variable_catalog = catalog['variable']
            dimension_catalog = catalog['dimension']
            global_attribute_catalog = catalog['global_attribute']
        
            # Affichage des dimensions du catalogue
            self.vuecatalogviewer.textarea.appendPlainText(str("\nDimensions :\n"))
            for dimension in dimension_catalog:
                self.vuecatalogviewer.textarea.appendPlainText(str(f"\t{dimension}"))
        
            # Affichage des variables du catalogue
            self.vuecatalogviewer.textarea.appendPlainText("\nVariables :")
            for variable_name, variable_data in variable_catalog.items():
                self.vuecatalogviewer.textarea.appendPlainText("\n\t" + str(variable_name) + "(" + str(variable_data['dimension']) + ")")
                self.vuecatalogviewer.textarea.appendPlainText(str("\tVariable Information :"))
                for attribute_name, attribute_value in variable_data['attribute'].items():
                    self.vuecatalogviewer.textarea.appendPlainText(str(f"\t\t{attribute_name} : {attribute_value}"))
        
            # Affichage des attributs globaux du catalogue
            self.vuecatalogviewer.textarea.appendPlainText(str("\nGlobal Information :\n"))
            for global_attribute_name, global_attribute_value in global_attribute_catalog.items():
                self.vuecatalogviewer.textarea.appendPlainText(str(f"\t{global_attribute_name} : {global_attribute_value}"))
