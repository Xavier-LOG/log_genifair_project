# Importation des fichiers




from modeleMainwindow import modeleMainwindow




# Importation des bibliothèques




import pandas as pd
import pyexcel_ods
import tkinter as tk
from tkinter import filedialog
from PyQt6.QtWidgets import QMdiSubWindow, QLabel





# Définition de la classe controleurToolbar




class controleurToolbar:
    
    
    dataframe: pd.DataFrame = pd.DataFrame()
    
    
    # Constructeur par défaut
    
    
    def __init__(self, vueToolbar):
        
        self.vueToolbar = vueToolbar
        
    
    # Définition des méthodes
    
    
    def file_clicked(self):
        
        # Affichage du menu contextuel de File à l'emplacement du coin inférieur gauche du bouton File. popup affiche le menu contextuel à une position spécifique sur l'écran. mapToGlobal convertit les coordonées locales du bouton File en coordonnées globales sur l'écran
        self.vueToolbar.toolbarwidget_file.popup(self.vueToolbar.toolbarwidget_file_button.mapToGlobal(self.vueToolbar.toolbarwidget_file_button.rect().bottomLeft()))


    def options_clicked(self):
        
        # Affichage du menu contextuel de Options à l'emplacement du coin inférieur gauche du bouton Options. popup affiche le menu contextuel à une position spécifique sur l'écran. mapToGlobal convertit les coordonées locales du bouton Options en coordonnées globales sur l'écran
        self.vueToolbar.toolbarwidget_options.popup(self.vueToolbar.toolbarwidget_options_button.mapToGlobal(self.vueToolbar.toolbarwidget_options_button.rect().bottomLeft()))


    def resolution_option(self):
        
        self.vueToolbar.mainwindow.setGeometry(50, 50, 1280, 768)


    def help_clicked(self):
        
        # Affichage du menu contextuel de Help à l'emplacement du coin inférieur gauche du bouton Help. popup affiche le menu contextuel à une position spécifique sur l'écran. mapToGlobal convertit les coordonées locales du bouton Help en coordonnées globales sur l'écran
        self.vueToolbar.toolbarwidget_help.popup(self.vueToolbar.toolbarwidget_help_button.mapToGlobal(self.vueToolbar.toolbarwidget_help_button.rect().bottomLeft()))


    def about_option(self):
        
        self.about_window = QMdiSubWindow()
        self.about_window.setWindowTitle("About")
        self.about_window.setFixedSize(400, 400)
        self.about_text = QLabel("Some Content", self.about_window)
        self.about_text.setWordWrap(True)
        self.about_text.setGeometry(10, 10, 390, 190)
        self.about_window.setWidget(self.about_text)
        self.about_window.move(400, 0)
        self.about_window.show()   
    
    
    # Définition des méthodes statiques
    

    @staticmethod    
    def import_option():
        
        # Création d'une fenêtre tkinter
        root = tk.Tk()
        # Fenêtre principale masquée
        root.withdraw()
        # Affichage de la boîte de dialogue pour sélectionner un fichier dans l'explorateur de fichiers
        file = filedialog.askopenfilename()
        # Si le fichier existe
        if file:
            # Si le fichier est au format .xlsx
            if file.endswith('.xlsx'):
                # Initialisation du dataframe (pandas remplit automatiquement les valeurs manquantes par NaN (donc même nombre de lignes dans le dataframe))
                controleurToolbar.dataframe = pd.read_excel(file)
            # Si le fichier est au format .csv
            elif file.endswith('.csv'):
                controleurToolbar.dataframe = pd.read_csv(file)
            # Si le fichier est au format .odf
            elif file.endswith('.odf'):
                # Utilisation de pyexcel_ods pour obtenir les données
                data = pyexcel_ods.get_data(file)
                # La première feuille de calcul du fichier est conservée
                first_spreadsheet = list(data.keys())[0]
                # Initialisation du dataframe
                controleurToolbar.dataframe = pd.DataFrame(data[first_spreadsheet])
            # Si le fichier est au format .txt
            elif file.endswith('.txt'):
                # Initialisation du dataframe (on suppose que les colonnes du fichier sont délimitées par des espaces, donc on utilise delim_whitespace)
                controleurToolbar.dataframe = pd.read_csv(file, delim_whitespace=True)
            # Si le fichier est au format .ods
            elif file.endswith('.ods'):
                # Initialisation du dataframe
                controleurToolbar.dataframe = pd.read_excel(file, engine='odf')
            # Sinon le format du fichier n'est pas le bon et le dataframe est vide
            else:
                modeleMainwindow.log("xlsx file format required.")
                controleurToolbar.dataframe = pd.DataFrame()
            # Si tous les noms de colonne du dataframe sont des chaînes de caractères
            if all(isinstance(column, str) for column in controleurToolbar.dataframe.columns) == True:   
                # Suppression des colonnes du dataframe dont le nom de colonne est dupliqué
                controleurToolbar.dataframe = controleurToolbar.dataframe.drop(columns = controleurToolbar.dataframe.columns[controleurToolbar.dataframe.columns.duplicated()]) 
                # Si les numéros de ligne et de colonne sont présents dans le dataframe
                if controleurToolbar.dataframe.columns[0] == 'Unnamed: 0' or controleurToolbar.dataframe.index[0] == 'Unnamed: 0':
                    # Suppression des numéros de ligne
                    controleurToolbar.dataframe = controleurToolbar.dataframe.iloc[:, 1:]
                    # Suppression des numéros de colonne
                    controleurToolbar.dataframe = controleurToolbar.dataframe.iloc[1:, :]
            # Sinon le dataframe est vide
            else:
                modeleMainwindow.log("Column name must be a string. Dataframe will be cleared.")
                controleurToolbar.dataframe = pd.DataFrame()
        # Sinon aucun fichier n'a été ouvert et le dataframe est vide
        else:
            modeleMainwindow.log("No file has been opened. Dataframe will be cleared.")
            controleurToolbar.dataframe = pd.DataFrame()




# Programme principal




if __name__ == '__main__':
    
    controleurToolbar.import_option()
