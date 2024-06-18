# Importation des bibliothèques




import json
from PyQt6.QtWidgets import QFileDialog




# Définition de la classe controleurCatalog




class controleurCatalog:


    # Constructeur par défaut

    
    def __init__(self, vuecatalog):
        
        super().__init__()
        # vueCatalog
        self.vuecatalog = vuecatalog
        # Signal pour récupérer les chemins de fichier lors de leur importation en modifiant modeleCatalog
        self.signal = self.vuecatalog.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.modify_path_list_files)
    
    
    # Définition des méthodes
    
    
    def modify_path_list_files(self, obj):
        
        """_summary_
        Mise à jour des chemins de fichier lors de l'importation
        """
        
        # Récupération des chemins de fichier
        self.vuecatalog.modelecatalog.path_list_files[1] = obj[0]
    
    
    def save(self):
    
        """_summary_
        Sauvegarde du catalogue choisi
        """
    
        # Ouverture d'une fenêtre permettant à l'utilisateur de choisir où et sous quel nom enregistrer le catalogue
        file_path, _ = QFileDialog.getSaveFileName(self.vuecatalog, "Save File", ".json", "JSON file (*.json)")
        if file_path and file_path.endswith(".json"):
            # Lecture du catalogue
            catalog = self.vuecatalog.modelecatalog.read_json()
            # Si le catalogue existe
            if catalog:
                # Ecriture du catalogue
                with open(file_path, "w") as f:
                    json.dump(catalog, f, indent = 4)
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog has been saved.\n")
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog has been saved.\n", "green")
            # Sinon
            else:
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog.\n")
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog.\n", "red")
        # Sinon
        else:
            self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def confirm(self):

        """_summary_
        Confirmation du catalogue choisi
        """
        
        # Lecture du catalogue
        catalog = self.vuecatalog.modelecatalog.read_json()
        if self.vuecatalog.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list:
            # Si le catalogue existe
            if catalog:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalog.vuecatalogtype.groupbox_restore_button.setEnabled(False)
                self.vuecatalog.vuecatalogtype.groupbox_open_button.setEnabled(False)
                self.vuecatalog.vuecatalogsettings.setEnabled(False)
                self.vuecatalog.groupbox_save_button.setEnabled(False)
                self.vuecatalog.groupbox_confirm_button.setEnabled(False)
                self.vuecatalog.vuemainwindow.tabwidget.setTabEnabled(1, True)
                self.vuecatalog.vuemainwindow.tabwidget.setCurrentIndex(1)
                self.vuecatalog.vuemainwindow.vueconversion.setEnabled(True)
                self.vuecatalog.vuemainwindow.vueconversion.vuedataframeviewer.controleurdataframeviewer.load_dataframe()
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog confirmed.\n")
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog confirmed.\n", "green")
            # Sinon
            else:        
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
                self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
        # Sinon
        else:        
            self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown file(s).\n")
            self.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown file(s).\n", "red")
