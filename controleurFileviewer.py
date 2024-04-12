# Définition de la classe controleurFileviewer




class controleurFileviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuefileviewer):
        
        super().__init__()
        self.vuefileviewer = vuefileviewer
        self.file = ""
        self.signal = self.vuefileviewer.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.load_file_name)
    
    
    # Définition des méthodes
    
    
    def load_file_name(self, obj):
        
        self.vuefileviewer.groupbox_textarea.setPlainText("")
        
        self.vuefileviewer.groupbox_textarea.appendPlainText("\n" + str(obj[2]))
        