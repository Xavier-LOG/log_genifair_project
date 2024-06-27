# Importation des bibliothèques




import pandas as pd
from datetime import datetime, date, time
import re
import json
import os




# Définition de la classe outilsArrangement




class outilsArrangement:


    # Définition des méthodes statiques
    
    
    @staticmethod
    def read_json(path: str):
        
        """_summary_
        Lecture JSON
        Returns:
            _type_: _description_
        """
        
        catalog = {}
        if path != "":
            # Si la taille du fichier n'est pas vide
            if os.path.getsize(path) != 0:
                # Chargement le fichier JSON
                with open(path, 'r') as f:
                    # Chargement du catalogue
                    catalog = json.load(f)
        
        # Retourne le catalogue
        return catalog
    
    
    @staticmethod
    def write_json(path: str, catalog: dict):
        
        """_summary_
        Ecriture du catalogue
        """
        
        # Ecriture du fichier JSON 
        with open(path, "w") as f:
            json.dump(catalog, f, indent = 4)
    
    
    @staticmethod
    def fill_catalog(catalog: dict, dimension_name: str, dataframe: pd.DataFrame, datetime_catalog: list):
        
        """_summary_
        Remplissage automatique du catalogue
        Returns:
            _type_: _description_
        """
        
        # Si le dataframe existe
        if not dataframe.empty:
                            
            # Parcours de chaque colonne du dataframe
            for column in dataframe.columns:
                # Si le nom de la colonne du dataframe filtré n'est pas dans les variables du catalogue
                if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower() not in catalog['variable']:
                    # Si le nom de la colonne du dataframe filtré commence ou se termine par station
                    if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith('station') or re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith('station'):
                        # Ajout de la variable
                        catalog['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
                            "dimension" : ['Station'],
                            "attribute" : {
                                ":dtype": str(dataframe[column].dtype),
                                ":units": "NaN",
                                ":sdn_uom_name": "NaN",
                                ":sdn_uom_urn": "urn:sdn:parameter:NaN",
                                ":standard_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower(),
                                ":long_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace('_', ' ').lower().capitalize(),
                                ":sdn_parameter_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower(),
                                ":sdn_paramter_urn": "urn:sdn:parameter:" + str(re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()),
                                "column_name": str(column)
                            }
                        }
                    # Si le nom de la colonne du dataframe filtré commence ou se termine par l'un des mots de la liste
                    elif [word for word in ['latitude', 'lat'] if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
                        # Ajout de la variable
                        catalog['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
                            "dimension" : [dimension_name],
                            "attribute" : {
                                ":axis": "Y",
                                ":coverage_content_type": "coordinate",
                                ":dtype": "float64",
                                ":units": "degree North",
                                ":sdn_uom_name": "degree_North",
                                ":sdn_uom_urn": "urn:sdn:parameter:degree_North",
                                ":standard_name": "latitude",
                                ":long_name": "Latitude",
                                ":sdn_parameter_name": "Latitude north",
                                ":sdn_paramter_urn": "SDN:P01::ALATZZ01",
                                "column_name": "lat"
                            }
                        }
                    # Si le nom de la colonne du dataframe filtré commence ou se termine par l'un des mots de la liste
                    elif [word for word in ['longitude', 'lon'] if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
                        # Ajout de la variable
                        catalog['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
                            "dimension" : [dimension_name],
                            "attribute" : {
                                ":axis": "X",
                                ":coverage_content_type": "coordinate",
                                ":dtype": "float64",
                                ":units": "degree East",
                                ":sdn_uom_name": "degree_East",
                                ":sdn_uom_urn": "urn:sdn:parameter:degree_East",
                                ":standard_name": "longitude",
                                ":long_name": "Longitude",
                                ":sdn_parameter_name": "Longitude east",
                                ":sdn_paramter_urn": "SDN:P01::ALONZZ01",
                                "column_name": "lon"
                            }
                        }
                    # Si le nom de la colonne du dataframe filtré commence ou se termine par l'un des noms possibles de date
                    elif [word for word in datetime_catalog if re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
                        # Si la variable time n'est pas dans le catalogue
                        if 'time' not in catalog['variable']:
                            # Ajout de la variable time
                            catalog['variable']['time'] = {
                                "dimension" : [dimension_name],
                                "attribute" : {
                                    ":axis": "T",
                                    ":coverage_content_type": "coordinate",
                                    ":dtype": "object",
                                    ":units": "seconds since 1970-01-01 00:00:00",
                                    ":origin": "01-JAN-1970 00:00:00",
                                    ":calendar": "standard",
                                    ":sdn_uom_name": "seconds",
                                    ":sdn_uom_urn": "SDN:P06::UTBB",
                                    ":standard_name": "time",
                                    ":long_name": "Time",
                                    ":sdn_parameter_name": "Elapsed time relative to 1970-01-01T00:00:00Z",
                                    ":sdn_paramter_urn": "SDN:P01::ELTMEP01",
                                    "column_name": "datetime"
                                }
                            }
                            # Si le nom de la dimension n'est pas dans l'attribut global
                            if dimension_name not in catalog['global_attribute'][':coordinates']:
                                # Ajout de la dimension
                                catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                            # Si la première ligne de la colonne du dataframe est de type datetime ou date
                            if isinstance(dataframe.iloc[0][column], datetime) or isinstance(dataframe.iloc[0][column], date):   
                                # Conversion en str et ajout
                                catalog['global_attribute'][":time_coverage_start"] = dataframe.iloc[0][column].strftime("%Y-%m-%d")
                            # Si la première ligne de la colonne du dataframe est de type time
                            elif isinstance(dataframe.iloc[0][column], time):
                                # Conversion en str et ajout
                                catalog['global_attribute'][":time_coverage_start"] = dataframe.iloc[0][column].strftime("%H:%M:%S")
                            # Si la première ligne de la colonne du dataframe est de type timestamp
                            elif isinstance(dataframe.iloc[0][column], pd.Timestamp):
                                # Conversion en str et ajout
                                catalog['global_attribute'][":time_coverage_start"] = datetime.fromtimestamp(dataframe.iloc[0][column]).strftime("%Y-%m-%d")
                            # Si la première ligne de la colonne du dataframe est de type str
                            elif isinstance(dataframe.iloc[0][column], str):
                                # Ajout
                                catalog['global_attribute'][":time_coverage_start"] = str(dataframe.iloc[0][column])
                            # Si la dernière ligne de la colonne du dataframe est de type datetime ou date
                            if isinstance(dataframe.iloc[-1][column], datetime) or isinstance(dataframe.iloc[-1][column], date):   
                                # Conversion en str et ajout
                                catalog['global_attribute'][":time_coverage_end"] = dataframe.iloc[-1][column].strftime("%Y-%m-%d")
                            # Si la dernière ligne de la colonne du dataframe est de type time
                            elif isinstance(dataframe.iloc[-1][column], time):
                                # Conversion en str et ajout
                                catalog['global_attribute'][":time_coverage_end"] = dataframe.iloc[-1][column].strftime("%H:%M:%S")
                            # Si la dernière ligne de la colonne du dataframe est de type timestamp
                            elif isinstance(dataframe.iloc[-1][column], pd.Timestamp):
                                # Conversion en str et ajout
                                catalog['global_attribute'][":time_coverage_end"] = datetime.fromtimestamp(dataframe.iloc[-1][column]).strftime("%Y-%m-%d")
                            # Si la dernière ligne de la colonne du dataframe est de type str
                            elif isinstance(dataframe.iloc[-1][column], str):
                                # Ajout
                                catalog['global_attribute'][":time_coverage_end"] = str(dataframe.iloc[-1][column])
                    # Sinon
                    else:
                        # Si le nom de la colonne du dataframe filtré ne commence pas par unnamed
                        if not re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith('unnamed'):
                            # Ajout de la variable
                            catalog['variable']["sea_water_" + re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
                                "dimension" : [dimension_name],
                                "attribute" : {
                                    ":dtype": str(dataframe[column].dtype),
                                    ":units": re.sub(r'[^\u0391-\u03A9\u03B1-\u03C9-a-zA-Z\s/%._]', '', column.split(",")[1].strip("_")).replace(' ','').lower() if len(column.split(",")) == 2 else "NaN",
                                    ":sdn_uom_name": re.sub(r'[^\u0391-\u03A9\u03B1-\u03C9-a-zA-Z\s/%._]', '', column.split(",")[1].strip("_")).replace(' ','').lower() if len(column.split(",")) == 2 else "NaN",
                                    ":sdn_uom_urn": "urn:sdn:parameter:" + re.sub(r'[^\u0391-\u03A9\u03B1-\u03C9-a-zA-Z\s/%._]', '', column.split(",")[1].strip("_")).replace(' ','').lower() if len(column.split(",")) == 2 else "NaN",
                                    ":standard_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower(),
                                    ":long_name": "sea_water_" + re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace('_', ' ').lower().capitalize(),
                                    ":sdn_parameter_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower(),
                                    ":sdn_paramter_urn": "urn:sdn:parameter:" + str(re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()),
                                    "column_name": str(column)
                                }
                            }
                                
            # Retourne le catalogue actualisé
            return catalog
    
    
    @staticmethod
    def dimension_name_add(catalog: dict, dimension_name: str):
    
        """_summary_
        Ajout du nom de la dimension
        Returns:
            _type_: _description_
        """
    
        # Ajout de la dimension
        catalog['dimension'][dimension_name] = {
            "values": []
        }
        # Ajout de la variable dimensionnelle
        catalog['variable'][dimension_name.lower()] = {
            "dimension" : [dimension_name],
            "attribute" : {
                ":dtype": "float64",
                ":units": "NaN",
                ":sdn_uom_name": "NaN",
                ":sdn_uom_urn": "urn:sdn:parameter:NaN",
                ":standard_name": dimension_name.lower(),
                ":long_name": dimension_name.replace('_', ' '),
                ":sdn_parameter_name": dimension_name.lower(),
                ":sdn_paramter_urn": "urn:sdn:parameter:" + str(dimension_name.lower()),
                "column_name": dimension_name.lower()
            }
        }
        # Si la dimension n'est pas dans l'attribut global
        if dimension_name not in catalog['global_attribute'][':coordinates'].replace(' ', '').split(','):
            # Ajout de la dimension dans l'attribut global
            catalog['global_attribute'][':coordinates'] += ", " + dimension_name
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def dimension_value_add(catalog: dict, dimension_name: str, dimension_value: str):
        
        """_summary_
        Ajout de la valeur de la dimension
        Returns:
            _type_: _description_
        """
        
        # Ajout des valeurs dans la dimension
        catalog['dimension'][dimension_name]['values'] = [float(word.replace(' ', '')) for word in dimension_value.split(',')]
    
        return catalog
    
    
    @staticmethod
    def dimension_name_modify(catalog: dict, dimension_name: str, dimension_new_name: str):
        
        """_summary_
        Modification du nom de la dimension
        Returns:
            _type_: _description_
        """
        
        # Ajout de la nouvelle dimension
        catalog['dimension'][dimension_new_name] = {
            'values': catalog['dimension'][dimension_name]['values']
        }
    
        # Recherche de la variable de la dimension
        # Parcours de chaque variable dans le catalogue
        for variable_name in catalog['variable']:
            # Si la dimension est dans les informations de la variable
            if 'dimension' in catalog['variable'][variable_name] and dimension_name in catalog['variable'][variable_name]['dimension']:
                # Si la variable est une variable dimensionnelle
                if variable_name == dimension_name.lower():
                    # Parcours de chaque attribut de variable obligatoire
                    for word in [":axis", ":standard_name", ":long_name", ":sdn_parameter_name", ":sdn_parameter_urn"]:
                        # Si l'attribut est dans les informations de la variable
                        if word in catalog['variable'][variable_name]['attribute']:
                            # Si la dimension en minuscule est dans l'attribut
                            if dimension_name.lower() in catalog['variable'][variable_name]['attribute'][word]:
                                # Remplacement de la dimension par la dimension actuelle
                                catalog['variable'][variable_name]['attribute'][word] = catalog['variable'][variable_name]['attribute'][word].replace(dimension_name.lower(), dimension_new_name.lower())
                            # Si la dimension est dans l'attribut
                            elif dimension_name in catalog['variable'][variable_name]['attribute'][word]:
                                # Remplacement de la dimension par la dimension actuelle
                                catalog['variable'][variable_name]['attribute'][word] = catalog['variable'][variable_name]['attribute'][word].replace(dimension_name, dimension_new_name)
                    # Ajout de la nouvelle variable dimensionnelle
                    catalog['variable'][dimension_new_name.lower()] = {
                        'dimension' : [word.replace(dimension_name, dimension_new_name) for word in catalog['variable'][variable_name]['dimension']],
                        'attribute' : catalog['variable'][variable_name]['attribute']
                    }
                    # Suppression de la variable dimensionnelle
                    del catalog['variable'][variable_name]
                    # Sortie de boucle
                    break
    
        # Recherche des variables ayant pour dimension dimension_name
        for variable_name in catalog['variable']:
            # Si la dimension est dans les informations de la variable
            if 'dimension' in catalog['variable'][variable_name] and dimension_name in catalog['variable'][variable_name]['dimension']:
                # Remplacement de la dimension dans la liste par la dimension actuelle
                catalog['variable'][variable_name]['dimension'] = [word.replace(dimension_name, dimension_new_name) for word in catalog['variable'][variable_name]['dimension']]
        
        # Mise à jour des attributs globaux
        catalog['global_attribute'][':coordinates'] = catalog['global_attribute'][':coordinates'].replace(dimension_name, dimension_new_name)
        
        # Suppression de la dimension
        del catalog['dimension'][dimension_name]
        
        # Retourne le catalogue actualisé
        return catalog


    @staticmethod
    def dimension_value_modify(catalog: dict, dimension_name: str, dimension_value: str, value_checked: int):
        
        """_summary_
        Modification de la valeur de la dimension
        Returns:
            _type_: _description_
        """
        
        # Si toutes les valeurs de la dimension ont été vérifiées
        if value_checked == len(dimension_value.replace(' ','').split(',')):
            # Modification de la valeur de la dimension
            catalog['dimension'][dimension_name]['values'] = [float(word.replace(' ', '')) for word in dimension_value.split(',')]
        # Si la valeur de la dimension est vide
        elif dimension_value == "":
            # Modification de la valeur de la dimension
            catalog['dimension'][dimension_name]['values'] = []
        
        # Retourne le catalogue actualisé
        return catalog

    
    @staticmethod
    def dimension_name_delete(catalog: dict, dimension_name: str, variables_to_remove: list):
    
        """_summary_
        Suppression du nom de la dimension
        Returns:
            _type_: _description_
        """
    
        # Parcours de chaque variable à supprimer dans la liste
        for variable in variables_to_remove:
            # Si la variable a une dimension
            if len(catalog['variable'][variable]['dimension']) == 1:
                # Suppression de la variable ayant pour dimension dimension_name
                del catalog['variable'][variable]
            # Si la variable a deux dimensions
            elif len(catalog['variable'][variable]['dimension']) == 2:
                # Suppression de la dimension dans la liste
                catalog['variable'][variable]['dimension'].remove(dimension_name)

        # Mise à jour des attributs globaux
        catalog['global_attribute'][':coordinates'] = ', '.join([word.replace(' ','') for word in catalog['global_attribute'][':coordinates'].split(',') if dimension_name != word.replace(' ','')])
        
        # Suppression de la dimension
        del catalog['dimension'][dimension_name]
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def dimension_value_delete(catalog: dict, dimension_name: str):
        
        """_summary_
        Suppression de la valeur de la dimension
        Returns:
            _type_: _description_
        """
        
        # Modification de la valeur de la dimension
        catalog['dimension'][dimension_name]['values'] = []
        
        # Retourne le catalogue actualisé
        return catalog

    
    @staticmethod
    def variable_name_add(catalog: dict, variable_name: str, variable_dimension_list: list, datetime_catalog: list):
        
        """_summary_
        Ajout du nom de la variable
        Returns:
            _type_: _description_
        """
    
        # Si la variable commence ou se termine par un des mots de la liste et si la variable n'est pas dans le catalogue    
        if [word for word in ['latitude', 'lat'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in catalog['variable']:
            # Ajout de la variable
            catalog['variable'][variable_name] = {
                "dimension" : variable_dimension_list,
                "attribute" : {
                    ":axis": "Y",
                    ":coverage_content_type": "coordinate",
                    ":dtype": "float64",
                    ":units": "degree North",
                    ":sdn_uom_name": "degree_North",
                    ":sdn_uom_urn": "urn:sdn:parameter:degree_North",
                    ":standard_name": variable_name,
                    ":long_name": variable_name.replace('_', ' ').capitalize(),
                    ":sdn_parameter_name": "Latitude north",
                    ":sdn_paramter_urn": "SDN:P01::ALATZZ01",
                    "column_name": "lat"
                }
            }
        # Si la variable commence ou se termine par un des mots de la liste et si la variable n'est pas dans le catalogue    
        elif [word for word in ['longitude', 'lon'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in catalog['variable']:
            # Ajout de la variable
            catalog['variable'][variable_name] = {
                "dimension" : variable_dimension_list,
                "attribute" : {
                    ":axis": "X",
                    ":coverage_content_type": "coordinate",
                    ":dtype": "float64",
                    ":units": "degree East",
                    ":sdn_uom_name": "degree_East",
                    ":sdn_uom_urn": "urn:sdn:parameter:degree_East",
                    ":standard_name": variable_name,
                    ":long_name": variable_name.replace('_', ' ').capitalize(),
                    ":sdn_parameter_name": "Longitude east",
                    ":sdn_paramter_urn": "SDN:P01::ALONZZ01",
                    "column_name": "lon"
                }
            }
        # Si la variable commence ou se termine par un des mots de la liste et si la variable n'est pas dans le catalogue    
        elif [word for word in ['depth', 'profondeur'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in catalog['variable']:
            # Ajout de la variable
            catalog['variable'][variable_name] = {
                "dimension" : variable_dimension_list,
                "attribute" : {
                    ":axis": "Z",
                    ":coverage_content_type": "coordinate",
                    ":dtype": "float64",
                    ":units": "meters",
                    ":sdn_uom_name": "meters",
                    ":sdn_uom_urn": "urn:sdn:parameter:meters",
                    ":standard_name": variable_name,
                    ":long_name": variable_name.replace('_', ' ').capitalize(),
                    ":sdn_parameter_name": variable_name,
                    ":sdn_paramter_urn": "urn:sdn:parameter:" + str(variable_name),
                    ":positive": "down",
                    "column_name": "profondeur"
                }
            }
        # Si la variable commence ou se termine par un des mots de la liste des noms possibles de date et si la variable n'est pas dans le catalogue    
        elif [word for word in datetime_catalog if variable_name.startswith(word) or variable_name.endswith(word)] and 'time' not in catalog['variable']:
            # Ajout de la variable time
            catalog['variable']['time'] = {
                "dimension" : variable_dimension_list,
                "attribute" : {
                    ":axis": "T",
                    ":coverage_content_type": "coordinate",
                    ":dtype": "object",
                    ":units": "seconds since 1970-01-01 00:00:00",
                    ":origin": "01-JAN-1970 00:00:00",
                    ":calendar": "standard",
                    ":sdn_uom_name": "seconds",
                    ":sdn_uom_urn": "SDN:P06::UTBB",
                    ":standard_name": "time",
                    ":long_name": "Time",
                    ":sdn_parameter_name": "Elapsed time relative to 1970-01-01T00:00:00Z",
                    ":sdn_paramter_urn": "SDN:P01::ELTMEP01",
                    "column_name": "datetime"
                }
            }
            # Mise à jour des attributs globaux
            catalog['global_attribute'][':time_coverage_start'] = "NaN"
            catalog['global_attribute'][':time_coverage_end'] = "NaN"
        # Sinon
        else:
            # Ajout de la variable
            catalog['variable'][variable_name] = {
                "dimension" : variable_dimension_list,
                "attribute" : {
                    ":dtype": "float64",
                    ":units": "NaN",
                    ":sdn_uom_name": "NaN",
                    ":sdn_uom_urn": "urn:sdn:parameter:NaN",
                    ":standard_name": variable_name,
                    ":long_name": variable_name.replace('_', ' ').capitalize(),
                    ":sdn_parameter_name": variable_name,
                    ":sdn_paramter_urn": "urn:sdn:parameter:" + str(variable_name),
                    "column_name": str(variable_name)
                }
            }
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def variable_attribute_add(catalog: dict, variable_name: str, attribute_name: str, attribute_value: str):
    
        """_summary_
        Ajout de l'attribut de variable
        Returns:
            _type_: _description_
        """
        
        # Ajout de l'attribut de variable
        catalog['variable'][variable_name]["attribute"][":" + attribute_name] = attribute_value
    
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def variable_name_modify(catalog: dict, variable_name: str, variable_new_name: str, dimension_name_list: list):
        
        """_summary_
        Modification du nom de variable
        Returns:
            _type_: _description_
        """
        
        # Ajout de la nouvelle variable
        catalog['variable'][variable_new_name] = {
            "dimension" : dimension_name_list,
            "attribute" : catalog['variable'][variable_name]['attribute']
        }
        # Si le nom de la nouvelle variable est différent du nom de la variable
        if variable_new_name != variable_name:
            # Suppression de la variable
            del catalog['variable'][variable_name]
        
        # Retourne le catalogue actualisé
        return catalog


    @staticmethod
    def variable_attribute_modify(catalog: dict, variable_name: str, attribute_name: str, attribute_new_name: str, attribute_new_value: str):

        """_summary_
        Modification de l'attribut de variable
        Returns:
            _type_: _description_
        """
        
        # Remplacement de l'attribut de variable par le nouvel attribut de variable
        catalog['variable'][variable_name]['attribute'][":" + attribute_new_name] = catalog['variable'][variable_name]['attribute'].pop(":" + attribute_name)
        # Ajout de la valeur au nouvel attribut de variable
        catalog['variable'][variable_name]['attribute'][":" + attribute_new_name] = attribute_new_value
    
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def variable_name_delete(catalog: dict, variable_name: str):
    
        """_summary_
        Suppression du nom de variable
        Returns:
            _type_: _description_
        """
        
        # Suppression de la variable
        del catalog['variable'][variable_name]
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def variable_attribute_delete(catalog: dict, variable_name: str, attribute_name: str):        
        
        """_summary_
        Suppression de l'attribut de variable
        Returns:
            _type_: _description_
        """
        
        # Suppression de l'attribut de variable
        del catalog['variable'][variable_name]['attribute'][":" + attribute_name]
        
        # Retourne le catalogue actualisé
        return catalog


    @staticmethod
    def global_attribute_name_add(catalog: dict, global_attribute_name: str):

        """_summary_
        Ajout de l'attribut global
        Returns:
            _type_: _description_
        """
        
        # Ajout de l'attribut global
        catalog['global_attribute'][":" + global_attribute_name] = "NaN"
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def global_attribute_value_add(catalog: dict, global_attribute_name: str, global_attribute_value: str):
    
        """_summary_
        Ajout de la valeur de l'attribut global
        Returns:
            _type_: _description_
        """
    
        # Ajout de la valeur à l'attribut global    
        catalog['global_attribute'][":" + global_attribute_name] = global_attribute_value
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def global_attribute_name_modify(catalog: dict, global_attribute_name: str, global_attribute_new_name: str):
    
        """_summary_
        Modification du nom de l'attribut global
        Returns:
            _type_: _description_
        """
        
        # Remplacement de l'attribut global par le nouvel attribut global
        catalog['global_attribute'][":" + global_attribute_new_name] = catalog['global_attribute'][":" + global_attribute_name]
        # Suppression de l'attribut global
        del catalog['global_attribute'][":" + global_attribute_name]
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def global_attribute_value_modify(catalog: dict, global_attribute_name: str, global_attribute_new_value: str):
    
        """_summary_
        Modification de la valeur de l'attribut global
        Returns:
            _type_: _description_
        """
        
        # Ajout de la valeur à l'attribut global
        catalog['global_attribute'][":" + global_attribute_name] = global_attribute_new_value
        
        # Retourne le catalogue actualisé
        return catalog
    
    
    @staticmethod
    def global_attribute_name_delete(catalog: dict, global_attribute_name: str):
    
        """_summary_
        Suppression de l'attribut global
        Returns:
            _type_: _description_
        """
        
        # Suppression de l'attribut global
        del catalog['global_attribute'][":" + global_attribute_name]
        
        # Retourne le catalogue actualisé
        return catalog
    
        
    @staticmethod
    def global_attribute_value_delete(catalog: dict, global_attribute_name: str):
        
        """_summary_
        Suppression de la valeur de l'attribut global
        Returns:
            _type_: _description_
        """
        
        # Suppression de la valeur de l'attribut global
        catalog['global_attribute'][":" + global_attribute_name] = "NaN"
        
        # Retourne le catalogue actualisé
        return catalog
