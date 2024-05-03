# Importation des bibliothèques




import os




# Définition de la classe controleurArrangementviewer




class controleurArrangementviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuearrangementviewer):
        
        super().__init__()
        self.vuearrangementviewer = vuearrangementviewer

    
    # Définition des méthodes


    def load_arrangement(self):
        
        # Mise à jour de l'agencement dans la vue
        self.vuearrangementviewer.groupbox_textarea.setPlainText("")
        
        file_path: str = self.vuearrangementviewer.vuearrangement.modelearrangement.path_list_files[0]
        arrangement = self.vuearrangementviewer.vuearrangement.modelearrangement.read_json()
            
        if arrangement:
            
            arrangement_name = file_path[:-5][2:].replace("_", " ").capitalize()
            
            self.vuearrangementviewer.groupbox_textarea.appendPlainText("\n" + os.path.basename(arrangement_name) + " : " + "\n")
        
            # Affichage des dimensions de l'agencement
            self.vuearrangementviewer.groupbox_textarea.appendPlainText(str("\ndimensions:"))
            for dimension_name in arrangement['dimension']:
                self.vuearrangementviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = " + str(len(arrangement['dimension'][dimension_name]['values'])) + ";")
                self.vuearrangementviewer.groupbox_textarea.appendPlainText("\t\t" + str(dimension_name) + " = " + str(arrangement['dimension'][dimension_name]['values']) + ";")
        
            # Affichage des variables de l'agencement
            self.vuearrangementviewer.groupbox_textarea.appendPlainText("\nvariables:")
            for variable_name in arrangement['variable']:
                self.vuearrangementviewer.groupbox_textarea.appendPlainText("\t" + str(arrangement['variable'][variable_name]['attribute'][':dtype'][:-2]) + " " + str(variable_name) + "(" + str(arrangement['variable'][variable_name]['dimension']) + ");")
                for attribute_name, attribute_value in arrangement['variable'][variable_name]['attribute'].items():
                    self.vuearrangementviewer.groupbox_textarea.appendPlainText("\t\t" + str(attribute_name) + " = " + str(attribute_value) + ";")
        
            # Affichage des attributs globaux de l'agencement
            self.vuearrangementviewer.groupbox_textarea.appendPlainText(str("\nattributes:"))
            for global_attribute_name, global_attribute_value in arrangement['global_attribute'].items():
                self.vuearrangementviewer.groupbox_textarea.appendPlainText("\t" + str(global_attribute_name) + " = " + str(global_attribute_value) + ";")
            
            self.vuearrangementviewer.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Arrangement has been loaded.\n")
            self.vuearrangementviewer.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Arrangement has been loaded.\n", "green")
