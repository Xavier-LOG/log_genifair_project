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
        
        # Chargement du dataframe dans vueDataframeviewer
        self.vuedataframeviewer.groupbox_tablewidget.setRowCount(len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns))
        self.vuedataframeviewer.groupbox_tablewidget.setColumnCount(len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].index))
        self.vuedataframeviewer.groupbox_tablewidget.setHorizontalHeaderLabels(list(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns))
        for row in range(len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].index)):
            for col in range(len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns)):
                item = str(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].iloc[row, col])
                self.vuedataframeviewer.groupbox_tablewidget.setItem(row, col, QTableWidgetItem(item))

        self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Dataframe has been loaded.\n")
        self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dataframe has been loaded.\n", "green")
