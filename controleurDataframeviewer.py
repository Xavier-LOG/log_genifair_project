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
        if len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns) > 20:
            total_column = len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns[:20])
            labels = list(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns[:20])
        else:
            total_column = len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns)
            labels = list(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].columns)
        if len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].index) > 20:
            total_row = len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].head(20))
        else:
            total_row = len(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].index)
        self.vuedataframeviewer.groupbox_tablewidget.setRowCount(total_column)
        self.vuedataframeviewer.groupbox_tablewidget.setColumnCount(total_row)
        self.vuedataframeviewer.groupbox_tablewidget.setHorizontalHeaderLabels(labels)
        for row in range(total_row):
            for col in range(total_column):
                item = str(self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[0].iloc[row, col])
                self.vuedataframeviewer.groupbox_tablewidget.setItem(row, col, QTableWidgetItem(item))

        self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Dataframe has been loaded.\n")
        self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dataframe has been loaded.\n", "green")
