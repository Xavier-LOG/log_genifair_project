# Définition de la classe controleurNetcdfviewer




class controleurNetcdfviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuenetcdfviewer):
        
        super().__init__()
        self.vuenetcdfviewer = vuenetcdfviewer
        
    
    # Définition des méthodes
    
    
    def load_netcdf(self, modelenetcdf):
        
        # Mise à jour du fichier netcdf dans la vue
        self.vuenetcdfviewer.groupbox_textarea.setPlainText("")
        
        self.vuenetcdfviewer.groupbox_textarea.appendPlainText(str(modelenetcdf.get_xarray_dataset()))
