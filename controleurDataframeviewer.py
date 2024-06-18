# Importation des bibliothèques




from PyQt6.QtWidgets import QTableWidgetItem




# Définition de la classe controleurDataframeviewer




class controleurDataframeviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuedataframeviewer):
        
        super().__init__()
        self.vuedataframeviewer = vuedataframeviewer
    
    
    # Définition des méthodes
    
    
    def load_dataframe(self):

        """_summary_
        Affichage du premier dataframe dans la vue
        """
        
        # Si la liste des dataframes existe
        if self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list:
            # Si le premier dataframe contient plus de 20 colonnes
            if len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns) > 20:
                total_column = 20
                # Initialisation d'une liste de labels contenant les 20 premiers noms de colonne
                labels = list(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns[:20])
            # Sinon
            else:
                total_column = len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns)
                # Initialisation d'une liste de labels contenant les noms de colonne
                labels = list(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns)
            # Si le premier dataframe contient plus de 20 lignes
            if len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].index) > 20:
                total_row = 20
            # Sinon
            else:
                total_row = len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].index)
            # Définition du nombre de colonnes dans le widget
            self.vuedataframeviewer.groupbox_tablewidget.setRowCount(total_column)
            # Définition du nombre de lignes dans le widget
            self.vuedataframeviewer.groupbox_tablewidget.setColumnCount(total_row)
            # Définition des noms de colonne du widget
            self.vuedataframeviewer.groupbox_tablewidget.setHorizontalHeaderLabels(labels)
            for row in range(total_row):
                for col in range(total_column):
                    # Récupération de la donnée du dataframe suivant la ligne et la colonne et conversion en str
                    item = str(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].iloc[row, col])
                    # Création d'un item dans le widget qui est la donnée du dataframe convertie
                    self.vuedataframeviewer.groupbox_tablewidget.setItem(row, col, QTableWidgetItem(item))

            self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Dataframe has been loaded.\n")
            self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dataframe has been loaded.\n", "green")
        else:
            self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("No dataframe detected.\n")
            self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("No dataframe detected.\n", "red")
