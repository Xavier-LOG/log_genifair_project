# Importation des bibliothèques




import pandas as pd




# Définition de la classe controleurCatalogsettings




class controleurCatalogsettings:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogsettings):
        
        super().__init__()
        self.vuecatalogsettings = vuecatalogsettings
        self.dataframe = pd.DataFrame()
        self.signal = self.vuecatalogsettings.vuecatalog.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.set_dataframe)

    
    # Définition des méthodes
    
    
    def set_dataframe(self, obj):
        
        self.dataframe = obj[1][0]
    
    
    def fill_catalog(self):
        
        dimension: str = ""
        # Si les chemins de fichier existent
        if self.vuecatalogsettings.vuecatalog.modelecatalog.path_list_files[1]:
            # Si le dataframe existe
            if not self.dataframe.empty:
                if self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked() or self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_time_series_catalog_checkbox.isChecked():
                    dimension = "Datetime"
                elif self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_profil_catalog_checkbox.isChecked():
                    dimension = "Depth"
                elif self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_sampling_catalog_checkbox.isChecked():
                    dimension = "Rows"
                catalog = {
                    "variable": {
                    },
                    "dimension": [
                        dimension
                    ],
                    "global_attribute": {
                        "title": "CF File version 1"
                    }
                }
                # Parcours de chaque colonne du dataframe
                for column in self.dataframe.columns:
                    catalog['variable'][column] = {
                    "dimension" : [dimension],
                    "attribute" : {
                        "long_name" : str(column),
                        "standard_name" : str(column),
                        "dtype" : str(self.dataframe[column].dtype)
                    }
                }
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()            
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Empty dataframe. Catalog will not be filled.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Empty dataframe. Catalog will not be filled.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("No path file. Catalog will not be filled.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("No path file. Catalog will not be filled.\n", "red")
    
    
    def dimension_name_add(self):
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.add_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il n'est pas dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name not in catalog['dimension']:
                catalog['dimension'].append(dimension_name)
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
            
    
    def dimension_name_modify_confirm(self):
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name in catalog['dimension']:
                self.vuecatalogsettings.dimension_tabwidget.modify_name_lineedit.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_confirm_button.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_name_lineedit.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_name_modify_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
        
    
    def dimension_name_modify_cancel(self):
        
        self.vuecatalogsettings.dimension_tabwidget.modify_name_lineedit.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.modify_name_confirm_button.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.modify_new_name_lineedit.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.modify_new_name_modify_button.setEnabled(False)
    
    
    def dimension_name_modify(self):
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_name_lineedit.text()
        dimension_new_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_new_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il n'est pas dans le catalogue
            if dimension_new_name != "" and any(char.isspace() for char in dimension_new_name) == False and dimension_new_name not in catalog['dimension']:
                index = catalog['dimension'].index(dimension_name)
                catalog['dimension'][index] = dimension_new_name
            
                # Recherche des variables ayant pour dimension dimension_name
                for variable_name, variable_data in catalog['variable'].items():
                    if 'dimension' in variable_data and dimension_name in variable_data['dimension']:
                        variable_data['dimension'] = [dimension_new_name]
            
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_lineedit.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_confirm_button.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_name_lineedit.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_name_modify_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")

    
    def dimension_name_delete(self):
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.delete_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension est inclu dans le catalogue et s'il y a au minimum plusieurs dimensions
            if dimension_name in catalog['dimension'] and len(catalog['dimension']) > 1:
                catalog['dimension'].remove(dimension_name)
            
                variables_to_remove = []
                # Recherche des variables ayant pour dimension dimension_name
                for variable_name, variable_data in catalog['variable'].items():
                    if 'dimension' in variable_data and dimension_name in variable_data['dimension']:
                        variables_to_remove.append(variable_name)
                for variable in variables_to_remove:
                    # Suppression des variables ayant pour dimension dimension_name
                    del catalog['variable'][variable]
            
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name deleted.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name. The model structure must depend on at least 1 dimension. Please enter a new dimension first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name. The model structure must depend on at least 1 dimension. Please enter a new dimension first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_add(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_name_lineedit.text()
        variable_dimension: str = self.vuecatalogsettings.variable_tabwidget.add_dimension_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, s'il n'est pas dans le catalogue et si la dimension de la variable est correcte
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name not in list(catalog['variable'].keys()) and variable_dimension in catalog['dimension']:
                catalog['variable'][variable_name] = {
                    "dimension" : [variable_dimension],
                    "attribute" : {}
                }
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_add_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_confirm_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_value_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_add_cancel(self):
        
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_lineedit.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_confirm_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_button.setEnabled(False)
    
    
    def variable_attribute_add(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_lineedit.text()
        attribute_value: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_value_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut et de la nouvelle valeur n'est pas vide et s'il ne contient aucun espace blanc
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name not in list(catalog['variable'][variable_name]['attribute'].keys()) and attribute_value != "" and any(char.isspace() for char in attribute_value) == False:
                catalog['variable'][variable_name]["attribute"][attribute_name] = attribute_value
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_confirm_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_value_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information name added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information name added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_modify_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
                self.vuecatalogsettings.variable_tabwidget.modify_name_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_name_confirm_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_new_name_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_dimension_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_new_name_modify_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_modify_cancel(self):
        
        self.vuecatalogsettings.variable_tabwidget.modify_name_lineedit.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_name_confirm_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_dimension_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_modify_button.setEnabled(False)
    
    
    def variable_name_modify(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_name_lineedit.text()
        variable_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_name_lineedit.text()
        dimension_name: str = self.vuecatalogsettings.variable_tabwidget.modify_dimension_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable et de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et si le nom de la nouvelle variable est différent du nom original de la variable
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_new_name != variable_name and dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name in catalog['dimension']:
                catalog['variable'][variable_new_name] = {
                    "dimension" : [dimension_name],
                    "attribute" : catalog['variable'][variable_name]['attribute']
                }
                del catalog['variable'][variable_name]
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.variable_tabwidget.modify_name_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_name_confirm_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_name_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_dimension_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_name_modify_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name and dimension name modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name and dimension name modified.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_variable_modify_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_variable_modify_cancel(self):
        
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)
    
    
    def variable_attribute_modify_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name in list(catalog['variable'][variable_name]['attribute'].keys()):
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_modify_cancel(self):
        
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)


    def variable_attribute_modify(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_lineedit.text()
        attribute_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_lineedit.text()
        attribute_new_value: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut n'est pas vide et s'il ne contient aucun espace blanc
            if attribute_new_name != "" and any(char.isspace() for char in attribute_new_name) == False and attribute_new_value != "":
                catalog['variable'][variable_name]['attribute'][attribute_new_name] = catalog['variable'][variable_name]['attribute'].pop(attribute_name)
                catalog['variable'][variable_name]['attribute'][attribute_new_name] = attribute_new_value
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information name modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information name modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_delete(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable est inclu dans le catalogue et s'il y a au minimum plusieurs variables
            if variable_name in list(catalog['variable'].keys()) and len(list(catalog['variable'].keys())) > 1:
                del catalog['variable'][variable_name]
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable deleted.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name. The model structure must depend on at least 1 variable. Please enter a new variable first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name. The model structure must depend on at least 1 variable. Please enter a new variable first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_delete_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_lineedit.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_confirm_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_lineedit.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_delete_cancel(self):
        
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_lineedit.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_button.setEnabled(False)
    
    
    def variable_attribute_delete(self):        
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut est inclu dans le catalogue
            if attribute_name in list(catalog['variable'][variable_name]['attribute'].keys()):
                del catalog['variable'][variable_name]['attribute'][attribute_name]
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information deleted.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name. The model structure must depend on at least 1 attribute. Please enter a new attribute first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name. The model structure must depend on at least 1 attribute. Please enter a new attribute first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")


    def global_attribute_name_add(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il n'est pas dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name not in list(catalog['global_attribute'].keys()):
                catalog['global_attribute'][global_attribute_name] = ""
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_add_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_confirm_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.add_value_lineedit.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.add_value_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_add_cancel(self):
        
        self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.add_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.add_value_button.setEnabled(False)
    
    
    def global_attribute_value_add(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_lineedit.text()
        global_attribute_value: str = self.vuecatalogsettings.attribute_tabwidget.add_value_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide
            if global_attribute_value != "":
                catalog['global_attribute'][global_attribute_name] = global_attribute_value
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_lineedit.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_confirm_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.add_value_lineedit.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.add_value_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Information added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect information.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect information.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_name_modify_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
                self.vuecatalogsettings.attribute_tabwidget.modify_name_lineedit.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_name_confirm_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_name_lineedit.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_name_modify_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_name_modify_cancel(self):
        
        self.vuecatalogsettings.attribute_tabwidget.modify_name_lineedit.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_name_confirm_button.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_name_lineedit.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_name_modify_button.setEnabled(False)
    
    
    def global_attribute_name_modify(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_name_lineedit.text()
        global_attribute_new_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_new_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est différent du nom original de l'attribut global
            if global_attribute_new_name != "" and any(char.isspace() for char in global_attribute_new_name) == False and global_attribute_name != global_attribute_new_name:
                catalog['global_attribute'][global_attribute_new_name] = catalog['global_attribute'][global_attribute_name]
                del catalog['global_attribute'][global_attribute_name]
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.attribute_tabwidget.modify_name_lineedit.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_name_confirm_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_name_lineedit.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_name_modify_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_modify_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_confirm_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_value_lineedit.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_value_modify_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_modify_cancel(self):
        
        self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_value_modify_button.setEnabled(False)
    
    
    def global_attribute_value_modify(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_lineedit.text()
        global_attribute_new_value: str = self.vuecatalogsettings.attribute_tabwidget.modify_new_value_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si la nouvelle valeur de l'attribut global n'est pas vide
            if global_attribute_new_value != "":
                catalog['global_attribute'][global_attribute_name] = global_attribute_new_value
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_lineedit.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_confirm_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_value_lineedit.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_value_modify_button.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Information modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect information.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect information.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_name_delete(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.delete_name_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global est inclu dans le catalogue et s'il y a au minimum 1 attribut global
            if global_attribute_name in list(catalog['global_attribute'].keys()) and len(list(catalog['global_attribute'].keys())) > 1:
                del catalog['global_attribute'][global_attribute_name]
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global information deleted.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name. The model structure must depend on at least 1 global information. Please enter a new global information first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name. The model structure must depend on at least 1 global information. Please enter a new global information first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_delete_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
                self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_lineedit.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_confirm_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.delete_value_button.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_delete_cancel(self):
        
        self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.delete_value_button.setEnabled(False)
    
    
    def global_attribute_value_delete(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_lineedit.text()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            catalog['global_attribute'][global_attribute_name] = "?"
            self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
            self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_lineedit.setEnabled(True)
            self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_confirm_button.setEnabled(True)
            self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_cancel_button.setEnabled(False)
            self.vuecatalogsettings.attribute_tabwidget.delete_value_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Information deleted.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information deleted.\n", "green")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
