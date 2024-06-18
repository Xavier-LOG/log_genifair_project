# Importation des bibliothèques




import os
from PyQt6.QtGui import QTextCursor
from PyQt6.QtCore import pyqtSignal, QObject




# Définition de la classe controleurCatalogviewer




class controleurCatalogviewer(QObject):


    signal = pyqtSignal(dict)


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogviewer):
        
        super().__init__()
        self.vuecatalogviewer = vuecatalogviewer

    
    # Définition des méthodes


    def load_catalog(self):
        
        """_summary_
        Chargement du catalogue choisi dans la vue
        """
        
        # Mise à jour du catalogue dans la vue
        self.vuecatalogviewer.groupbox_textarea.setPlainText("")
        
        # Récupération du chemin du catalogue
        file_path: str = self.vuecatalogviewer.vuecatalog.modelecatalog.path_list_files[0]
        # Lecture du catalogue
        catalog = self.vuecatalogviewer.vuecatalog.modelecatalog.read_json()
        # Emission du signal vers controleurCatalogSettings pour remplir les listes déroulantes
        self.signal.emit(catalog)
            
        # Si le catalogue existe
        if catalog:
            
            # Récupération du nom du catalogue à partir de son chemin
            catalog_name = file_path[:-5][2:]
            
            # Ajout du nom du catalogue dans la zone de texte
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n" + "netcdf " + os.path.basename(catalog_name) + " { " + "\n")
        
            # Affichage des dimensions du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\ndimensions :\n")
            # Parcours des dimensions du catalogue
            for dimension_name in catalog['dimension']:
                # Si la dimension n'a pas de valeur
                if len(catalog['dimension'][dimension_name]['values']) == 0:
                    # Affichage de UNLIMITED
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = UNLIMITED ; ")
                # Sinon
                else:
                    # Affichage des valeurs
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = " + str(len(catalog['dimension'][dimension_name]['values'])) + " ; ")
        
            # Affichage des variables du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\nvariables :")
            # Parcours des variables du catalogue
            for variable_name in catalog['variable']:
                if str(catalog['variable'][variable_name]['attribute'][':dtype']) != "object":
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n\t" + str(catalog['variable'][variable_name]['attribute'][':dtype'][:-2]) + " " + str(variable_name) + "(" + str(catalog['variable'][variable_name]['dimension']) + "); ")
                else:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n\t" + str(catalog['variable'][variable_name]['attribute'][':dtype']) + " " + str(variable_name) + "(" + str(catalog['variable'][variable_name]['dimension']) + "); ")
                for attribute_name, attribute_value in catalog['variable'][variable_name]['attribute'].items():
                    if attribute_name != "column_name":
                        self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t\t" + str(variable_name) + str(attribute_name) + " = " + str(attribute_value) + " ; ")
        
            # Affichage des attributs globaux du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n// global attributes:\n")
            for global_attribute_name, global_attribute_value in catalog['global_attribute'].items():
                self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(global_attribute_name) + " = " + str(global_attribute_value) + " ; ")

            # Affichage des valeurs des dimensions du catalogue
            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\ndata :\n")
            for dimension_name in catalog['dimension']:
                if catalog['dimension'][dimension_name]['values'] == []:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = " + "UNLIMITED" + " ; ")
                else:
                    self.vuecatalogviewer.groupbox_textarea.appendPlainText("\t" + str(dimension_name) + " = " + str(catalog['dimension'][dimension_name]['values']) + " ; ")

            self.vuecatalogviewer.groupbox_textarea.appendPlainText("\n" + " }; " + "\n")
            
            self.vuecatalogviewer.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Catalog has been loaded.\n")
            self.vuecatalogviewer.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Catalog has been loaded.\n", "green")
    
    
    def toggle_searchbar(self):
        
        """_summary_
        Gérer la visibilité de la barre de recherche dans la vue
        """
        
        # Si la barre de recherche est visible
        if self.vuecatalogviewer.groupbox_searchbar.isVisible():
            self.vuecatalogviewer.groupbox_searchbar.setVisible(False)
            # Permet de commencer à taper immédiatement
            self.vuecatalogviewer.groupbox_textarea.setFocus()
        else:
            self.vuecatalogviewer.groupbox_searchbar.setVisible(True)
            # Permet de commencer à taper immédiatement
            self.vuecatalogviewer.groupbox_textarea.setFocus()
    
    
    def find_keyword(self):
        
        """_summary_
        Surlignage du mot de la barre de recherche dans la vue
        """
        
        # Obtient le curseur actuel du QPlainTextEdit (sert à sélectionner un mot dans le texte du QPlainTextEdit)
        cursor = self.vuecatalogviewer.groupbox_textarea.textCursor()
        # Commence un bloc d'édition (bloc pour rechercher un mot dans le texte du QPlainTextEdit)
        cursor.beginEditBlock()

        # Déplace le curseur au début du texte du QPlainTextEdit
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        # Met à jour le curseur dans le QPlainTextEdit
        self.vuecatalogviewer.groupbox_textarea.setTextCursor(cursor)

        # Récupère le mot à rechercher depuis la barre de recherche
        search_word = self.vuecatalogviewer.groupbox_searchbar.text()
        # Récupère le texte du QPlainTextEdit sous forme de document
        document = self.vuecatalogviewer.groupbox_textarea.document()
        
        # Si le mot à rechercher existe
        if search_word:
            found = False
            # Continue la recherche tant que le curseur n'est pas nul et qu'il n'est pas à la fin du document
            while not cursor.isNull() and not cursor.atEnd():
                # Cherche la première occurrence du mot à partir de la position actuelle du curseur jusqu'à la fin du document. Si aucune correspondance n'est trouvée avant la fin du document, le curseur est nul
                cursor = document.find(search_word, cursor)
                # Si une occurrence est trouvée
                if not cursor.isNull():
                    found = True
                    # Met à jour le curseur pour le déplacer vers la position de la première occurrence du mot trouvée dans le document
                    self.vuecatalogviewer.groupbox_textarea.setTextCursor(cursor)
                    # Fin de boucle
                    break

            # Si le mot à rechercher a été trouvé
            if found == True:
                # Réinitialise le style de la barre de recherche
                self.vuecatalogviewer.groupbox_searchbar.setStyleSheet("")
            # Sinon
            else:
                # Change la couleur du fond d'écran en rouge
                self.vuecatalogviewer.groupbox_searchbar.setStyleSheet("background-color: red;")

        # Termine le bloc d'édition
        cursor.endEditBlock()
