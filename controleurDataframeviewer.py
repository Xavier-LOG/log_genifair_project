# Importation des bibliothèques




from PyQt6.QtWidgets import QTableWidgetItem




# Définition de la classe controleurDataframeviewer




class controleurDataframeviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuedataframeviewer):
        
        super().__init__()
        self.vuedataframeviewer = vuedataframeviewer
        self.controleurlogs = self.vuedataframeviewer.vueconversion.vuemainwindow.vuelogs.controleurlogs
        self.signal = self.vuedataframeviewer.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.load_dataframe)
    
    
    # Définition des méthodes
    
    
    def load_dataframe(self, obj):

        self.controleurlogs.log("Dataframe has been loaded.\n")
        self.controleurlogs.addColoredText("Dataframe has been loaded.\n", "green")
        
        self.vuedataframeviewer.vueconversion.vuemainwindow.tabwidget.setTabEnabled(1, True)
        self.vuedataframeviewer.vueconversion.vuemainwindow.tabwidget.setCurrentIndex(1)
        self.vuedataframeviewer.vueconversion.setEnabled(True)
        # Chargement du dataframe dans vueDataframeviewer
        self.vuedataframeviewer.groupbox_tablewidget.setRowCount(len(obj[0].columns))
        self.vuedataframeviewer.groupbox_tablewidget.setColumnCount(len(obj[0].index))
        self.vuedataframeviewer.groupbox_tablewidget.setHorizontalHeaderLabels(list(obj[0].columns))
        for row in range(len(obj[0].index)):
            for col in range(len(obj[0].columns)):
                item = str(obj[0].iloc[row, col])
                self.vuedataframeviewer.groupbox_tablewidget.setItem(row, col, QTableWidgetItem(item))
