# Importation des fichiers




from modeleMainwindow import modeleMainwindow
from controleurToolbar import controleurToolbar




# Importation des bibliothèques




from typing_extensions import Self
import xarray as xr
import pandas as pd
import numpy as np
from datetime import datetime, date, time
import re
import json




# Définition de la classe modeleNetCDF




class modeleNetCDF :
    
    
    # Initialisation d'un catalogue sous forme d'une liste contenant une liste de noms possibles pour la variable datetime du fichier netCDF et une liste de données temporelles
    datetime_catalog: list[list] = [['datetime', 'date', 'time', 'temps', 'heure', 'hour', 'minute', 'min', 'seconde', 'sec', 'YYYY/MM/DD', 'DD/MM/YYYY', 'HH:MM:SS']]
    
    
    # Constructeur par défaut
    
    
    def __init__(self: Self, dataframe: pd.DataFrame, xarray_dataset: xr.Dataset):
        
        self.dataframe: pd.DataFrame = dataframe
        self.xarray_dataset: xr.Dataset = xarray_dataset
    
    
    # Définition des méthodes
    
    
    def check_dataframe_integrity(self: Self):
        
        # Si le dataframe est vide
        if self.dataframe.empty:
            modeleMainwindow.log("Empty dataframe.")
            self.dataframe = pd.DataFrame()
        # Sinon
        else:
            # Parcours de chaque colonne du dataframe
            for column in self.dataframe.columns:
                # Si le nom de la colonne du dataframe en minuscule sans espace blanc n'est pas dans la première liste du catalogue
                if column.replace(' ', '').lower() not in modeleNetCDF.datetime_catalog[0]:
                    # Parcours de chaque clé du dataset xarray
                    for key in list(self.xarray_dataset.data_vars.keys()):
                        # Parcours de chaque mot de la liste des noms possibles pour chaque clé
                        for substring in [self.xarray_dataset[key].attrs['long_name'], self.xarray_dataset[key].attrs['standard_name']]:
                            # Si le mot en minuscule est contenu dans le nom de la colonne du dataframe en minuscule sans espace blanc
                            if substring.lower() in column.replace(' ', '').lower():
                                # Si les données de la colonne du dataframe sont du même type que celui des données du fichier netCDF ou si une colonne du dataframe est vide
                                if self.dataframe[column].dtype == self.xarray_dataset[key].attrs['dtype'] or self.dataframe[column].isna().all() == True:
                                    # Si la liste de données de la colonne du dataframe contient au minimum 10 données
                                    if len(self.dataframe[column].iloc[:].tolist()) >= 10:
                                        # Si la clé est latitude
                                        if key == 'latitude':
                                            # Si les données de la colonne du dataframe sont des valeurs de latitude
                                            if all(self.dataframe[column].between(-90.0, 90.0)):
                                                # Ajout des données de la colonne du dataframe dans le tableau de données associé à la clé
                                                self.xarray_dataset[key].values = np.array(self.dataframe[column].iloc[:].tolist())
                                            # Sinon les données de la colonne du dataframe ne sont pas des valeurs de latitude
                                            else:
                                                modeleMainwindow.log("Latitude values are not between -90 and 90.")
                                        # Si la clé est longitude
                                        elif key == 'longitude':
                                            # Si les données de la colonne du dataframe sont des valeurs de longitude
                                            if all(self.dataframe[column].between(-180.0, 180.0)):
                                                # Ajout des données de la colonne du dataframe dans le tableau de données associé à la clé
                                                self.xarray_dataset[key].values = np.array(self.dataframe[column].iloc[:].tolist())
                                            # Sinon les données de la colonne du dataframe ne sont pas des valeurs de longitude
                                            else:
                                                modeleMainwindow.log("Longitude values are not between -180 and 180.")
                                        # Sinon la clé est une autre clé
                                        else:
                                            # Ajout des données de la colonne du dataframe dans le tableau de données associé à la clé
                                            self.xarray_dataset[key].values = np.array(self.dataframe[column].iloc[:].tolist())
                                    # Sinon
                                    else:
                                        modeleMainwindow.log("Less than 10 data are present in column " + column + " . Data will be not selected.")
                                # Sinon
                                else:
                                    modeleMainwindow.log("Data type in column " + column + " : " + str(self.dataframe[column].dtype) + " does not match the type of the variable : " + key + " : " + self.xarray_dataset[key].attrs['dtype'] + " . Data will be not selected.")


    def check_datetime_format(self: Self):
        
        # Si le dataframe est vide
        if self.dataframe.empty:
            modeleMainwindow.log("Empty dataframe.")
            self.dataframe = pd.DataFrame()
        # Sinon
        else:
            # Parcours de chaque colonne du dataframe
            for column in self.dataframe.columns:
                # Parcours de chaque élément de la première liste du catalogue
                for element in modeleNetCDF.datetime_catalog[0]:
                    # Si l'élément du catalogue est contenu dans le nom de la colonne du dataframe en minuscule sans espace blanc et si le catalogue ne contient pas plus de 3 listes
                    if element in column.replace(' ', '').lower() and len(modeleNetCDF.datetime_catalog) < 3:
                        # Si la liste de données de la colonne du dataframe contient au minimum 10 données
                        if len(self.dataframe[column].iloc[:].tolist()) >= 10:
                            # Ajout des données de la colonne du dataframe dans le catalogue
                            modeleNetCDF.datetime_catalog.append(self.dataframe[column].iloc[:].tolist())
                        # Sinon
                        else:
                            modeleMainwindow.log("Less than 10 data are present in column " + column + " . Data will be not selected.")
            # Si le catalogue contient une liste de noms possibles pour la variable datetime et une liste de données temporelles
            if len(modeleNetCDF.datetime_catalog) == 2:
                # Parcours de la première donnée temporelle jusqu'à la dernière dans la liste
                for i in range(0, len(modeleNetCDF.datetime_catalog[1])):
                    # Si la donnée temporelle est au format timestamp
                    if isinstance(modeleNetCDF.datetime_catalog[1][i], pd.Timestamp):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                        modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))
                    # Si la donnée temporelle est au format datetime
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], datetime):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                        modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))   
                    # Si la donnée temporelle est au format date
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], date):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                        modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%Y-%m-%d"))
                    # Si la donnée temporelle est au format time
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], time):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                        modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%H:%M:%S"))    
                    # Si la donnée temporelle est une chaîne de caractères
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], str):
                        # Si la donnée temporelle n'est pas au format 'YYYY-MM-DD HH:MM:SS', 'YYYY-MM-DD' ou 'HH:MM:SS'
                        if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1]) (?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[1][i])) == False and bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', modeleNetCDF.datetime_catalog[1][i])) == False and bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[1][i])) == False:
                            # La donnée temporelle est nulle
                            modeleNetCDF.datetime_catalog[1][i] = str('')
                    # Sinon le type de donnée n'est pas correct
                    else:
                        modeleMainwindow.log("Incorrect data type for " + str(modeleNetCDF.datetime_catalog[1][i]) + " : " + str(type(modeleNetCDF.datetime_catalog[1][i])) + " . Data will be cleared.")
                        # La donnée temporelle est nulle
                        modeleNetCDF.datetime_catalog[1][i] = str('')  
                # Ajout des données temporelles de la liste dans le tableau de données associé à la clé
                self.xarray_dataset['datetime'].values = np.array(modeleNetCDF.datetime_catalog[1])  
            # Si le catalogue contient une liste de noms possibles pour la variable datetime et 2 listes de données temporelles
            elif len(modeleNetCDF.datetime_catalog) == 3:
                # Parcours de la première donnée temporelle jusqu'à la dernière dans la liste
                for i in range(0, len(modeleNetCDF.datetime_catalog[1])):
                    # Si la donnée temporelle est au format timestamp
                    if isinstance(modeleNetCDF.datetime_catalog[1][i], pd.Timestamp):
                        # Si la donnée temporelle est au format 'YYYY-MM-DD'
                        if str(modeleNetCDF.datetime_catalog[1][i].strftime("%H:%M:%S")) == '00:00:00':
                            # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                            modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%Y-%m-%d"))
                            # Si la donnée temporelle de la deuxième liste est au format time
                            if isinstance(modeleNetCDF.datetime_catalog[2][i], time):
                                # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                                modeleNetCDF.datetime_catalog[2][i] = str(modeleNetCDF.datetime_catalog[2][i].strftime("%H:%M:%S"))   
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[1][i] + " " + modeleNetCDF.datetime_catalog[2][i]
                            # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                            elif isinstance(modeleNetCDF.datetime_catalog[2][i], str):
                                # Si la donnée temporelle est au format 'HH:MM:SS'
                                if bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[2][i])) == True:
                                    # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                    modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[1][i] + " " + modeleNetCDF.datetime_catalog[2][i]
                        # Sinon la donnée temporelle est au format 'YYYY-MM-DD HH:MM:SS'
                        else:
                            # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))
                    # Si la donnée temporelle est au format datetime
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], datetime):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                        modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%Y-%m-%d %H:%M:%S"))
                    # Si la donnée temporelle est au format date
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], date):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                        modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%Y-%m-%d"))
                        # Si la donnée temporelle de la deuxième liste est au format time
                        if isinstance(modeleNetCDF.datetime_catalog[2][i], time):
                            # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                            modeleNetCDF.datetime_catalog[2][i] = str(modeleNetCDF.datetime_catalog[2][i].strftime("%H:%M:%S"))   
                            # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[1][i] + " " + modeleNetCDF.datetime_catalog[2][i]
                        # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                        elif isinstance(modeleNetCDF.datetime_catalog[2][i], str):
                            # Si la donnée temporelle est au format 'HH:MM:SS'
                            if bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[2][i])) == True:
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[1][i] + " " + modeleNetCDF.datetime_catalog[2][i]
                    # Si la donnée temporelle est au format time
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], time):
                        # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                        modeleNetCDF.datetime_catalog[1][i] = str(modeleNetCDF.datetime_catalog[1][i].strftime("%H:%M:%S"))
                        # Si la donnée temporelle de la deuxième liste est au format date
                        if isinstance(modeleNetCDF.datetime_catalog[2][i], date):
                            # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                            modeleNetCDF.datetime_catalog[2][i] = str(modeleNetCDF.datetime_catalog[2][i].strftime("%Y-%m-%d"))   
                            # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                            modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[2][i] + " " + modeleNetCDF.datetime_catalog[1][i]
                        # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                        elif isinstance(modeleNetCDF.datetime_catalog[2][i], str):
                            # Si la donnée temporelle est au format 'YYYY-MM-DD'
                            if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', modeleNetCDF.datetime_catalog[2][i])) == True:
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[2][i] + " " + modeleNetCDF.datetime_catalog[1][i]
                    # Si la donnée temporelle est une chaîne de caractères
                    elif isinstance(modeleNetCDF.datetime_catalog[1][i], str):                
                        # Si la donnée temporelle est une chaîne de caractères au format 'YYYY-MM-DD'    
                        if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', modeleNetCDF.datetime_catalog[1][i])) == True:
                            # Si la donnée temporelle de la deuxième liste est au format time
                            if isinstance(modeleNetCDF.datetime_catalog[2][i], time):
                                # Conversion de la donnée temporelle en chaîne de caractères au format 'HH:MM:SS'
                                modeleNetCDF.datetime_catalog[2][i] = str(modeleNetCDF.datetime_catalog[2][i].strftime("%H:%M:%S"))   
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[1][i] + " " + modeleNetCDF.datetime_catalog[2][i]
                            # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                            elif isinstance(modeleNetCDF.datetime_catalog[2][i], str):
                                # Si la donnée temporelle de la deuxième liste est une chaîne de caractères au format 'HH:MM:SS'
                                if bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[2][i])) == True:
                                    # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                    modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[1][i] + " " + modeleNetCDF.datetime_catalog[2][i]
                        # Si la donnée temporelle est une chaîne de caractères au format 'HH:MM:SS'    
                        elif bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[1][i])) == True:
                            # Si la donnée temporelle de la deuxième liste est au format date
                            if isinstance(modeleNetCDF.datetime_catalog[2][i], date):
                                # Conversion de la donnée temporelle en chaîne de caractères au format 'YYYY-MM-DD'
                                modeleNetCDF.datetime_catalog[2][i] = str(modeleNetCDF.datetime_catalog[2][i].strftime("%Y-%m-%d"))   
                                # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[2][i] + " " + modeleNetCDF.datetime_catalog[1][i]
                            # Si la donnée temporelle de la deuxième liste est une chaîne de caractères
                            elif isinstance(modeleNetCDF.datetime_catalog[2][i], str):
                                # Si la donnée temporelle de la deuxième liste est une chaîne de caractères au format 'YYYY-MM-DD'
                                if bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', modeleNetCDF.datetime_catalog[2][i])) == True:
                                    # Concaténation pour obtenir une chaîne de caractères au format 'YYYY-MM-DD HH:MM:SS'
                                    modeleNetCDF.datetime_catalog[1][i] = modeleNetCDF.datetime_catalog[2][i] + " " + modeleNetCDF.datetime_catalog[1][i]
                        # Si la donnée temporelle est une chaîne de caractères qui n'est pas au format 'YYYY-MM-DD HH:MM:SS', 'YYYY-MM-DD' ou 'HH:MM:SS'
                        elif bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1]) (?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[1][i])) == False and bool(re.match(r'^(?:\d{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])$', modeleNetCDF.datetime_catalog[1][i])) == False and bool(re.match(r'^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', modeleNetCDF.datetime_catalog[1][i])) == False:
                            modeleMainwindow.log("Date format not recognized for " + str(modeleNetCDF.datetime_catalog[1][i]) + " . Data will be cleared.")
                            # La donnée temporelle est nulle
                            modeleNetCDF.datetime_catalog[1][i] = str('')
                    # Sinon le type de donnée n'est pas correct
                    else:
                        modeleMainwindow.log("Incorrect data type for " + str(modeleNetCDF.datetime_catalog[1][i]) + " : " + str(type(modeleNetCDF.datetime_catalog[1][i])) + " . Data will be cleared.")
                        # La donnée temporelle est nulle
                        modeleNetCDF.datetime_catalog[1][i] = str('') 
                # Technique de slicing pour retirer toutes les listes de données temporelles sauf la première
                modeleNetCDF.datetime_catalog = modeleNetCDF.datetime_catalog[:-(len(modeleNetCDF.datetime_catalog)-2)]
                # Ajout des données temporelles de la liste dans le tableau de données associé à la clé
                self.xarray_dataset['datetime'].values = np.array(modeleNetCDF.datetime_catalog[1])


    def adapt_xarray_dataset(self: Self):
        
        # Parcours de chaque clé du dataset xarray
        for key in list(self.xarray_dataset.data_vars.keys()):
            # Si le tableau de données de la clé est vide
            if np.all(self.xarray_dataset[key].values == 0) or np.all(self.xarray_dataset[key].values != self.xarray_dataset[key].values):
                # Suppression des attributs de la variable
                self.xarray_dataset[key].attrs.clear()
                # Suppression de la variable
                del self.xarray_dataset[key]


    def get_xarray_dataset(self: Self):
        
        return self.xarray_dataset


    def __repr__(self: Self):
        
        print(self.xarray_dataset)
        
    
    # Définition des méthodes statiques
    
    
    @staticmethod
    def create_xarray_dataset(dataframe: pd.DataFrame):
        
        # Initialisation du dataset xarray
        xarray_dataset = xr.Dataset()
        
        # Chargement le fichier JSON
        with open('./catalog.json', 'r') as f:
            catalog = json.load(f)
            
        # Accès à chaque valeur de chaque attribut du catalogue
        variable_catalog = catalog['variable']
        dimension_catalog = catalog['dimension']
        global_attribute_catalog = catalog['global_attribute']
        
        for dimension in dimension_catalog:
            xarray_dataset.coords[dimension] = np.arange(dataframe.shape[0])
        
        for variable_name, variable_data in variable_catalog.items():
            xarray_dataset[variable_name] = xr.DataArray(np.zeros(dataframe.shape[0]), dims=variable_data['dimension'])
            for attribute_name, attribute_value in variable_data['attribute'].items():
                xarray_dataset[variable_name].attrs[attribute_name] = attribute_value
        
        for global_attribute_name, global_attribute_value in global_attribute_catalog.items():
            xarray_dataset.attrs[global_attribute_name] = global_attribute_value
    
        return xarray_dataset




# Programme principal




if __name__ == '__main__':
    
    # Initialisation du dataframe
    controleurToolbar.import_option()
    
    # Initialisation du dataset xarray
    xarray_dataset = modeleNetCDF.create_xarray_dataset(controleurToolbar.dataframe)
    
    modelenetCDF = modeleNetCDF(controleurToolbar.dataframe, xarray_dataset)
    modelenetCDF.check_dataframe_integrity()
    modelenetCDF.check_datetime_format()
    modelenetCDF.adapt_xarray_dataset()
    modelenetCDF.__repr__()
