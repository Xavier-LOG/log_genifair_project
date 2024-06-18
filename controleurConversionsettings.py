# Importation des fichiers




from outilsProcessing import outilsProcessing




# Importations des bibliothèques




from PyQt6.QtWidgets import QFileDialog
import re
import os
import xarray as xr




# Définition de la classe controleurConversionsettings




class controleurConversionsettings:


    # Constructeur par défaut
        
    
    def __init__(self, vueconversionsettings):
        
        super().__init__()
        self.vueconversionsettings = vueconversionsettings
    
    
    # Définition des méthodes
    
    
    def convert(self):

        """_summary_
        Conversion de dataset xarray en NetCDF à partir du fichier importé et du catalogue choisi
        """

        # Ouverture d'une fenêtre permettant à l'utilisateur de choisir où et sous quel nom enregistrer le fichier NetCDF
        file_path, _ = QFileDialog.getSaveFileName(self.vueconversionsettings, "Save NetCDF File", self.vueconversionsettings.vueconversion.vuemainwindow.vuecatalog.modelecatalog.path_list_files[1][0][:self.vueconversionsettings.vueconversion.vuemainwindow.vuecatalog.modelecatalog.path_list_files[1][0].find(".")] + ".nc", "NetCDF File (*.nc)")
        # Si le chemin du fichier existe
        if file_path:
            # Si le chemin du fichier se termine par nc
            if file_path.endswith(".nc"):
                # Parcours de chaque dataframe de fichier importé dans la liste
                for i in range(0, len(self.vueconversionsettings.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list)):
                    controleurlogs = self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs
                    dataframe = self.vueconversionsettings.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list[i]
                    catalog_path = self.vueconversionsettings.vueconversion.vuemainwindow.vuecatalog.modelecatalog.path_list_files[0]
                    # Initialisation du dataset xarray à partir de l'outil de traitement
                    xarray_dataset = outilsProcessing(controleurlogs, dataframe, xr.Dataset(), catalog_path)
                    # Création du dataset xarray
                    xarray_dataset.create_xarray_dataset()
                    # Si le dataset xarray existe
                    if xarray_dataset.get_xarray_dataset():
                        # Si le chemin du répertoire ne contient pas d'accents
                        # Recherche dans le chemin du répertoire du fichier tous les caractères qui ne sont pas de la norme ASCII
                        if bool(re.search(r'[^\x00-\x7F]', str(os.path.dirname(str(file_path))))) == False:
                            # Conversion du dataset xarray au netcdf et sauvegarde dans le chemin du fichier
                            xarray_dataset.get_xarray_dataset().to_netcdf(str(file_path[:file_path.find(".")]) + "_" + str(i + 1) + ".nc")
                            if i == len(self.vueconversionsettings.vueconversion.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list) - 1:
                                # Affichage du dernier dataset xarray
                                self.vueconversionsettings.vueconversion.vuenetcdfviewer.controleurnetcdfviewer.load_netcdf(xarray_dataset)
                                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Netcdf file has been saved.\n")
                                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Netcdf file has been saved.\n", "green")
                        else:
                            self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("NetCDF file has not been saved. The file path contains accents.\n")
                            self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("NetCDF file has not been saved. The file path contains accents.\n", "red")
                    else:
                        self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Empty dataframe.\n")
                        self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Empty dataframe.\n", "red")
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Click on Cancel in File Settings or click on Cancel in Arrange Data to convert a new file again.\n")
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Click on Cancel in File Settings or click on Cancel in Arrange Data to convert a new file again.\n", "green")
            else:
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect file format. Click on Cancel in File Settings or click on Cancel in Arrange Data to convert a new file again.\n")
                self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect file format. Click on Cancel in File Settings or click on Cancel in Arrange Data to convert a new file again.\n", "red")
        else:
            self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_log("NetCDF file has not been saved. Click on Cancel in File Settings or click on Cancel in Arrange Data to convert a new file again.\n")
            self.vueconversionsettings.vueconversion.vuemainwindow.vuelogs.controleurlogs.add_colored_log("NetCDF file has not been saved. Click on Cancel in File Settings or click on Cancel in Arrange Data to convert a new file again.\n", "red")
