# Importation des bibliothèques




import xarray as xr
import pandas as pd
import pyexcel_ods
import numpy as np
import tkinter as tk
from tkinter import filedialog
from datetime import datetime, date, time
import re
import matplotlib.pyplot as plt




# Définitions des fonctions




def create_catalog():
    # Initialisation d'un catalogue sous forme d'une liste contenant une liste de noms possibles pour la variable datetime du fichier netCDF et une liste de données temporelles
    datetime_catalog = [['datetime', 'date', 'time', 'temps', 'heure', 'hour', 'minute', 'min', 'seconde', 'sec', 'YYYY/MM/DD', 'DD/MM/YYYY', 'HH:MM:SS']]
    # Retourne le catalogue
    return datetime_catalog


def open_file(error_log: list[str]):
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
            dataframe = pd.read_excel(file)
        # Si le fichier est au format .csv
        elif file.endswith('.csv'):
            dataframe = pd.read_csv(file)
        # Si le fichier est au format .odf
        elif file.endswith('.odf'):
            # Utilisation de pyexcel_ods pour obtenir les données
            data = pyexcel_ods.get_data(file)
            # La première feuille de calcul du fichier est conservée
            first_spreadsheet = list(data.keys())[0]
            # Initialisation du dataframe
            dataframe = pd.DataFrame(data[first_spreadsheet])
        # Si le fichier est au format .txt
        elif file.endswith('.txt'):
            # Initialisation du dataframe (on suppose que les colonnes du fichier sont délimitées par des espaces, donc on utilise delim_whitespace)
            dataframe = pd.read_csv(file, delim_whitespace=True)
        # Si le fichier est au format .ods
        elif file.endswith('.ods'):
            # Initialisation du dataframe
            dataframe = pd.read_excel(file, engine='odf')
        # Sinon le format du fichier n'est pas le bon et le dataframe est vide
        else:
            error_log.append("xlsx file format required.")
            dataframe = pd.DataFrame()
        # Si tous les noms de colonne du dataframe sont des chaînes de caractères
        if all(isinstance(column, str) for column in dataframe.columns) == True:   
            # Suppression des colonnes du dataframe dont le nom de colonne est dupliqué
            dataframe = dataframe.drop(columns=dataframe.columns[dataframe.columns.duplicated()]) 
            # Si les numéros de ligne et de colonne sont présents dans le dataframe
            if dataframe.columns[0] == 'Unnamed: 0' or dataframe.index[0] == 'Unnamed: 0':
                # Suppression des numéros de ligne
                dataframe = dataframe.iloc[:, 1:]
                # Suppression des numéros de colonne
                dataframe = dataframe.iloc[1:, :]
        # Sinon le dataframe est vide
        else:
            error_log.append("Column name must be a string. Dataframe will be cleared.")
            dataframe = pd.DataFrame()
    # Sinon aucun fichier n'a été ouvert et le dataframe est vide
    else:
        error_log.append("No file has been opened. Dataframe will be cleared.")
        dataframe = pd.DataFrame()
    # Retourne les logs d'erreur et le dataframe
    return error_log, dataframe


