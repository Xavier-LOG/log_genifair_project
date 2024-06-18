# Importation des bibliothèques




import os
import pydoc




# Définition de la fonction




def doc_gen(directory):
       
    """_summary_
    Génération de la documentation pydoc
    root : répertoire
    _ : sous-dossiers
    files : fichiers du répertoire
    """
    
    # Parcours du répertoire de façon récursive
    for root, _, files in os.walk(directory):
        # Parcours de chaque fichier du répertoire
        for file in files:
            # Si le fichier se termine par .py
            if file.endswith(".py"):
                # Nom du module sans le format .py
                module_name = file[:-3]
                # Création de la documentation pour le module
                pydoc.writedoc(module_name)




# Programme principal




if __name__ == "__main__":
    
    doc_gen(".")
