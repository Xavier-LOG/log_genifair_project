# Importation des bibliothèques




import json
from PyQt6.QtWidgets import QFileDialog




# Définition de la classe controleurCatalog




class controleurCatalog:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalog):
        
        super().__init__()
        self.vuecatalog = vuecatalog
        self.modelecatalog = self.vuecatalog.modelecatalog
        self.controleurlogs = self.vuecatalog.vuemainwindow.vuelogs.controleurlogs
    
    
    # Définition des méthodes
    
    
    def save(self):
        
        catalog = self.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            file_path, _ = QFileDialog.getSaveFileName(self.vuecatalog, "Save File", ".json", "JSON file (*.json)")
            if file_path:
                if file_path.endswith(".json"):
                    with open(file_path, "w") as f:
                        json.dump(catalog, f, indent = 4)
                    self.controleurlogs.log("File has been saved.\n")
                    self.controleurlogs.addColoredText("File has been saved.\n", "green")
        # Sinon
        else:
            self.controleurlogs.log("Unknown catalog type.\n")
            self.controleurlogs.addColoredText("Unknown catalog type.\n", "red")
    
    
    def confirm(self):
        
        catalog = self.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            self.controleurlogs.log("Catalog confirmed. Please, import file(s) to proceed data.\n")
            self.controleurlogs.addColoredText("Catalog confirmed. Please, import file(s) to proceed data.\n", "green")
            self.vuecatalog.vuecatalogtype.groupbox_restore_button.setEnabled(False)
            self.vuecatalog.vuecatalogtype.groupbox_open_button.setEnabled(False)
            self.vuecatalog.vuecatalogsettings.setEnabled(False)
            self.vuecatalog.save_button.setEnabled(False)
            self.vuecatalog.confirm_button.setEnabled(False)
            self.vuecatalog.vuemainwindow.vuetoolbar.menu_file.setEnabled(True)
        # Sinon
        else:
            self.controleurlogs.log("Unknown catalog type.\n")
            self.controleurlogs.addColoredText("Unknown catalog type.\n", "red")