def create_xarray_dataset(dataframe: pd.DataFrame):
    # Initialisation du dataset
    xarray_dataset = xr.Dataset(
        # Variables
        data_vars=
        {
            # Les variables correspondent aux noms de colonne du tableau du fichier .xlsx
            'id_station' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'mission' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'num_station' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'datetime' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'latitude' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'longitude' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'depth' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'temperature' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'salinity' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'turbidity' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'chlorophyll-a' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'suspended_particulate_matter' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'particulate_organic_carbon' : (['lenstation'], np.zeros(dataframe.shape[0])),
            'dissolved_organic_carbon' : (['lenstation'], np.zeros(dataframe.shape[0])),
        },
        # Dimensions
        coords=
        {
            # La dimension correspond au nombre de lignes du tableau du fichier .xlsx
            'lenstation' : np.arange(dataframe.shape[0]),
        },
        # Attributs globaux
        attrs=
        {
            'title': 'CF File version 1',
        }
    )
    
    # Ajout des attributs de paramètres
    xarray_dataset['id_station'].attrs['long_name'] = 'id_station'
    xarray_dataset['id_station'].attrs['standard_name'] = 'id_station'
    xarray_dataset['id_station'].attrs['dtype'] = 'object'
    
    xarray_dataset['mission'].attrs['long_name'] = 'mission'
    xarray_dataset['mission'].attrs['standard_name'] = 'mission'
    xarray_dataset['mission'].attrs['dtype'] = 'object'
    
    xarray_dataset['num_station'].attrs['long_name'] = 'num_station'
    xarray_dataset['num_station'].attrs['standard_name'] = 'numero_station'
    xarray_dataset['num_station'].attrs['dtype'] = 'object'
    
    xarray_dataset['datetime'].attrs['long_name'] = 'datetime'
    xarray_dataset['datetime'].attrs['standard_name'] = 'datetime'
    xarray_dataset['datetime'].attrs['dtype'] = 'object'
    
    xarray_dataset['latitude'].attrs['long_name'] = 'latitude'
    xarray_dataset['latitude'].attrs['standard_name'] = 'lat'
    xarray_dataset['latitude'].attrs['dtype'] = 'float64'
    xarray_dataset['latitude'].attrs['units'] = 'Meters'
    
    xarray_dataset['longitude'].attrs['long_name'] = 'longitude'
    xarray_dataset['longitude'].attrs['standard_name'] = 'lon'
    xarray_dataset['longitude'].attrs['dtype'] = 'float64'
    xarray_dataset['longitude'].attrs['units'] = 'Meters'
    
    xarray_dataset['depth'].attrs['long_name'] = 'depth'
    xarray_dataset['depth'].attrs['standard_name'] = 'profondeur'
    xarray_dataset['depth'].attrs['dtype'] = 'float64'
    xarray_dataset['depth'].attrs['units'] = 'Meters'
    
    xarray_dataset['temperature'].attrs['long_name'] = 'temperature'
    xarray_dataset['temperature'].attrs['standard_name'] = 'temp'
    xarray_dataset['temperature'].attrs['dtype'] = 'float64'
    xarray_dataset['temperature'].attrs['units'] = 'Celsius'
    
    xarray_dataset['salinity'].attrs['long_name'] = 'salinity'
    xarray_dataset['salinity'].attrs['standard_name'] = 'salinity'
    xarray_dataset['salinity'].attrs['dtype'] = 'float64'
    
    xarray_dataset['turbidity'].attrs['long_name'] = 'turbidity'
    xarray_dataset['turbidity'].attrs['standard_name'] = 'tur'
    xarray_dataset['turbidity'].attrs['dtype'] = 'float64'
    xarray_dataset['turbidity'].attrs['units'] = 'NTU'
    
    xarray_dataset['chlorophyll-a'].attrs['long_name'] = 'chlorophyll-a'
    xarray_dataset['chlorophyll-a'].attrs['standard_name'] = 'chla(µg/l)'
    xarray_dataset['chlorophyll-a'].attrs['dtype'] = 'float64'
    xarray_dataset['chlorophyll-a'].attrs['units'] = 'mg/L'
    
    xarray_dataset['suspended_particulate_matter'].attrs['long_name'] = 'suspended_particulate_matter'
    xarray_dataset['suspended_particulate_matter'].attrs['standard_name'] = 'spm'
    xarray_dataset['suspended_particulate_matter'].attrs['dtype'] = 'float64'
    xarray_dataset['suspended_particulate_matter'].attrs['units'] = 'mg/L'
    
    xarray_dataset['particulate_organic_carbon'].attrs['long_name'] = 'particulate_organic_carbon'
    xarray_dataset['particulate_organic_carbon'].attrs['standard_name'] = 'poc'
    xarray_dataset['particulate_organic_carbon'].attrs['dtype'] = 'float64'
    xarray_dataset['particulate_organic_carbon'].attrs['units'] = 'mg/L'
    
    xarray_dataset['dissolved_organic_carbon'].attrs['long_name'] = 'dissolved_organic_carbon'
    xarray_dataset['dissolved_organic_carbon'].attrs['standard_name'] = 'doc'
    xarray_dataset['dissolved_organic_carbon'].attrs['dtype'] = 'float64'
    
    # Retourne le dataset xarray
    return xarray_dataset


