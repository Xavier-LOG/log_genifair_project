# Définition de la classe controleurNetcdfviewer




class controleurNetcdfviewer:


    # Constructeur par défaut
        
    
    def __init__(self, vuenetcdfviewer):
        
        super().__init__()
        self.vuenetcdfviewer = vuenetcdfviewer
        
    
    # Définition des méthodes
    
    
    def load_netcdf(self, xarray_dataset):
        
        """_summary_
        Affichage du fichier dans la vue
        """
        
        # Mise à jour du fichier netcdf dans la vue
        self.vuenetcdfviewer.groupbox_textarea.setPlainText("")
        
        self.vuenetcdfviewer.groupbox_textarea.appendPlainText(str(xarray_dataset.get_xarray_dataset()))
