# Importation des bibliothèques




import json
import os




# Définition de la classe modeleCatalog




class modeleCatalog:
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        self.path_list_files = ["", []]
    
    
    # Définition des méthodes
    
    
    def read_json(self):
        
        catalog = {}
        if self.path_list_files[0] != "":
            if os.path.getsize(self.path_list_files[0]) != 0:
                # Chargement le fichier JSON
                with open(self.path_list_files[0], 'r') as f:
                    catalog = json.load(f)
        return catalog
    
    
    def write_json(self, catalog):
        
        # Ecriture du fichier JSON 
        with open(self.path_list_files[0], "w") as f:
            json.dump(catalog, f, indent = 4)