def check_dataframe_integrity(error_log: list[str], dataframe: pd.DataFrame, xarray_dataset: xr.Dataset, datetime_catalog: list[list]):
    # Si le dataframe est vide
    if dataframe.empty:
        error_log.append("Empty dataframe.")
        dataframe = pd.DataFrame()
    # Sinon
    else:
        # Parcours de chaque colonne du dataframe
        for column in dataframe.columns:
            # Si le nom de la colonne du dataframe en minuscule sans espace blanc n'est pas dans la première liste du catalogue
            if column.replace(' ', '').lower() not in datetime_catalog[0]:
                # Parcours de chaque clé du dataset xarray
                for key in list(xarray_dataset.data_vars.keys()):
                    # Parcours de chaque mot de la liste des noms possibles pour chaque clé
                    for substring in [xarray_dataset[key].attrs['long_name'], xarray_dataset[key].attrs['standard_name']]:
                        # Si le mot en minuscule est contenu dans le nom de la colonne du dataframe en minuscule sans espace blanc
                        if substring.lower() in column.replace(' ', '').lower():
                            # Si les données de la colonne du dataframe sont du même type que celui des données du fichier netCDF ou si une colonne du dataframe est vide
                            if dataframe[column].dtype == xarray_dataset[key].attrs['dtype'] or dataframe[column].isna().all() == True:
                                # Si la liste de données de la colonne du dataframe contient au minimum 10 données
                                if len(dataframe[column].iloc[:].tolist()) >= 10:
                                    # Si la clé est latitude
                                    if key == 'latitude':
                                        # Si les données de la colonne du dataframe sont des valeurs de latitude
                                        if all(dataframe[column].between(-90.0, 90.0)):
                                            # Ajout des données de la colonne du dataframe dans le tableau de données associé à la clé
                                            xarray_dataset[key].values = np.array(dataframe[column].iloc[:].tolist())
                                        # Sinon les données de la colonne du dataframe ne sont pas des valeurs de latitude
                                        else:
                                            error_log.append("Latitude values are not between -90 and 90.")
                                    # Si la clé est longitude
                                    elif key == 'longitude':
                                        # Si les données de la colonne du dataframe sont des valeurs de longitude
                                        if all(dataframe[column].between(-180.0, 180.0)):
                                            # Ajout des données de la colonne du dataframe dans le tableau de données associé à la clé
                                            xarray_dataset[key].values = np.array(dataframe[column].iloc[:].tolist())
                                        # Sinon les données de la colonne du dataframe ne sont pas des valeurs de longitude
                                        else:
                                            error_log.append("Longitude values are not between -180 and 180.")
                                    # Sinon la clé est une autre clé
                                    else:
                                        # Ajout des données de la colonne du dataframe dans le tableau de données associé à la clé
                                        xarray_dataset[key].values = np.array(dataframe[column].iloc[:].tolist())
                                # Sinon
                                else:
                                    error_log.append("Less than 10 data are present in column " + column + " . Data will be not selected.")
                            # Sinon
                            else:
                                print(column, substring)
                                error_log.append("Data type in column " + column + " : " + str(dataframe[column].dtype) + " does not match the type of the variable : " + key + " : " + xarray_dataset[key].attrs['dtype'] + " . Data will be not selected.")
    # Retourne les logs d'erreur et le dataset xarray actualisé
    return error_log, xarray_dataset


