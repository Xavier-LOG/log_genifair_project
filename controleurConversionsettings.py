# Importation des fichiers




from modeleNetcdf import modeleNetcdf




# Importations des bibliothèques




from PyQt6.QtWidgets import QFileDialog




# Définition de la classe controleurConversionsettings




class controleurConversionsettings:


    # Constructeur par défaut
        
    
    def __init__(self, vueconversionsettings):
        
        super().__init__()
        self.vueconversionsettings = vueconversionsettings
    
    
    # Définition des méthodes
    
    
    def convert(self):

        file_path, _ = QFileDialog.getSaveFileName(self.vueconversionsettings, "Save NetCDF File", self.vueconversionsettings.vueconversion.vuemainwindow.vuearrangement.modelearrangement.path_list_files[1][0][:self.vueconversionsettings.vueconversion.vuemainwindow.vuearrangement.modelearrangement.path_list_files[1][0].find(".")] + ".nc", "NetCDF File (*.nc)")
        if file_path:
            if file_path.endswith(".nc"):
                for i in range(0, len(self.vueconversionsettings.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list)):
                    conversionlogs = self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs
                    dataframe = self.vueconversionsettings.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[i]
                    arrangement_path = self.vueconversionsettings.vueconversion.vuemainwindow.vuearrangement.modelearrangement.path_list_files[0]
                    xarray_dataset = modeleNetcdf.create_xarray_dataset(dataframe, arrangement_path)
                    xarray_dataset = modeleNetcdf.check_xarray_dataset(xarray_dataset)
                    modelenetcdf = modeleNetcdf(conversionlogs, dataframe, xarray_dataset)
                    modelenetcdf.check_dataframe_integrity()
                    modelenetcdf.check_datetime_format()
                    modelenetcdf.adapt_xarray_dataset()
                    if modelenetcdf.get_xarray_dataset():
                        modelenetcdf.get_xarray_dataset().to_netcdf(str(file_path[:file_path.find(".")]) + "_" + str(i + 1) + ".nc")
                        if i == len(self.vueconversionsettings.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list) - 1:
                            self.vueconversionsettings.vueconversion.vuenetcdfviewer.controleurnetcdfviewer.load_netcdf(modelenetcdf)
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Netcdf files have been saved. Click on Cancel in Arrange Data to convert a new file again.\n")
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Netcdf files have been saved. Click on Cancel in Arrange Data to convert a new file again.\n", "green")
            else:
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect file format. Click on Cancel in Arrange Data to convert a new file again.\n")
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect file format. Click on Cancel in Arrange Data to convert a new file again.\n", "red")
        else:
            self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("NetCDF file has not been saved. Click on Cancel in Arrange Data to convert a new file again.\n")
            self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("NetCDF file has not been saved. Click on Cancel in Arrange Data to convert a new file again.\n", "red")
