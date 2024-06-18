# Définition de la classe controleurFileviewer




class controleurFileviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuefileviewer):
        
        super().__init__()
        self.vuefileviewer = vuefileviewer
        self.signal = self.vuefileviewer.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.load_file_name)
    
    
    # Définition des méthodes
    
    
    def load_file_name(self):
        
        """_summary_
        Affichage des chemins de fichier
        """
        
        self.vuefileviewer.groupbox_textarea.setPlainText("")
        
        for file_path in self.vuefileviewer.vuemainwindow.vuecatalog.modelecatalog.path_list_files[1]:
            self.vuefileviewer.groupbox_textarea.appendPlainText("\n" + str(file_path))
        