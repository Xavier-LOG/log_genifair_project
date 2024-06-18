# Importation des bibliothèques




import json
import os




# Définition de la classe modeleCatalog




class modeleCatalog:
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        # Initialisation d'une liste contenant le chemin du catalogue choisi et une liste des dataframes des fichiers importés
        self.path_list_files = ["", []]
    
    
    # Définition des méthodes
    
    
    def read_json(self):
        
        """_summary_
        Lecture du catalogue
        Returns:
            _type_: _description_
        """
        
        catalog = {}
        if self.path_list_files[0] != "":
            # Si la taille du fichier n'est pas vide
            if os.path.getsize(self.path_list_files[0]) != 0:
                # Chargement le fichier JSON
                with open(self.path_list_files[0], 'r') as f:
                    # Chargement du catalogue
                    catalog = json.load(f)
        return catalog
    
    
    def write_json(self, catalog):
        
        """_summary_
        Ecriture du catalogue
        """
        
        # Ecriture du fichier JSON 
        with open(self.path_list_files[0], "w") as f:
            json.dump(catalog, f, indent = 4)
