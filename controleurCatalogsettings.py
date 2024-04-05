# Importation des fichiers




from controleurMainwindow import controleurMainwindow
from controleurCatalogviewer import controleurCatalogviewer




# Importation des bibliothèques




import json




# Définition de la classe controleurCatalogsettings




class controleurCatalogsettings:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogsettings):
        
        self.vuecatalogsettings = vuecatalogsettings
        self.modelemainwindow = self.vuecatalogsettings.vuecatalog.mainwindow.modelemainwindow
        self.modelecatalog = self.vuecatalogsettings.vuecatalog.modelecatalog
        self.controleurmainwindow = controleurMainwindow(self.vuecatalogsettings.vuecatalog.mainwindow)
        self.controleurcatalogviewer = controleurCatalogviewer(self.vuecatalogsettings.vuecatalog.vuecatalogviewer)

    
    # Définition des méthodes
    
    
    def dimension_name_add(self):
        
        dimension_name: str = self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_add_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il n'est pas dans le catalogue
        if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name not in catalog['dimension']:
            catalog['dimension'].append(dimension_name)
            self.modelecatalog.write_json(catalog)
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Dimension added")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect dimension name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
            
    
    def dimension_name_modify_confirm(self):
        
        dimension_name: str = self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name in catalog['dimension']:
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_modify_button.setEnabled(True)
            self.modelemainwindow.log("Dimension name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect dimension name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)

    
    def dimension_name_modify_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_modify_button.setEnabled(False)
    
    
    def dimension_name_modify(self):
        
        dimension_name: str = self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_lineedit.text()
        dimension_new_name: str = self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il n'est pas dans le catalogue
        if dimension_new_name != "" and any(char.isspace() for char in dimension_new_name) == False and dimension_new_name not in catalog['dimension']:
            index = catalog['dimension'].index(dimension_name)
            catalog['dimension'][index] = dimension_new_name
            
            # Recherche des variables ayant pour dimension dimension_name
            for variable_name, variable_data in catalog['variable'].items():
                if 'dimension' in variable_data and dimension_name in variable_data['dimension']:
                    variable_data['dimension'] = [dimension_new_name]
            
            self.modelecatalog.write_json()
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_modify_button.setEnabled(False)
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Dimension name modified")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect dimension name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)

    
    def dimension_name_delete(self):
        
        dimension_name: str = self.vuecatalogsettings.vuecatalogsettings_dimension_tabwidget.dimensiontab_delete_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
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
            
            self.modelecatalog.write_json()
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Dimension deleted")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect dimension name. The model structure must depend on at least 1 dimension. Please enter a new dimension first")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_name_add(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_name_lineedit.text()
        variable_dimension: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_dimension_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, s'il n'est pas dans le catalogue et si la dimension de la variable est correcte
        if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name not in list(catalog['variable'].keys()) and variable_dimension in catalog['dimension']:
            catalog['variable'][variable_name] = {
                "dimension" : [variable_dimension],
                "attribute" : {}
            }
            self.modelecatalog.write_json()
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Variable name added")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_attribute_add_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_value_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_button.setEnabled(True)
            self.modelemainwindow.log("Variable name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_attribute_add_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_button.setEnabled(False)
    
    
    def variable_attribute_add(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_lineedit.text()
        attribute_value: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_value_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom du nouvel attribut et de la nouvelle valeur n'est pas vide et s'il ne contient aucun espace blanc
        if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name not in list(catalog['variable'][variable_name]['attribute'].keys()) and attribute_value != "" and any(char.isspace() for char in attribute_value) == False and attribute_value not in list(catalog['variable'][variable_name]['attribute'].values()):
            catalog['variable'][variable_name]["attribute"][attribute_name] = attribute_value
            self.modelecatalog.write_json()
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_value_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_button.setEnabled(False)
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Variable information name added")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_name_modify_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_dimension_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_modify_button.setEnabled(True)
            self.modelemainwindow.log("Variable name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_name_modify_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_dimension_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_modify_button.setEnabled(False)
    
    
    def variable_name_modify(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_lineedit.text()
        variable_new_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_lineedit.text()
        dimension_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_dimension_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la nouvelle variable et de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et si le nom de la nouvelle variable est différent du nom original de la variable
        if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_new_name != variable_name and dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name in catalog['dimension']:
            catalog['variable'][variable_new_name] = {
                "dimension" : [dimension_name],
                "attribute" : catalog['variable'][variable_name]['attribute']
            }
            del catalog['variable'][variable_name]
            self.modelecatalog.write_json()
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_dimension_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_modify_button.setEnabled(False)
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Variable name and dimension name modified")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_attribute_variable_modify_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_value_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_modify_button.setEnabled(False)
            self.modelemainwindow.log("Variable name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_attribute_variable_modify_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_confirm_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_modify_button.setEnabled(False)
    
    
    def variable_attribute_modify_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de l'attribut n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name in list(catalog['variable'][variable_name]['attribute'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_value_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_modify_button.setEnabled(True)
            self.modelemainwindow.log("Variable information name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_attribute_modify_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_confirm_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_cancel_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_modify_button.setEnabled(False)


    def variable_attribute_modify(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_lineedit.text()
        attribute_new_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_lineedit.text()
        attribute_new_value: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_value_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom du nouvel attribut n'est pas vide et s'il ne contient aucun espace blanc
        if attribute_new_name != "" and any(char.isspace() for char in attribute_new_name) == False and attribute_new_value != "":
            catalog['variable'][variable_name]['attribute'][attribute_new_name] = catalog['variable'][variable_name]['attribute'].pop(attribute_name)
            catalog['variable'][variable_name]['attribute'][attribute_new_name] = attribute_new_value
            self.modelecatalog.write_json()
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_value_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_modify_button.setEnabled(False)
            self.modelemainwindow.log("Variable information name modified")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect attribute name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)        
    
    
    def variable_name_delete(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la variable est inclu dans le catalogue et s'il y a au minimum plusieurs variables
        if variable_name in list(catalog['variable'].keys()) and len(list(catalog['variable'].keys())) > 1:
            del catalog['variable'][variable_name]
            self.modelecatalog.write_json()
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Variable deleted")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable name. The model structure must depend on at least 1 variable. Please enter a new variable first")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_attribute_delete_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_variable_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name in list(catalog['variable'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_variable_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_button.setEnabled(True)
            self.modelemainwindow.log("Variable name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def variable_attribute_delete_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_variable_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_button.setEnabled(False)
    
    
    def variable_attribute_delete(self):        
        
        variable_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_variable_lineedit.text()
        attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de l'attribut est inclu dans le catalogue
        if attribute_name in list(catalog['variable'][variable_name]['attribute'].keys()):
            del catalog['variable'][variable_name]['attribute'][attribute_name]
            self.modelecatalog.write_json()
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Variable information deleted")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect variable information name. The model structure must depend on at least 1 attribute. Please enter a new attribute first")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)


    def global_attribute_name_add(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il n'est pas dans le catalogue
        if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name not in list(catalog['global_attribute'].keys()):
            catalog['global_attribute'][global_attribute_name] = ""
            self.modelecatalog.write_json()
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Global information name added")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect global information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_value_add_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_button.setEnabled(True)
            self.modelemainwindow.log("Global information name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect global information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_value_add_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_button.setEnabled(False)
    
    
    def global_attribute_value_add(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_lineedit.text()
        global_attribute_value: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom du nouvel attribut global n'est pas vide
        if global_attribute_value != "":
            catalog['global_attribute'][global_attribute_name] = global_attribute_value
            self.modelecatalog.write_json()
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_button.setEnabled(False)
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Information added")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect information")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_name_modify_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_modify_button.setEnabled(True)
            self.modelemainwindow.log("Global information name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect global information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_name_modify_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_modify_button.setEnabled(False)
    
    
    def global_attribute_name_modify(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_lineedit.text()
        global_attribute_new_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est différent du nom original de l'attribut global
        if global_attribute_new_name != "" and any(char.isspace() for char in global_attribute_new_name) == False and global_attribute_name != global_attribute_new_name:
            catalog['global_attribute'][global_attribute_new_name] = catalog['global_attribute'][global_attribute_name]
            del catalog['global_attribute'][global_attribute_name]
            self.modelecatalog.write_json()
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_modify_button.setEnabled(False)
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Global information name modified")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect global information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_value_modify_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_modify_button.setEnabled(True)
            self.modelemainwindow.log("Global information name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect global information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_value_modify_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_lineedit.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_modify_button.setEnabled(False)
    
    
    def global_attribute_value_modify(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_lineedit.text()
        global_attribute_new_value: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si la nouvelle valeur de l'attribut global n'est pas vide
        if global_attribute_new_value != "":
            catalog['global_attribute'][global_attribute_name] = global_attribute_new_value
            self.modelecatalog.write_json()
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_lineedit.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_confirm_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_cancel_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_modify_button.setEnabled(False)
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Information modified")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect information")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_name_delete(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_name_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de l'attribut global est inclu dans le catalogue et s'il y a au minimum 1 attribut global
        if global_attribute_name in list(catalog['global_attribute'].keys()) and len(list(catalog['global_attribute'].keys())) > 1:
            del catalog['global_attribute'][global_attribute_name]
            self.modelecatalog.write_json()
            self.controleurcatalogviewer.load_catalog()
            self.modelemainwindow.log("Global information deleted")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect global information name. The model structure must depend on at least 1 global information. Please enter a new global information first")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_value_delete_confirm(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_lineedit.text()
        catalog = self.modelecatalog.read_json()
        # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
        if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name in list(catalog['global_attribute'].keys()):
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_lineedit.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_confirm_button.setEnabled(False)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_cancel_button.setEnabled(True)
            self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_button.setEnabled(True)
            self.modelemainwindow.log("Global information name selected")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
        # Sinon
        else:
            self.modelemainwindow.log("Incorrect global information name")
            self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
    
    
    def global_attribute_value_delete_cancel(self):
        
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_button.setEnabled(False)
    
    
    def global_attribute_value_delete(self):
        
        global_attribute_name: str = self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_lineedit.text()
        catalog = self.modelecatalog.read_json()
        catalog['global_attribute'][global_attribute_name] = "?"
        self.modelecatalog.write_json()
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_lineedit.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_confirm_button.setEnabled(True)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_button.setEnabled(False)
        self.controleurcatalogviewer.load_catalog()
        self.modelemainwindow.log("Information deleted")
        self.controleurmainwindow.load_logs(self.modelemainwindow.logs)
