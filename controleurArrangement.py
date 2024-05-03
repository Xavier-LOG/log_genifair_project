# Importation des bibliothèques




import json
from PyQt6.QtWidgets import QFileDialog




# Définition de la classe controleurArrangement




class controleurArrangement:


    # Constructeur par défaut

    
    def __init__(self, vuearrangement):
        
        super().__init__()        
        self.vuearrangement = vuearrangement
        self.signal = self.vuearrangement.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.modify_path_list_files)
    
    
    # Définition des méthodes
    
    
    def modify_path_list_files(self, obj):
        
        self.vuearrangement.modelearrangement.path_list_files[1] = obj[0]
    
    
    def save(self):
    
        file_path, _ = QFileDialog.getSaveFileName(self.vuearrangement, "Save File", ".json", "JSON file (*.json)")
        if file_path and file_path.endswith(".json"):
            arrangement = self.vuearrangement.modelearrangement.read_json()
            # Si l'agencement existe
            if arrangement:
                with open(file_path, "w") as f:
                    json.dump(arrangement, f, indent = 4)
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Files have been saved.\n")
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Files have been saved.\n", "green")
            # Sinon
            else:
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement.\n")
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement.\n", "red")
        # Sinon
        else:
            self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def confirm(self):
        
        arrangement = self.vuearrangement.modelearrangement.read_json()
        if self.vuearrangement.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list:
            # Si l'agencement existe
            if arrangement:
                self.vuearrangement.vuearrangementtype.groupbox_restore_button.setEnabled(False)
                self.vuearrangement.vuearrangementtype.groupbox_open_button.setEnabled(False)
                self.vuearrangement.vuearrangementsettings.setEnabled(False)
                self.vuearrangement.groupbox_save_button.setEnabled(False)
                self.vuearrangement.groupbox_confirm_button.setEnabled(False)
                self.vuearrangement.vuemainwindow.tabwidget.setTabEnabled(1, True)
                self.vuearrangement.vuemainwindow.tabwidget.setCurrentIndex(1)
                self.vuearrangement.vuemainwindow.vueconversion.setEnabled(True)
                self.vuearrangement.vuemainwindow.vueconversion.vuedataframeviewer.controleurdataframeviewer.load_dataframe()
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Arrangement confirmed.\n")
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Arrangement confirmed.\n", "green")
            # Sinon
            else:        
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
                self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
        # Sinon
        else:        
            self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown file(s).\n")
            self.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown file(s).\n", "red")