def check_datetime_format(error_log: list[str], dataframe: pd.DataFrame, xarray_dataset: xr.Dataset, datetime_catalog: list[list]):
    # Si le dataframe est vide
    if dataframe.empty:
        error_log.append("Empty dataframe.")
        dataframe = pd.DataFrame()
        # Retourne les logs d'erreur et le dataset xarray
        return error_log, xarray_dataset
    # Sinon
    else:
        # Parcours de chaque colonne du dataframe
        for column in dataframe.columns:
            # Parcours de chaque élément de la première liste du catalogue
            for element in datetime_catalog[0]:
                # Si l'élément du catalogue est contenu dans le nom de la colonne du dataframe en minuscule sans espace blanc et si le catalogue ne contient pas plus de 3 listes
                if element in column.replace(' ', '').lower() and len(datetime_catalog) < 3:
                    # Si la liste de données de la colonne du dataframe contient au minimum 10 données
                    if len(dataframe[column].iloc[:].tolist()) >= 10:
                        # Ajout des données de la colonne du dataframe dans le catalogue
                        datetime_catalog.append(dataframe[column].iloc[:].tolist())
                    # Sinon
                    else:
                        error_log.append("Less than 10 data are present in column " + column + " . Data will be not selected.")
        print(datetime_catalog)
        # Si le catalogue contient une liste de noms possibles pour la variable datetime et une liste de données temporelles
        if len(datetime_catalog) == 2:
            # Parcours de la première donnée temporelle jusqu'à la dernière dans la liste
            for i in range(0, len(datetime_catalog[1])):
                # Si la donnée temporelle est au format timestamp
                if isinstance(datetime_catalog[1][i], pd.Timestamp):
                    # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                    datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))
                # Si la donnée temporelle est au format datetime
                elif isinstance(datetime_catalog[1][i], datetime):
                    # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                    datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))   
                # Si la donnée temporelle est au format date
                elif isinstance(datetime_catalog[1][i], date):
                    # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                    datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%Y-%m-%d"))
                # Si la donnée temporelle est au format time
                elif isinstance(datetime_catalog[1][i], time):
                    # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                    datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%H:%M:%S"))    
                # Si la donnée temporelle est une chaîne de caractères
                elif isinstance(datetime_catalog[1][i], str):
                    # Si la donnée temporelle n'est pas au format 'YYYY-MM-DD HH:MM:SS', 'YYYY-MM-DD' ou 'HH:MM:SS'
                    if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1]) (?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[1][i])) == False and bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', datetime_catalog[1][i])) == False and bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[1][i])) == False:
                        # La donnée temporelle est nulle
                        datetime_catalog[1][i] = str('')
                # Sinon le type de donnée n'est pas correct
                else:
                    error_log.append("Incorrect data type for " + str(datetime_catalog[1][i]) + " : " + str(type(datetime_catalog[1][i])) + " . Data will be cleared.")
                    # La donnée temporelle est nulle
                    datetime_catalog[1][i] = str('')    
        # Si le catalogue contient une liste de noms possibles pour la variable datetime et 2 listes de données temporelles
        elif len(datetime_catalog) == 3:
            # Parcours de la première donnée temporelle jusqu'à la dernière dans la liste
            for i in range(0, len(datetime_catalog[1])):
                # Si la donnée temporelle est au format timestamp
                if isinstance(datetime_catalog[1][i], pd.Timestamp):
                    # Si la donnée temporelle est au format 'YYYY-MM-DD'
                    if str(datetime_catalog[1][i].strftime("%H:%M:%S")) == '00:00:00':
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                        datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%Y-%m-%d"))
                        # Si la donnée temporelle de la deuxième liste est au format time
                        if isinstance(datetime_catalog[2][i], time):
                            # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                            datetime_catalog[2][i] = str(datetime_catalog[2][i].strftime("%H:%M:%S"))   
                            # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            datetime_catalog[1][i] = datetime_catalog[1][i] + " " + datetime_catalog[2][i]
                        # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                        elif isinstance(datetime_catalog[2][i], str):
                            # Si la donnée temporelle est au format 'HH:MM:SS'
                            if bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[2][i])) == True:
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                datetime_catalog[1][i] = datetime_catalog[1][i] + " " + datetime_catalog[2][i]
                    # Sinon la donnée temporelle est au format 'YYYY-MM-DD HH:MM:SS'
                    else:
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                        datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))
                # Si la donnée temporelle est au format datetime
                elif isinstance(datetime_catalog[1][i], datetime):
                    # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                    datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))
                # Si la donnée temporelle est au format date
                elif isinstance(datetime_catalog[1][i], date):
                    # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                    datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%Y-%m-%d"))
                    # Si la donnée temporelle de la deuxième liste est au format time
                    if isinstance(datetime_catalog[2][i], time):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                        datetime_catalog[2][i] = str(datetime_catalog[2][i].strftime("%H:%M:%S"))   
                        # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                        datetime_catalog[1][i] = datetime_catalog[1][i] + " " + datetime_catalog[2][i]
                    # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                    elif isinstance(datetime_catalog[2][i], str):
                        # Si la donnée temporelle est au format 'HH:MM:SS'
                        if bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[2][i])) == True:
                            # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            datetime_catalog[1][i] = datetime_catalog[1][i] + " " + datetime_catalog[2][i]
                # Si la donnée temporelle est au format time
                elif isinstance(datetime_catalog[1][i], time):
                    # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                    datetime_catalog[1][i] = str(datetime_catalog[1][i].strftime("%H:%M:%S"))
                    # Si la donnée temporelle de la deuxième liste est au format date
                    if isinstance(datetime_catalog[2][i], date):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                        datetime_catalog[2][i] = str(datetime_catalog[2][i].strftime("%Y-%m-%d"))   
                        # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                        datetime_catalog[1][i] = datetime_catalog[2][i] + " " + datetime_catalog[1][i]
                    # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                    elif isinstance(datetime_catalog[2][i], str):
                        # Si la donnée temporelle est au format 'YYYY-MM-DD'
                        if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', datetime_catalog[2][i])) == True:
                            # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            datetime_catalog[1][i] = datetime_catalog[2][i] + " " + datetime_catalog[1][i]
                # Si la donnée temporelle est une chaîne de caractères
                elif isinstance(datetime_catalog[1][i], str):                
                    # Si la donnée temporelle est une chaîne de caractères au format 'YYYY-MM-DD'    
                    if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', datetime_catalog[1][i])) == True:
                        # Si la donnée temporelle de la deuxième liste est au format time
                        if isinstance(datetime_catalog[2][i], time):
                            # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                            datetime_catalog[2][i] = str(datetime_catalog[2][i].strftime("%H:%M:%S"))   
                            # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            datetime_catalog[1][i] = datetime_catalog[1][i] + " " + datetime_catalog[2][i]
                        # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                        elif isinstance(datetime_catalog[2][i], str):
                            # Si la donnée temporelle de la deuxième liste est une chaîne de caractères au format 'HH:MM:SS'
                            if bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[2][i])) == True:
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                datetime_catalog[1][i] = datetime_catalog[1][i] + " " + datetime_catalog[2][i]
                    # Si la donnée temporelle est une chaîne de caractères au format 'HH:MM:SS'    
                    elif bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[1][i])) == True:
                        # Si la donnée temporelle de la deuxième liste est au format date
                        if isinstance(datetime_catalog[2][i], date):
                            # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                            datetime_catalog[2][i] = str(datetime_catalog[2][i].strftime("%Y-%m-%d"))   
                            # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            datetime_catalog[1][i] = datetime_catalog[2][i] + " " + datetime_catalog[1][i]
                        # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                        elif isinstance(datetime_catalog[2][i], str):
                            # Si la donnée temporelle de la deuxième liste est une chaîne de caractères au format 'YYYY-MM-DD'
                            if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', datetime_catalog[2][i])) == True:
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                datetime_catalog[1][i] = datetime_catalog[2][i] + " " + datetime_catalog[1][i]
                    # Si la donnée temporelle est une chaîne de caractères qui n'est pas au format 'YYYY-MM-DD HH:MM:SS', 'YYYY-MM-DD' ou 'HH:MM:SS'
                    elif bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1]) (?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[1][i])) == False and bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', datetime_catalog[1][i])) == False and bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', datetime_catalog[1][i])) == False:
                        error_log.append("Date format not recognized for " + str(datetime_catalog[1][i]) + " . Data will be cleared.")
                        # La donnée temporelle est nulle
                        datetime_catalog[1][i] = str('')
                # Sinon le type de donnée n'est pas correct
                else:
                    error_log.append("Incorrect data type for " + str(datetime_catalog[1][i]) + " : " + str(type(datetime_catalog[1][i])) + " . Data will be cleared.")
                    # La donnée temporelle est nulle
                    datetime_catalog[1][i] = str('') 
            # Technique de slicing pour retirer toutes les listes de données temporelles sauf la première
            datetime_catalog = datetime_catalog[:-(len(datetime_catalog)-2)]
        # Sinon
        else:
            # Retourne les logs d'erreurs et le dataset xarray
            return error_log, xarray_dataset
        # Ajout des données temporelles de la liste dans le tableau de données associé à la clé
        xarray_dataset['datetime'].values = np.array(datetime_catalog[1])
        # Retourne les logs d'erreur et le dataset xarray actualisé
        return error_log, xarray_dataset


def adapt_xarray_dataset(xarray_dataset: xr.Dataset):
    # Parcours de chaque clé du dataset xarray
    for key in list(xarray_dataset.data_vars.keys()):
        # Si le tableau de données de la clé est vide
        if np.all(xarray_dataset[key].values == 0) or np.all(xarray_dataset[key].values != xarray_dataset[key].values):
            # Suppression des attributs de la variable
            xarray_dataset[key].attrs.clear()
            # Suppression de la variable
            del xarray_dataset[key]
    # Retourne le dataset xarray actualisé
    return xarray_dataset




# Programme principal




if __name__ == "__main__":
    datetime_catalog = create_catalog()
    error_log = []
    error_log, dataframe = open_file(error_log)
    xarray_dataset = create_xarray_dataset(dataframe)
    error_log, xarray_dataset = check_dataframe_integrity(error_log, dataframe, xarray_dataset, datetime_catalog)
    error_log, xarray_dataset = check_datetime_format(error_log, dataframe, xarray_dataset, datetime_catalog)
    xarray_dataset = adapt_xarray_dataset(xarray_dataset)
    print(xarray_dataset, "\n", error_log)
    