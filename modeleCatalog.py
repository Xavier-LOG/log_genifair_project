# Importation des bibliothèques




import json
import os




# Définition de la classe modeleCatalog




class modeleCatalog:
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        self.catalog_path = ""
    
    
    # Définition des méthodes
    
    
    def read_json(self):
        
        catalog = {}
        if self.catalog_path != "":
            if os.path.getsize(self.catalog_path) != 0:
                # Chargement le fichier JSON
                with open(self.catalog_path, 'r') as f:
                    catalog = json.load(f)
        return catalog
    
    
    def write_json(self, catalog):
        
        # Ecriture du fichier JSON 
        with open(self.catalog_path, "w") as f:
            json.dump(catalog, f, indent = 4)
