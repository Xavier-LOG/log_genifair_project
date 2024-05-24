# Importation des bibliothèques




import os
from PyQt6.QtCore import pyqtSignal, QObject




# Définition de la classe controleurCatalogviewer




class controleurCatalogviewer(QObject):


    signal = pyqtSignal(dict)


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
        self.signal.emit(catalog)
            
        if catalog:
            
            catalog_name = file_path[:-5][2:]
            
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n" + "netcdf " + os.path.basename(catalog_name) + " { " + "\n")
        
            # Affichage des dimensions du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\ndimensions :\n")
            for dimension_name in catalog['dimension']:
                if len(catalog['dimension'][dimension_name]['values']) == 0:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = UNLIMITED ; ")
                else:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = " + str(len(catalog['dimension'][dimension_name]['values'])) + " ; ")
        
            # Affichage des variables du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\nvariables :")
            for variable_name in catalog['variable']:
                if str(catalog['variable'][variable_name]['attribute'][':dtype']) != "object":
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n\t" + str(catalog['variable'][variable_name]['attribute'][':dtype'][:-2]) + " " + str(variable_name) + "(" + str(catalog['variable'][variable_name]['dimension']) + "); ")
                else:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n\t" + str(catalog['variable'][variable_name]['attribute'][':dtype']) + " " + str(variable_name) + "(" + str(catalog['variable'][variable_name]['dimension']) + "); ")
                for attribute_name, attribute_value in catalog['variable'][variable_name]['attribute'].items():
                    if attribute_name != "column_name":
                        self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t\t" + str(variable_name) + str(attribute_name) + " = " + str(attribute_value) + " ; ")
        
            # Affichage des attributs globaux du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n// global attributes:\n")
            for global_attribute_name, global_attribute_value in catalog['global_attribute'].items():
                self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(global_attribute_name) + " = " + str(global_attribute_value) + " ; ")

            # Affichage des valeurs des dimensions du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\ndata :\n")
            for dimension_name in catalog['dimension']:
                if catalog['dimension'][dimension_name]['values'] == []:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = " + "UNLIMITED" + " ; ")
                else:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = " + str(catalog['dimension'][dimension_name]['values']) + " ; ")

            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n" + " }; " + "\n")
            
            self.vuecatalogviewer.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog has been loaded.\n")
            self.vuecatalogviewer.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog has been loaded.\n", "green")
