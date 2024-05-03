# Importation des bibliothèques




import json
import os




# Définition de la classe modeleArrangement




class modeleArrangement:
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        self.path_list_files = ["", []]
    
    
    # Définition des méthodes
    
    
    def read_json(self):
        
        arrangement = {}
        if self.path_list_files[0] != "":
            if os.path.getsize(self.path_list_files[0]) != 0:
                # Chargement le fichier JSON
                with open(self.path_list_files[0], 'r') as f:
                    arrangement = json.load(f)
        return arrangement
    
    
    def write_json(self, arrangement):
        
        # Ecriture du fichier JSON 
        with open(self.path_list_files[0], "w") as f:
            json.dump(arrangement, f, indent = 4)
