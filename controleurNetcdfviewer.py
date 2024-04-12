# Définition de la classe controleurNetcdfviewer




class controleurNetcdfviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuenetcdfviewer):
        
        super().__init__()
        self.vuenetcdfviewer = vuenetcdfviewer
        self.signal = self.vuenetcdfviewer.vueconversion.vueconversionsettings.controleurconversionsettings.signal_modelenetcdf
        self.signal.connect(self.load_netcdf)
        
    
    # Définition des méthodes
    
    
    def load_netcdf(self, modelenetcdf):
        
        # Mise à jour du fichier netcdf dans la vue
        self.vuenetcdfviewer.groupbox_textarea.setPlainText("")
        
        self.vuenetcdfviewer.groupbox_textarea.appendPlainText(str(modelenetcdf.get_xarray_dataset()))
