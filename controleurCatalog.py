# Importation des bibliothèques




import json




# Définition de la classe controleurCatalog




class controleurCatalog:


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalog):
        
        self.vuecatalog = vuecatalog
        self.modelecatalog = self.vuecatalog.modelecatalog
    
    
    # Définition des méthodes
    
    
    def save(self):
        
        catalog = self.modelecatalog.read_json()
        # Ecriture du fichier JSON 
        with open('./' + self.modelecatalog.catalog_name[:-5] + '_save.json', "w") as f:
            json.dump(catalog, f, indent = 4)
