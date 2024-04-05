# Importation des bibliothèques




import json




# Définition de la classe modeleCatalog




class modeleCatalog:
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        self.catalog_name = ""
    
    
    # Définition des méthodes
    
    
    def read_json(self):
        
        # Chargement le fichier JSON
        with open('./' + self.catalog_name, 'r') as f:
            catalog = json.load(f)
        return catalog
    
    
    def write_json(self, catalog):
        
        # Ecriture du fichier JSON 
        with open('./' + self.catalog_name, "w") as f:
            json.dump(catalog, f, indent = 4)
