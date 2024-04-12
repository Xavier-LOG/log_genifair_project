# Importation des fichiers




from modeleNetcdf import modeleNetcdf




# Importations des bibliothèques




import pandas as pd
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import pyqtSignal, QObject




# Définition de la classe controleurConversionsettings




class controleurConversionsettings(QObject):


    signal_modelenetcdf = pyqtSignal(modeleNetcdf)


    # Constructeur par défaut
        
    
    def __init__(self, vueconversionsettings):
        
        super().__init__()
        self.vueconversionsettings = vueconversionsettings
        self.controleurlogs = self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs
        self.dataframe = pd.DataFrame()
        self.catalog_path = ""
        self.file = ""
        self.signal = self.vueconversionsettings.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.set_attrs)
    
    
    # Définition des méthodes
    
    
    def set_attrs(self, obj):
        
        self.dataframe = obj[0]
        self.catalog_path = obj[1]
        self.file = obj[2]
    
    
    def convert(self):

        modelenetcdf = modeleNetcdf(self.controleurlogs, self.dataframe, modeleNetcdf.create_xarray_dataset(self.dataframe, self.catalog_path))
        modelenetcdf.check_dataframe_integrity()
        modelenetcdf.check_datetime_format()
        modelenetcdf.adapt_xarray_dataset()
        if modelenetcdf.get_xarray_dataset():
            self.signal_modelenetcdf.emit(modelenetcdf)
            self.controleurlogs.log("Netcdf file has been created. Please, select a save location to proceed.\n")
            self.controleurlogs.addColoredText("Netcdf file has been created. Please, select a save location to proceed.\n", "green")
            file_path, _ = QFileDialog.getSaveFileName(self.vueconversionsettings, "Save NetCDF File", self.file[:self.file.find(".")] + ".nc", "NetCDF File (*.nc)")
            if file_path:
                if file_path.endswith(".nc"):
                    with open(file_path, "w") as f:
                        modelenetcdf.get_xarray_dataset().to_netcdf(file_path)
                        self.controleurlogs.log("Netcdf file has been saved. Click on Cancel in Arrange Data to convert a new file again.\n")
                        self.controleurlogs.addColoredText("Netcdf file has been saved. Click on Cancel in Arrange Data to convert a new file again.\n", "green")
                else:
                    self.controleurlogs.log("Incorrect file format. Click on Cancel in Arrange Data to convert a new file again.\n")
                    self.controleurlogs.addColoredText("Incorrect file format. Click on Cancel in Arrange Data to convert a new file again.\n", "red")
            else:
                self.controleurlogs.log("NetCDF file has not been saved. Click on Cancel in Arrange Data to convert a new file again.\n")
                self.controleurlogs.addColoredText("NetCDF file has not been saved. Click on Cancel in Arrange Data to convert a new file again.\n", "red")
        else:
            self.controleurlogs.log("Incorrect file content. Click on Cancel in Arrange Data to convert a new file again.\n")
            self.controleurlogs.addColoredText("Incorrect file content. Click on Cancel in Arrange Data to convert a new file again.\n", "red")
