# Importation des fichiers




from vueDatabase import vueDatabase




# Importation des bibliothèques




import pandas as pd
import os
import pyexcel_ods
from PyQt6.QtWidgets import QMdiSubWindow, QFileDialog, QLabel
from PyQt6.QtCore import pyqtSignal, QObject




# Définition de la classe controleurToolbar




class controleurToolbar(QObject):


    signal = pyqtSignal(list)

    
    # Constructeur par défaut

    
    def __init__(self, vuetoolbar):
        
        super().__init__()        
        self.vuetoolbar = vuetoolbar
        self.file_list = []
        self.dataframe_list = []
        self.row_number = None
        self.vuedatabase = None
        self.about_window = None
        
        
    # Définition des méthodes
    
    
    def data_collect(self, obj):
        
        """_summary_
        Collection des données importées
        """
        
        # Parcours de chaque dataframe de la liste
        for i in range(0, len(obj[1])):
            # Vérification de chaque dataframe
            self.import_check(obj[0], obj[1][i])
        # Validation de l'importation
        self.import_validation()
    

    def import_check(self, file_path, dataframe):
        
        """_summary_
        Vérification de l'importation et suppression des colonnes du dataframe dont le nom de colonne est duppliqué
        """
        
        # Si tous les noms de colonne du dataframe sont des chaînes de caractères
        if all(isinstance(column, str) for column in dataframe.columns) == True: 
            # Suppression des colonnes du dataframe dont le nom de colonne est duppliqué
            dataframe = dataframe.drop(columns = dataframe.columns[dataframe.columns.duplicated()])
            self.file_list.append(str(file_path))
            self.dataframe_list.append(dataframe)
        # Sinon le chemin du fichier et le dataframe sont ignorés
        else:
            self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_log("Column name must be a string. Dataframe will be cleared.\n")
            self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Column name must be a string. Dataframe will be cleared.\n", "red")


    def import_validation(self):

        """_summary_
        Validation de l'importation des données
        """
        
        # vueToolbar est instanciée avant vueCatalog et vueConversion. Donc émission d'un signal.
        # Emission d'un signal sous forme de liste vers controleurCatalog en premier (pour remplacer la deuxième valeur de path_list_files de modeleCatalog par self.file_list), 
        # puis vers controleurFileviewer en deuxième (pour afficher la liste des fichiers importés avec la deuxième valeur de path_list_files désormais modifiée), 
        # puis vers controleurCatalogsettings en troisième (pour remplacer dataframe de controleurCatalogsettings par la première valeur de self.dataframe_list)
        # puis vers controleurDataframeviewer en quatrième (pour afficher uniquement la première valeur de self.dataframe_list)
        # puis vers controleurConversionsettings en dernier (pour convertir tous les dataframes pandas en fichier netCDF)
        self.signal.emit([self.file_list, self.dataframe_list])
        self.vuetoolbar.menu_file_button.setEnabled(False)
        self.vuetoolbar.vuemainwindow.vuecatalog.vuecatalogsettings.button.setEnabled(True)
        self.vuetoolbar.vuemainwindow.vuecatalog.groupbox_confirm_button.setEnabled(True)
        self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_log("Files have been imported.\n")
        self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Files have been imported.\n", "green")

    
    def import_file_option(self):
        
        """_summary_
        Importation des données de fichier au format xlsx, txt, csv, ods, odf
        """
        
        file_dialog = QFileDialog(self.vuetoolbar)
        # Affichage de la boîte de dialogue pour sélectionner un fichier dans l'explorateur de fichiers
        file_path, _ = file_dialog.getOpenFileName(self.vuetoolbar, "Open File", "", "(*.xlsx);;(*.csv);;(*.odf);;(*.txt);;(*.ods)")        
        # Si le chemin du fichier existe
        if file_path:
            # Si le fichier est au format .xlsx
            if file_path.endswith('.xlsx'):
                # Initialisation du dataframe (pandas remplit automatiquement les valeurs manquantes par NaN (donc même nombre de lignes dans le dataframe))
                dataframe = pd.read_excel(file_path, nrows = self.row_number)
            # Si le fichier est au format .csv
            elif file_path.endswith('.csv'):
                dataframe = pd.read_csv(file_path, nrows = self.row_number)
            # Si le fichier est au format .odf
            elif file_path.endswith('.odf'):
                # Utilisation de pyexcel_ods pour obtenir les données
                data = pyexcel_ods.get_data(file_path)
                # La première feuille de calcul du fichier est conservée
                first_spreadsheet = list(data.keys())[0]
                # Initialisation du dataframe
                dataframe = pd.DataFrame(data[first_spreadsheet])
            # Si le fichier est au format .txt
            elif file_path.endswith('.txt'):
                # Initialisation du dataframe (on suppose que les colonnes du fichier sont délimitées par des espaces, donc on utilise delim_whitespace)
                dataframe = pd.read_csv(file_path, nrows = self.row_number, delimiter = '\t')
                file_path = file_path[:-4] + '.xlsx'
                # Ecriture dans un fichier Excel
                dataframe.to_excel(file_path)
                # Lecture du fichier Excel
                dataframe = pd.read_excel(file_path)
            # Si le fichier est au format .ods
            elif file_path.endswith('.ods'):
                # Initialisation du dataframe
                dataframe = pd.read_excel(file_path, engine='odf')
            # Sinon le format du fichier n'est pas le bon et le dataframe est vide
            else:
                dataframe = pd.DataFrame()
                self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown file format.\n")
                self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown file format.\n", "red")
            self.import_check(file_path, dataframe)
            self.import_validation()
        # Sinon aucun fichier n'a été ouvert
        else:
            self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_log("No file has been opened. Dataframe will be cleared.\n")
            self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_colored_log("No file has been opened. Dataframe will be cleared.\n", "red")
 
    
    def import_folder_option(self):
        
        directory_dialog = QFileDialog(self.vuetoolbar)
        # Variable pour le chemin du dossier
        directory = directory_dialog.getExistingDirectory(self.vuetoolbar, "Select a folder")
        # Variable pour vérifier si tous les fichiers du répertoire sont au même format (xlsx, csv, odf, txt, ods)
        xlsx = 0
        csv = 0
        odf = 0
        txt = 0
        ods = 0
        # Si le dossier existe
        if directory:
            # Pour chaque nom de fichier dans la liste des noms de fichier du dossier
            for file_name in os.listdir(directory):
                if file_name.endswith(".xlsx"):
                    xlsx += 1
                elif file_name.endswith(".csv"):
                    csv += 1
                elif file_name.endswith(".ods"):
                    odf += 1
                elif file_name.endswith(".txt"):
                    txt += 1
                elif file_name.endswith(".odf"):
                    ods += 1
            if xlsx == len(os.listdir(directory)):
                # Pour chaque nom de fichier dans la liste des noms de fichier du dossier
                for file_name in os.listdir(directory):
                    # Concaténation du chemin du dossier avec le nom du fichier
                    file_path = os.path.join(directory, file_name)
                    dataframe = pd.read_excel(file_path, nrows = self.row_number)
                    self.import_check(file_path, dataframe)
                self.import_validation()
            elif csv == len(os.listdir(directory)):
                # Pour chaque nom de fichier dans la liste des noms de fichier du dossier
                for file_name in os.listdir(directory):
                    # Concaténation du chemin du dossier avec le nom du fichier
                    file_path = os.path.join(directory, file_name)
                    dataframe = pd.read_csv(file_path, nrows = self.row_number)
                    self.import_check(file_path, dataframe)
                self.import_validation()
            elif odf == len(os.listdir(directory)):
                # Pour chaque nom de fichier dans la liste des noms de fichier du dossier
                for file_name in os.listdir(directory):
                    # Concaténation du chemin du dossier avec le nom du fichier
                    file_path = os.path.join(directory, file_name)
                    # Utilisation de pyexcel_ods pour obtenir les données
                    data = pyexcel_ods.get_data(file_path)
                    # La première feuille de calcul du fichier est conservée
                    first_spreadsheet = list(data.keys())[0]
                    dataframe = pd.DataFrame(data[first_spreadsheet])
                    self.import_check(file_path, dataframe)
                self.import_validation()
            elif txt == len(os.listdir(directory)):
                # Pour chaque nom de fichier dans la liste des noms de fichier du dossier
                for file_name in os.listdir(directory):
                    # Concaténation du chemin du dossier avec le nom du fichier
                    file_path = os.path.join(directory, file_name)
                    dataframe = pd.read_csv(file_path, nrows = self.row_number, delimiter = '\t')
                    file = file[:-4] + '.xlsx'
                    # Ecriture dans un fichier Excel
                    dataframe.to_excel(file_path)
                    # Lecture du fichier Excel
                    dataframe = pd.read_excel(file_path)
                    self.import_check(file_path, dataframe)
                self.import_validation()
            elif ods == len(os.listdir(directory)):
                # Pour chaque nom de fichier dans la liste des noms de fichier du dossier
                for file_name in os.listdir(directory):
                    # Concaténation du chemin du dossier avec le nom du fichier
                    file_path = os.path.join(directory, file_name)
                    dataframe = pd.read_excel(file_path, engine='odf')
                    self.import_check(file_path, dataframe)
                self.import_validation()
            else:
                self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_log("The folder to be imported must contain the same file types.\n")
                self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The folder to be imported must contain the same file types.\n", "red")    
        else:
            self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_log("No folder has been opened. Dataframe will be cleared.\n")
            self.vuetoolbar.vuemainwindow.vuelogs.controleurlogs.add_colored_log("No folder has been opened. Dataframe will be cleared.\n", "red")
    
    
    def import_data_option(self):
    
        """_summary_
        Affichage de la vue pour la base de données et connexion
        """
        
        self.vuedatabase = vueDatabase()
        self.vuedatabase.show()
        self.vuedatabase.controleurdatabase.signal.connect(self.data_collect)
    
    
    def resolution_option(self):

        """_summary_
        Changement de la résolution de la fenêtre principale
        """
                    
        self.vuetoolbar.vuemainwindow.setGeometry(50, 50, 1280, 768)


    def about_option(self):
        
        """_summary_
        Affichage de la fenêtre A Propos
        """
        
        self.about_window = QMdiSubWindow()
        self.about_window.setWindowTitle("About")
        self.about_window.setFixedSize(400, 400)
        
        self.about_text = QLabel("This software was designed for the Laboratoire d'Océanologie et de Géosciences de Wimereux to arrange and process NetCDF data as part of the GENIFAIR (GENeration d'outils Informatiques destinés à la FAIRisation des données) project funded by the SFR Campus de la Mer. For more information on how to use it, please consult the user manual or visit the Github page.", self.about_window)
        # Activation du retour à la ligne
        self.about_text.setWordWrap(True)
        
        self.about_window.setWidget(self.about_text)
        self.about_window.move(400, 0)
        self.about_window.show()
