# Importation des fichiers




from outilsArrangement import outilsArrangement




# Importation des bibliothèques




import pandas as pd
from datetime import datetime, date, time
import re
from PyQt6.QtWidgets import QToolTip
from PyQt6.QtCore import QObject, QEvent




# Définition de la classe controleurCatalogsettings




class controleurCatalogsettings(QObject):


    # Constructeur par défaut
        
    
    def __init__(self, vuecatalogsettings):
        
        super().__init__()
        self.vuecatalogsettings = vuecatalogsettings
        self.dataframe = pd.DataFrame()
        # Catalogue des noms possibles de date
        self.datetime_catalog = ['datetime', 'date', 'time', 'temps', 'heure', 'hour', 'minute', 'seconde', 'yyyy-mm-ddthh:mm:ss', 'yyyy/mm/ddthh:mm:ss', 'yyyy-mm-dd hh:mm:ss', 'yyyy/mm/dd hh:mm:ss', 'yyyy-mm-dd', 'yyyy/mm/dd', 'dd-mm-yyyy', 'dd/mm/yyyy', 'hh:mm:ss', 'hh:mm:ss.sss']
        # Noms de dimension optionnels
        self.optional_dimension_name_list = ['Depth', 'Latitude', 'Longitude', 'Sample', 'Station', 'Time']
        # Valeurs de dimension optionnelles
        self.optional_dimension_value_list = ['400, 500, 600, 700', '400, 450, 500, 550, 600, 650, 700', '1, 2', '1, 2, 3', '1, 2, 3, 4', '1, 2, 3, 4, 5', '1, 2, 3, 4, 5, 6', '1, 2, 3, 4, 5, 6, 7', '1, 2, 3, 4, 5, 6, 7, 8', '1, 2, 3, 4, 5, 6, 7, 8, 9', '1, 2, 3, 4, 5, 6, 7, 8, 9, 10']
        # Noms de variable optionnels
        self.optional_variable_name_list = ['sea_surface_temperature', 'sea_bottom_temperature', 'sea_surface_salinity', 'sea_bottom_salinity', 'sea_surface_pressure', 'sea_bottom_pressure', 'sea_surface_height', 'sea_bottom_depth', 'sea_surface_oxygen_concentration', 'sea_bottom_oxygen_concentration', 'sea_surface_chlorophyll_concentration', 'sea_bottom_chlorophyll_concentration']
        # Attributs de variable obligatoires
        self.mandatory_variable_attribute_list = ['dtype', 'units', 'sdn_uom_name', 'sdn_uom_urn', 'standard_name', 'long_name', 'sdn_parameter_name', 'sdn_paramter_urn']
        # Attributs de variables optionnels
        self.optional_variable_attribute_list = ['axis', 'calendar', 'comment', 'coverage_content_type', 'inverse_flattening', 'origin', 'scale_factor', 'valid_max', 'valid_min']
        # Attributs globaux obligatoires
        self.mandatory_global_attribute_list = ['_FillValue', 'coordinates', 'title', 'project', 'Conventions', 'institution', 'source', 'request_for_aknowledgement', 'citation', 'license', 'references', 'summary', 'principal_investigator', 'principal_investigator_email', 'metadata_contact', 'contributor_name', 'contributor_role', 'contact', 'featureType', 'cdm_data_type', 'comments', 'history', 'creator_email', 'creator_name', 'creator_url']
        # Attributs globaux optionnels
        self.optional_global_attribute_list = ['comment', 'date_created', 'date_modified', 'geospatial_lat_max', 'geospatial_lat_min', 'geospatial_lat_resolution', 'geospatial_lat_units', 'geospatial_lon_max', 'geospatial_lon_min', 'geospatial_lon_resolution', 'geospatial_lon_units', 'geospatial_vertical_max', 'geospatial_vertical_min', 'geospatial_vertical_positive', 'geospatial_vertical_resolution', 'keywords', 'keywords_vocabulary', 'platform', 'time_coverage_start', 'time_coverage_end']
        # Signal pour remplir les listes déroulantes lorsque le catalogue a été mis à jour dans la vue
        self.catalog_signal = self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.signal
        self.catalog_signal.connect(self.fill_combobox)
        # Signal pour récupérer le premier dataframe de(s) fichier(s) importé(s) pour remplir des attributs globaux spécifiques
        self.dataframe_signal = self.vuecatalogsettings.vuecatalog.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.dataframe_signal.connect(self.set_dataframe)

    
    # Définition des méthodes
    
    
    def set_dataframe(self, obj):
        
        """_summary_
        Remplissage des attributs globaux temporels lors de l'importation du premier fichier
        """
        
        # Dataframe du premier fichier importé
        self.dataframe: pd.DataFrame = obj[1][0]
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue et le dataframe existent
        if catalog and not self.dataframe.empty:
            # Si les attributs globaux sont dans le catalogue
            if ":time_coverage_start" in catalog['global_attribute'] and ":time_coverage_end" in catalog['global_attribute']:
                # Parcours de chaque colonne du dataframe
                for column in self.dataframe.columns:
                    # Si l'un des noms possibles de date est présent au début ou à la fin du nom filtré de la colonne du dataframe
                    # Remplacement de tous les caractères qui ne sont pas des lettres minuscules, majuscules, /, :, ., -, _ par du vide
                    if [word for word in self.datetime_catalog if re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
                        # Si le format de la première valeur de la colonne est datetime ou date
                        if isinstance(self.dataframe.iloc[0][column], datetime) or isinstance(self.dataframe.iloc[0][column], date):   
                            # Conversion en str de la première valeur de la colonne
                            catalog['global_attribute'][":time_coverage_start"] = self.dataframe.iloc[0][column].strftime("%Y-%m-%d")
                        # Si le format de la première valeur de la colonne est time
                        elif isinstance(self.dataframe.iloc[0][column], time):
                            # Conversion en str de la première valeur de la colonne
                            catalog['global_attribute'][":time_coverage_start"] = self.dataframe.iloc[0][column].strftime("%H:%M:%S")
                        # Si le format de la première valeur de la colonne est timestamp
                        elif isinstance(self.dataframe.iloc[0][column], pd.Timestamp):
                            # Conversion en str de la première valeur de la colonne
                            catalog['global_attribute'][":time_coverage_start"] = datetime.fromtimestamp(self.dataframe.iloc[0][column]).strftime("%Y-%m-%d")
                        elif isinstance(self.dataframe.iloc[0][column], str):
                            catalog['global_attribute'][":time_coverage_start"] = str(self.dataframe.iloc[0][column])
                        # Si le format de la dernière valeur de la colonne est datetime ou date
                        if isinstance(self.dataframe.iloc[-1][column], datetime) or isinstance(self.dataframe.iloc[-1][column], date):   
                            # Conversion en str de la dernière valeur de la colonne
                            catalog['global_attribute'][":time_coverage_end"] = self.dataframe.iloc[-1][column].strftime("%Y-%m-%d")
                        # Si le format de la dernière valeur de la colonne est time
                        elif isinstance(self.dataframe.iloc[-1][column], time):
                            # Conversion en str de la dernière valeur de la colonne
                            catalog['global_attribute'][":time_coverage_end"] = self.dataframe.iloc[-1][column].strftime("%H:%M:%S")
                        # Si le format de la dernière valeur de la colonne est timestamp
                        elif isinstance(self.dataframe.iloc[-1][column], pd.Timestamp):
                            # Conversion en str de la dernière valeur de la colonne
                            catalog['global_attribute'][":time_coverage_end"] = datetime.fromtimestamp(self.dataframe.iloc[-1][column]).strftime("%Y-%m-%d")
                        # Si le format de la dernière valeur de la colonne est str
                        elif isinstance(self.dataframe.iloc[-1][column], str):
                            catalog['global_attribute'][":time_coverage_end"] = str(self.dataframe.iloc[-1][column])
    
    
    def eventFilter(self, source, event):
        
        """_summary_
        Affichage de bulles d'information indiquant les définitions des métadonnées
        Returns:
            _type_: _description_
        """
        
        # Si l'évènement en cours correspond à l'affichage d'une bulle d'information
        if event.type() == QEvent.Type.ToolTip:
            # Si les sources sont des listes déroulantes des attributs de variable
            if source == self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox or source == self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox:
                # Récupération de l'indice de l'élément actuel de la liste
                index = source.currentIndex()
                if index == 0:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the direction of data in a specific dimension, such as time (axis: “T”), etc.")
                elif index == 1:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Specifies the type of calendar used to interpret dates (calendar: “gregorian”)")
                elif index == 2:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Additional textual description providing explanations and details about a variable")
                elif index == 3:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Describes the type of data contained, such as thematic data (coverage_content_type: “coordinate”)")
                elif index == 4:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the measure of the Earth's flatness")
                elif index == 5:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates data source (origin: “01-JAN-1970 00:00:00”)")
                elif index == 6:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Adjusts stored values to a specific scale (scale_factor: “0.1”)")
                elif index == 7:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Specifies the maximum valid value for a given variable")
                elif index == 8:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Specifies the minimum valid value for a given variable")
                else:
                    QToolTip.hideText()
            # Si les sources sont des listes déroulantes des attributs globaux
            elif source == self.vuecatalogsettings.attribute_tabwidget.add_name_combobox or source == self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox:
                # Récupération de l'indice de l'élément actuel de la liste
                index = source.currentIndex()
                if index == 0:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Brief description or remarks on the data contained in the file")
                elif index == 1:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the date on which the file was first created or generated")
                elif index == 2:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the last time the file was modified")
                elif index == 3:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the maximum latitude of geospatial data")
                elif index == 4:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the minimum latitude of geospatial data")
                elif index == 5:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the spatial resolution of the data in latitude")
                elif index == 6:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Specifies the unit used to measure latitude, often in degrees north or south of the equator")
                elif index == 7:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the maximum longitude of geospatial data")
                elif index == 8:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the minimum longitude of geospatial data")
                elif index == 9:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the spatial resolution of the data in longitude")
                elif index == 10:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Specifies the unit used to measure longitude, often in degrees east or west in relation to the Greenwich meridian")
                elif index == 11:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the maximum value of the geospatial vertical dimension, often used to represent the maximum depth or altitude of geospatial data")
                elif index == 12:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the minimum value of the geospatial vertical dimension, often used to represent the minimum depth or altitude of geospatial data")
                elif index == 13:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the positive direction of the vertical axis, for example “up” to indicate that values increase with altitude")
                elif index == 14:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the precision with which data is represented along the vertical axis")
                elif index == 15:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Keywords describing the content and subject of the file")
                elif index == 16:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Indicates the vocabulary used to describe the keywords associated with the data")
                elif index == 17:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Provides information on the platform from which the data was collected or generated, such as the type of sensor or instrument used")
                elif index == 18:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Specifies the start of the period of temporal data coverage")
                elif index == 19:
                    # Récupération de la position du curseur de la souris sur l'écran pour afficher la bulle d'information indiquant la définition de l'attribut
                    QToolTip.showText(event.globalPos(), "Specifies the end of the period of temporal data coverage")
                else:
                    QToolTip.hideText()
            return True
        # Traitement des évènements de bulle d'information
        return super().eventFilter(source, event)
    
    
    def fill_combobox(self, obj):
        
        """_summary_
        Remplissage des listes déroulantes lorsque le catalogue a été mis à jour dans la vue vueCatalogviewer
        """
        
        catalog = obj
        # Si le catalogue existe
        if catalog:
        
            # Actualisation de la liste déroulante    
            self.vuecatalogsettings.dimension_tabwidget.add_name_combobox.clear()
            # Ajout des noms de dimension optionnels dans la liste
            self.vuecatalogsettings.dimension_tabwidget.add_name_combobox.addItems(self.optional_dimension_name_list)
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.clear()
            # Ajout des noms de dimension du catalogue dans la liste
            self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.clear()
            # Ajout des valeurs de dimension optionnelles dans la liste
            self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.addItems(self.optional_dimension_value_list)
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.clear()
            # Ajout des noms de dimension du catalogue dans la liste
            self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.addItems(list(catalog['dimension'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.clear()
            # Ajout des noms de dimension optionnels dans la liste
            self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.addItems(self.optional_dimension_name_list)
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.clear()
            # Ajout des noms de dimension du catalogue dans la liste
            self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.clear()
            # Ajout des valeurs de dimension optionnelles dans la liste
            self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.addItems(self.optional_dimension_value_list)
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.delete_name_combobox.clear()
            # Ajout des noms de dimension du catalogue dans la liste
            self.vuecatalogsettings.dimension_tabwidget.delete_name_combobox.addItems(list(catalog['dimension'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.dimension_tabwidget.delete_value_dimension_combobox.clear()
            # Ajout des noms de dimension du catalogue dans la liste
            self.vuecatalogsettings.dimension_tabwidget.delete_value_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.add_name_combobox.clear()
            # Ajout des noms de variable optionnels dans la liste
            self.vuecatalogsettings.variable_tabwidget.add_name_combobox.addItems(self.optional_variable_name_list)
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.clear()
            # Ajout des noms de dimension du catalogue dans la liste
            self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.clear()
            # Ajout des noms de variable du catalogue dans la liste
            self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.addItems(list(catalog['variable'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.clear()
            # Ajout des attributs de variable optionnels dans la liste
            self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.addItems(self.optional_variable_attribute_list)
            # Gestion des évènements de bulle d'information
            self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.installEventFilter(self)
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.clear()
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.clear()
            # Ajout des noms de variable du catalogue dans la liste
            self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.addItems(list(catalog['variable'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.clear()
            # Ajout des noms de variable optionnels dans la liste
            self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.addItems(self.optional_variable_name_list)
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.clear()
            # Ajout des noms de dimension du catalogue dans la liste
            self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.clear()
            # Ajout des noms de variable du catalogue dans la liste
            self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.addItems(list(catalog['variable'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.clear()
            # Ajout des attributs de variable optionnels dans la liste
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.addItems(self.optional_variable_attribute_list)
            # Gestion des évènements de bulle d'information
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.installEventFilter(self)
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.clear()
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.delete_name_combobox.clear()
            # Ajout des noms de variable du catalogue dans la liste
            self.vuecatalogsettings.variable_tabwidget.delete_name_combobox.addItems(list(catalog['variable'].keys()))
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.clear()
            # Ajout des noms de variable du catalogue dans la liste
            self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.addItems(list(catalog['variable'].keys()))
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.clear()
            # Ajout des attributs globaux optionnels dans la liste
            self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.addItems(self.optional_global_attribute_list)
            # Gestion des évènements de bulle d'information
            self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.installEventFilter(self)
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.clear()
            # Ajout des attributs globaux du catalogue dans la liste sans le ":"
            self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.clear()
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.clear()
            # Ajout des attributs globaux du catalogue dans la liste sans le ":"
            self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.clear()
            # Ajout des attributs globaux optionnels dans la liste
            self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.addItems(self.optional_global_attribute_list)
            # Gestion des évènements de bulle d'information
            self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.installEventFilter(self)
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.clear()
            # Ajout des attributs globaux du catalogue dans la liste sans le ":"
            self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.clear()
            
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.delete_name_combobox.clear()
            # Ajout des attributs globaux du catalogue dans la liste sans le ":"
            self.vuecatalogsettings.attribute_tabwidget.delete_name_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            # Actualisation de la liste déroulante
            self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_combobox.clear()
            # Ajout des attributs globaux du catalogue dans la liste sans le ":"
            self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
    
    
    def fill_catalog(self):
        
        """_summary_
        Remplissage automatique du catalogue dans la vue à partir de l'outil d'agencement
        """
        
        dimension_name: str = ""
        # Si les chemins de fichier existent
        if self.vuecatalogsettings.vuecatalog.modelecatalog.path_list_files[1]:
            # Si le dataframe existe
            if not self.dataframe.empty:
                # Initialisation d'un nouveau catalogue
                catalog = {
                    "dimension": {
                        "Station": {
                            "values": []
                        }
                    },
                    "variable": {
                    },
                    "global_attribute": {
                        ":_FillValue": "NaN",
                        ":project": "NaN",
                        ":coordinates": "Station",
                        ":Conventions": "CF-1.6, SeaDataNet_1.0",
                        ":institution": "LOG Wimereux",
                        ":source": "NaN",
                        ":request_for_aknowledgement": "If you use the data in presentation or in publications, please acknowledge. Send us also a reprint or preprint of publications using the data for inclusion in our bibliography.",
                        ":citation": "NaN",
                        ":license": "The data is not intended for legal use. However, it may be used and redistributed for free.",
                        ":references": "NaN",
                        ":summary": "NaN",
                        ":principal_investigator": "NaN",
                        ":principal_investigator_email": "NaN",
                        ":metadata_contact": "NaN",
                        ":contributor_name": "NaN",
                        ":contributor_role": "NaN",
                        ":contact": "NaN",
                        ":comments": "NaN",
                        ":history": "NaN",
                        ":creator_email": "NaN",
                        ":creator_name": "NaN",
                        ":creator_url": "NaN"
                    }
                }
                # Si le catalogue de type trajectoire ou de type série temporelle a été coché
                if self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked() or self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_time_series_catalog_checkbox.isChecked():
                    # Ajout de la variable dimensionnelle
                    dimension_name = "Time"
                    catalog['variable'][dimension_name.lower()] = {
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
                    # Mise à jour des attributs globaux
                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                    catalog['global_attribute'][':time_coverage_start'] = "NaN"
                    catalog['global_attribute'][':time_coverage_end'] = "NaN"
                    # Si le catalogue de type trajectoire a été coché
                    if self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked():  
                        # Mise à jour des attributs globaux
                        catalog['global_attribute'][':title'] = "Trajectory"
                        catalog['global_attribute'][':featureType'] = "Trajectory"
                        catalog['global_attribute'][':cdm_data_type'] = "Trajectory"
                    # Sinon
                    else:
                        # Mise à jour des attributs globaux
                        catalog['global_attribute'][':title'] = "Timeseries"
                        catalog['global_attribute'][':featureType'] = "TimeSeries"
                        catalog['global_attribute'][':cdm_data_type'] = "TimeSeries"
                # Si le catalogue de type profil a été coché
                elif self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_profile_catalog_checkbox.isChecked():
                    dimension_name = "Depth"
                    # Ajout de la variable dimensionnelle
                    catalog['variable'][dimension_name.lower()] = {
                        "dimension" : [dimension_name],
                        "attribute" : {
                            ":axis": "Z",
                            ":coverage_content_type": "coordinate",
                            ":dtype": "float64",
                            ":units": "meters",
                            ":sdn_uom_name": "meters",
                            ":sdn_uom_urn": "urn:sdn:parameter:meters",
                            ":standard_name": "depth",
                            ":long_name": "Depth",
                            ":sdn_parameter_name": "depth",
                            ":sdn_paramter_urn": "urn:sdn:parameter:depth",
                            ":positive": "down",
                            "column_name": "profondeur"
                        }
                    }
                    # Mise à jour des attributs globaux
                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                    catalog['global_attribute'][':title'] = "Profile"
                    catalog['global_attribute'][':featureType'] = "Profile"
                    catalog['global_attribute'][':cdm_data_type'] = "Profile"
                # Si le catalogue de type échantillonnage a été coché
                elif self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_sample_catalog_checkbox.isChecked():
                    dimension_name = "Sample"
                    # Ajout de la variable dimensionnelle
                    catalog['variable'][dimension_name.lower()] = {
                        "dimension" : [dimension_name],
                        "attribute" : {
                            ":axis": "Sample",
                            ":coverage_content_type": "coordinate",
                            ":dtype": "object",
                            ":units": "NaN",
                            ":standard_name": "sample",
                            ":long_name": "Sample",
                            ":sdn_parameter_name": "sample",
                            ":sdn_paramter_urn": "urn:sdn:parameter:sample",
                            "column_name": "sample"
                        }
                    }
                    # Mise à jour des attributs globaux
                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                    catalog['global_attribute'][':title'] = "Sample"
                
                # Ajout de la dimension
                catalog['dimension'][dimension_name] = {
                        "values": []
                }
                # Mise à jour de la date de création
                catalog['global_attribute'][':date_created'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                
                # Remplissage automatique du catalogue à partir de l'outil d'agencement
                catalog = outilsArrangement.fill_catalog(catalog, dimension_name, self.dataframe, self.datetime_catalog)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()            
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Empty dataframe. Catalog will not be filled.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Empty dataframe. Catalog will not be filled.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("No path file. Catalog will not be filled.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("No path file. Catalog will not be filled.\n", "red")
    
    
    def dimension_name_add(self):
        
        """_summary_
        Ajout du nom de dimension dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.add_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il n'est pas dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name not in catalog['dimension'] and dimension_name not in catalog['global_attribute'][':coordinates'].replace(' ', '').split(','):
                # Ajout du nom de dimension à partir de l'outil d'agencement
                catalog = outilsArrangement.dimension_name_add(catalog, dimension_name)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def dimension_value_add_confirm(self):
        
        """_summary_
        Confirmation de l'ajout de la valeur de la dimension dans la vue
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension']:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_cancel_button.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def dimension_value_add_cancel(self):
        
        """_summary_
        Annulation de l'ajout de la valeur de la dimension dans la vue
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_cancel_button.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.setEnabled(False)
    
    
    def dimension_value_add(self):
        
        """_summary_
        Ajout de la valeur de la dimension dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.currentText()
        # Récupération de la valeur de dimension choisi dans la liste déroulante
        dimension_value: str = self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.currentText()
        # Variable pour vérifier les valeurs correctes saisies par l'utilisateur
        value_checked: int = 0
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
                # Parcours des valeurs de la dimension
                for value in dimension_value.replace(' ','').split(','):
                    # Si la valeur contient des points, des chiffres ou des tirets
                    if bool(re.match(r'^[\d\s.-]+$', value)) == True:
                        # S'il y a un ou zéro signe moins et s'il y a un ou zéro point
                        if (value.count("-") == 0 or value.count("-") == 1) and (value.count(".") == 0 or value.count(".") == 1):
                            # Si le signe moins est devant la valeur et si la valeur contient au moins 1 chiffre
                            if "-" in value and value[0] == "-" and len(value) > 1:
                                # Si la valeur est flottante, si le point est entre deux chiffres et si la valeur contient au moins un point et 2 chiffres
                                if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 2:
                                    # La valeur saisie est correcte
                                    value_checked += 1
                                # Si la valeur n'est pas flottante
                                elif "." not in value:
                                    # La valeur saisie est correcte
                                    value_checked += 1
                            # Si la valeur n'est pas négative
                            elif "-" not in value:
                                # Si la valeur est flottante, si le point est entre deux chiffres et si la valeur contient au moins 2 chiffres
                                if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 1:
                                    # La valeur saisie est correcte
                                    value_checked += 1
                                # Si la valeur n'est pas flottante
                                elif "." not in value:
                                    # La valeur saisie est correcte
                                    value_checked += 1
                # Si toutes les valeurs de la dimension sont correctes
                if value_checked == len(dimension_value.replace(' ','').split(',')):
                    # Ajout de la dimension de la valeur à partir de l'outil d'agencement
                    catalog = outilsArrangement.dimension_value_add(catalog, dimension_name, dimension_value)
                    # Ecriture du catalogue
                    self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                    self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                    self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.setEnabled(True)
                    self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.setEnabled(False)
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension value added.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension value added.\n", "green")
                # Sinon
                else:
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension values.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension values.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
            
    
    def dimension_name_modify_confirm(self):
        
        """_summary_
        Confirmation de la modification du nom de la dimension dans la vue
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
        
    
    def dimension_name_modify_cancel(self):
    
        """_summary_
        Annulation de la modification du nom de la dimension dans la vue
        """
    
        # Grisage et dégrisage des zones nécessaires    
        self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.setEnabled(False)
    
    
    def dimension_name_modify(self):
        
        """_summary_
        Modification du nom de la dimension dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.currentText()
        # Récupération du nom de la nouvelle dimension choisi dans la liste déroulante
        dimension_new_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il n'est pas dans le catalogue
            if dimension_new_name != "" and any(char.isspace() for char in dimension_new_name) == False and dimension_new_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_new_name)) == True and dimension_new_name not in catalog['dimension']:
                # Modification du nom de la dimension à partir de l'outil d'agencement
                catalog = outilsArrangement.dimension_name_modify(catalog, dimension_name, dimension_new_name)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")


    def dimension_value_modify_confirm(self):

        """_summary_
        Confirmation de la modification de la valeur de la dimension dans la vue
        """

        # Récupération du nom de dimension choisi dans la liste déroulante        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_cancel_button.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def dimension_value_modify_cancel(self):
        
        """_summary_
        Annulation de la modification de la valeur de la dimension dans la vue
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_cancel_button.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.setEnabled(False)
    
    
    def dimension_value_modify(self):
        
        """_summary_
        Modification de la valeur de la dimension dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.currentText()
        # Récupération de la valeur de dimension choisi dans la liste déroulante
        dimension_value: str = self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.currentText()
        # Variable pour vérifier si les valeurs saisies sont correctes
        value_checked: int = 0
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Parcours des valeurs de la dimension
            for value in dimension_value.replace(' ','').split(','):
                # Si la valeur contient des points, des chiffres ou des tirets
                if bool(re.match(r'^[\d\s.-]+$', value)) == True:
                    # S'il y a un ou zéro signe moins et s'il y a un ou zéro point
                    if (value.count("-") == 0 or value.count("-") == 1) and (value.count(".") == 0 or value.count(".") == 1):
                        # Si le signe moins est devant la valeur et si la valeur contient au moins 1 chiffre
                        if "-" in value and value[0] == "-" and len(value) > 1:
                            # Si la valeur est flottante, si le point est entre deux chiffres et si la valeur contient au moins un point et 2 chiffres
                            if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 2:
                                # La valeur saisie est correcte
                                value_checked += 1
                            # Si la valeur n'est pas flottante
                            elif "." not in value:
                                # La valeur saisie est correcte
                                value_checked += 1
                        # Si la valeur n'est pas négative
                        elif "-" not in value:
                            # Si la valeur est flottante, si le point est entre deux chiffres et si la valeur contient au moins 2 chiffres
                            if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 1:
                                # La valeur saisie est correcte
                                value_checked += 1
                            # Si la valeur n'est pas flottante
                            elif "." not in value:
                                # La valeur saisie est correcte
                                value_checked += 1
            # Si toutes les valeurs de la dimension sont correctes
            if value_checked == len(dimension_value.replace(' ','').split(',')) or dimension_value == "":
                # Modification de la valeur de la dimension à partir de l'outil d'agencement
                catalog = outilsArrangement.dimension_value_modify(catalog, dimension_name, dimension_value, value_checked)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.setEnabled(True)
                self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_cancel_button.setEnabled(False)
                self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension value modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension value modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension values.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension values.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")

    
    def dimension_name_delete(self):
        
        """_summary_
        Suppression du nom de la dimension et de ses variables dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.delete_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule, s'il n'y a que des lettres ou des chiffres mais pas seulement que des chiffres, s'il est inclu dans le catalogue et s'il y a au minimum plusieurs dimensions
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable'] and len(catalog['dimension']) > 1:
                # Initialisation d'une liste pour enlever les variables dépendant de la dimension à supprimer
                variables_to_remove = []
                # Recherche des variables ayant pour dimension dimension_name
                for variable_name in catalog['variable']:
                    # Si la dimension est dans les informations de la variable
                    if 'dimension' in catalog['variable'][variable_name] and dimension_name in catalog['variable'][variable_name]['dimension']:
                        # Ajout de la variable à supprimer
                        variables_to_remove.append(variable_name)
                        
                # S'il y a au minimum une variable de dimension différente de la dimension à supprimer dans le catalogue
                if len(variables_to_remove) < len(catalog['variable']):
                    # Suppression du nom de la dimension à partir de l'outil d'agencement
                    catalog = outilsArrangement.dimension_name_delete(catalog, dimension_name, variables_to_remove)
                    # Ecriture du catalogue
                    self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                    self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name deleted.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name deleted.\n", "green")
                # Sinon
                else:
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The model structure must depend on at least 1 variable. Please enter a new variable with another dimension first.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The model structure must depend on at least 1 variable. Please enter a new variable with another dimension first.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name. The model structure must depend on at least 1 dimension. Please enter a new dimension first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name. The model structure must depend on at least 1 dimension. Please enter a new dimension first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def dimension_value_delete(self):
        
        """_summary_
        Suppression de la valeur de la dimension dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.delete_value_dimension_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
                # Suppression de la valeur de la dimension à partir de l'outil d'agencement
                catalog = outilsArrangement.dimension_value_delete(catalog, dimension_name)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension value deleted.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension value deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    

    def variable_name_add_confirm(self):
        
        """_summary_
        Confirmation de l'ajout du nom de variable dans la vue
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name not in catalog['variable']:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalogsettings.variable_tabwidget.add_name_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_name_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")

    
    def variable_name_add_cancel(self):
        
        """_summary_
        Annulation de l'ajout du nom de variable dans la vue
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.add_name_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.setEnabled(False)

    
    def variable_name_add(self):
        
        """_summary_
        Ajout du nom de variable dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_name_combobox.currentText()
        # Récupération du nom de dimension de la variable choisi dans la liste déroulante
        variable_dimension: str = self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.currentText()
        # Initialisation d'une liste pour les dimensions de la variable
        variable_dimension_list: list = []
        # Variable pour vérifier les dimensions de la variable
        variable_dimension_checked: int = 0
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name not in catalog['variable']:
                # Filtration de la liste des dimensions de la variable pour supprimer les espaces blancs
                variable_dimension_list = [word.replace(' ', '') for word in variable_dimension.split(',')]
                # Pour chaque élément de la liste
                for element in variable_dimension_list:
                    # Si l'élément est dans les dimensions du catalogue
                    if element in catalog['dimension']:
                        # La dimension de la variable est vérifiée
                        variable_dimension_checked += 1
                       
                # Si toutes les dimensions de la variable sont correctes
                if variable_dimension_checked == len(variable_dimension_list):
                    # Ajout du nom de variable à partir de l'outil d'agencement
                    catalog = outilsArrangement.variable_name_add(catalog, variable_name, variable_dimension_list, self.datetime_catalog)
                    # Ecriture du catalogue
                    self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                    self.vuecatalogsettings.variable_tabwidget.add_name_combobox.setEnabled(True)
                    self.vuecatalogsettings.variable_tabwidget.add_name_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.setEnabled(False)
                    self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name added.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name added.\n", "green")
                # Sinon
                else:
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_variable_add_confirm(self):
        
        """_summary_
        Confirmation de l'ajout de la variable de l'attribut de variable dans la vue
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in catalog['variable']:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_variable_add_cancel(self):
        
        """_summary_
        Annulation de l'ajout de la variable de l'attribut de variable dans la vue
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.setEnabled(False)
    
    
    def variable_attribute_add_confirm(self):
        
        """_summary_
        Confirmation de l'ajout de l'attribut de variable dans la vue
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.currentText()
        # Récupération du nom de l'attribut de variable choisi dans la liste déroulante
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut n'est pas vide et si le nom du nouvel attribut ne contient aucun espace blanc
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) not in catalog['variable'][variable_name]['attribute']:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Attribute name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Attribute name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect attribute name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect attribute name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_add_cancel(self):
    
        """_summary_
        Annulation de l'ajout de l'attribut de variable dans la vue
        """
    
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.setEnabled(False)
    
    
    def variable_attribute_add(self):
        
        """_summary_
        Ajout de l'attribut de variable dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.currentText()
        # Récupération du nom de l'attribut de variable choisi dans la liste déroulante
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.currentText()
        # Récupération de la valeur de l'attribut de variable choisi dans la liste déroulante
        attribute_value: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut et de la nouvelle valeur ne sont pas vides et si le nom du nouvel attribut ne contient aucun espace blanc
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) not in catalog['variable'][variable_name]['attribute'] and attribute_value != "":
                # Ajout de l'attribut de variable à partir de l'outil d'agencement
                catalog = outilsArrangement.variable_attribute_add(catalog, variable_name, attribute_name, attribute_value)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable attribute name added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable attribute name added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_modify_confirm(self):
        
        """_summary_
        Confirmation de la modification du nom de variable
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in catalog['variable']:
                # Si la variable n'est pas une variable de dimension
                if len(catalog['variable'][variable_name]['dimension']) == 1 and (variable_name.capitalize() == catalog['variable'][variable_name]['dimension'][0] or variable_name == "time"):
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The dimension variable cannot be modified.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The dimension variable cannot be modified.\n", "red")
                # Sinon
                else:
                    self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(True)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(True)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(False)
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_modify_cancel(self):
        
        """_summary_
        Annulation de la modification du nom de variable
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(False)
    
    
    def variable_new_name_modify_confirm(self):
        
        """_summary_
        Confirmation de la modification du nom de la nouvelle variable
        """
        
        # Récupération du nom de la nouvelle variable choisi dans la liste déroulante
        variable_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if variable_new_name != "" and any(char.isspace() for char in variable_new_name) == False and variable_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_new_name)) == True:
                # Grisage et dégrisage des zones nécessaires
                self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable new name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable new name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_new_name_modify_cancel(self):
        
        """_summary_
        Annulation de la modification du nom de la nouvelle variable
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(False)
    
    
    def variable_name_modify(self):
        
        """_summary_
        Modification du nom de la variable dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.currentText()
        # Récupération du nom de la nouvelle variable choisi dans la liste déroulante
        variable_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.currentText()
        # Récupération du nom de dimension choisi dans la liste déroulante
        dimension_name: str = self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.currentText()
        # Initialisation d'une liste pour les dimensions
        dimension_name_list: list = []
        # Variable pour vérifier les dimensions
        dimension_name_checked: int = 0
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if variable_new_name != "" and any(char.isspace() for char in variable_new_name) == False and variable_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_new_name)) == True:
                # Filtration de la liste des dimensions pour supprimer les espaces blancs
                dimension_name_list = [word.replace(' ', '') for word in dimension_name.split(',')]
                # Pour chaque élément de la liste
                for element in dimension_name_list:
                    # Si l'élément est dans les dimensions du catalogue
                    if element in catalog['dimension']:
                        # La dimension est vérifiée
                        dimension_name_checked += 1
                        
                # Si toutes les dimensions sont correctes
                if dimension_name_checked == len(dimension_name_list):
                    # Si la variable contient une seule dimension
                    if len(catalog['variable'][variable_name]['dimension']) == 1:
                        # Si le nom de la nouvelle variable n'est pas time et si sa première lettre est en minuscule
                        if variable_new_name != "time" and variable_new_name.capitalize() != catalog['variable'][variable_name]['dimension'][0]:
                            # Modification du nom de variable à partir de l'outil d'agencement
                            catalog = outilsArrangement.variable_name_modify(catalog, variable_name, variable_new_name, dimension_name_list)
                            # Ecriture du catalogue
                            self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                            self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(True)
                            self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
                            self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(False)
                            self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(False)
                            self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(False)
                            self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name and dimension name modified.\n")
                            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name and dimension name modified.\n", "green")
                        # Sinon
                        else:
                            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The variable cannot be assigned to 'time'. The default 'time' variable cannot be modified due to dates.\n")
                            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The variable cannot be assigned to 'time'. The default 'time' variable cannot be modified due to dates.\n", "red")    
                    # Si la variable contient plus d'une dimension
                    elif len(catalog['variable'][variable_name]['dimension']) > 1:
                        # Modification du nom de variable à partir de l'outil d'agencement
                        catalog = outilsArrangement.variable_name_modify(catalog, variable_name, variable_new_name, dimension_name_list)
                        # Ecriture du catalogue
                        self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                        self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(True)
                        self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
                        self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(False)
                        self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(False)
                        self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(False)
                        self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name and dimension name modified.\n")
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name and dimension name modified.\n", "green")
                # Sinon
                else:
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_variable_modify_confirm(self):
    
        """_summary_
        Confirmation de la modification de la variable de l'attribut de variable
        """
    
        # Récupération du nom de variable choisi dans la liste déroulante    
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in catalog['variable']:
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.clear()
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.addItems([key[1:] for key in list(catalog['variable'][variable_name]['attribute'].keys()) if key != 'column_name'])
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_variable_modify_cancel(self):
        
        """_summary_
        Annulation de la modification de la variable de l'attribut de variable
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)
    
    
    def variable_attribute_modify_confirm(self):
        
        """_summary_
        Confirmation de la modification de l'attribut de variable
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.currentText()
        # Récupération du nom de l'attribut de variable choisi dans la liste déroulante
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut n'est pas vide, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il n'est pas un attribut obligatoire
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) in catalog['variable'][variable_name]['attribute']:
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable attribute name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable attribute name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_modify_cancel(self):
        
        """_summary_
        Annulation de la modification de l'attribut de variable
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)


    def variable_new_attribute_modify_confirm(self):
        
        """_summary_
        Confirmation de la modification du nouvel attribut de variable
        """
        
        # Récupération du nom de l'attribut de variable choisi dans la liste déroulante
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.currentText()
        # Récupération du nom du nouvel attribut de variable choisi dans la liste déroulante
        attribute_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut n'est pas vide, si la première lettre est en minuscule et s'il n'est pas un attribut obligatoire
            if attribute_new_name != "" and any(char.isspace() for char in attribute_new_name) == False and attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_new_name)) == True:
                # Si le nom de l'attribut est dans la liste des attributs de variable obligatoires et si le nom du nouvel attribut est l'attribut
                if attribute_name in self.mandatory_variable_attribute_list and attribute_new_name == attribute_name:
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(True)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(True)
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable attribute new name selected.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable attribute new name selected.\n", "green")
                # Si le nom de l'attribut n'est pas dans la liste des attributs de variable obligatoires
                elif attribute_name not in self.mandatory_variable_attribute_list and attribute_new_name not in self.mandatory_variable_attribute_list:
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(True)
                    self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(True)
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable attribute new name selected.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable attribute new name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_new_attribute_modify_cancel(self):
        
        """_summary_
        Annulation de la modification du nouvel attribut de variable
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)


    def variable_attribute_modify(self):
        
        """_summary_
        Modification de l'attribut de variable dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.currentText()
        # Récupération du nom de l'attribut de variable choisi dans la liste déroulante
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.currentText()
        # Récupération du nom du nouvel attribut de variable choisi dans la liste déroulante
        attribute_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.currentText()
        # Récupération de la valeur du nouvel attribut de variable choisi dans la liste déroulante
        attribute_new_value: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut n'est pas vide, si la première lettre est en minuscule et si la nouvelle valeur de l'attribut n'est pas vide
            if attribute_new_name != "" and any(char.isspace() for char in attribute_new_name) == False and attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_new_name)) == True and attribute_new_value != "":
                # Modification de l'attribut de variable à partir de l'outil d'agencement
                catalog = outilsArrangement.variable_attribute_modify(catalog, variable_name, attribute_name, attribute_new_name, attribute_new_value)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable attribute value modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable attribute value modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_delete(self):
        
        """_summary_
        Suppression du nom de variable dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il y a au minimum plusieurs variables
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in catalog['variable'] and len(catalog['variable']) > 1:
                if len(catalog['variable'][variable_name]['dimension']) == 1:
                    # Si le nom de la variable n'est pas celui d'une variable de dimension
                    if variable_name != "time" and variable_name.capitalize() != catalog['variable'][variable_name]['dimension'][0]:
                        # Suppression du nom de variable à partir de l'outil d'agencement
                        catalog = outilsArrangement.variable_name_delete(catalog, variable_name)
                        # Ecriture du catalogue
                        self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                        self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable deleted.\n")
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable deleted.\n", "green")
                    # Sinon
                    else:
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The variable " + variable_name + " of the dimension " + catalog['variable'][variable_name]['dimension'][0] + " cannot be deleted.\n")
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The variable " + variable_name + " of the dimension " + catalog['variable'][variable_name]['dimension'][0] + " cannot be deleted.\n", "red")
                elif len(catalog['variable'][variable_name]['dimension']) > 1:
                    catalog = outilsArrangement.variable_name_delete(catalog, variable_name)
                    self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                    self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable deleted.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name. The model structure must depend on at least 1 variable. Please enter a new variable first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name. The model structure must depend on at least 1 variable. Please enter a new variable first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_delete_confirm(self):
        
        """_summary_
        Confirmation de la suppression de l'attribut de variable
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in catalog['variable']:
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.setEnabled(False)
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.setEnabled(True)
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.clear()
                self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.addItems([key[1:] for key in list(catalog['variable'][variable_name]['attribute'].keys()) if key != 'column_name'])
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_attribute_delete_cancel(self):
        
        """_summary_
        Annulation de la suppresion de l'attribut de variable
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.setEnabled(False)
    
    
    def variable_attribute_delete(self):        
        
        """_summary_
        Suppression de l'attribut de variable dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération du nom de variable choisi dans la liste déroulante
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.currentText()
        # Récupération du nom de l'attribut de variable choisi dans la liste déroulante
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut n'est pas vide, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il y a au minimum plusieurs attributs
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) in catalog['variable'][variable_name]['attribute'] and len(catalog['variable'][variable_name]['attribute']) > 1:
                # Si le nom de l'attribut n'est pas un attribut obligatoire
                if attribute_name not in self.mandatory_variable_attribute_list:
                    # Suppression de l'attribut de variable à partir de l'outil d'agencement
                    catalog = outilsArrangement.variable_attribute_delete(catalog, variable_name, attribute_name)
                    # Ecriture du catalogue
                    self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                    self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.setEnabled(True)
                    self.vuecatalogsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.setEnabled(False)
                    self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable attribute deleted.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable attribute deleted.\n", "green")
                # Sinon
                else:
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The name of a mandatory variable attribute cannot be modified.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The name of a mandatory variable attribute cannot be modified.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name. The model structure must depend on at least 1 attribute. Please enter a new attribute first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name. The model structure must depend on at least 1 attribute. Please enter a new attribute first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")


    def global_attribute_name_add(self):
        
        """_summary_
        Ajout de l'attribut global dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) not in catalog['global_attribute']:
                # Ajout de l'attribut global à partir de l'outil d'agencement
                catalog = outilsArrangement.global_attribute_name_add(catalog, global_attribute_name)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global attribute name added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global attribute name added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global attribute name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global attribute name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_add_confirm(self):
        
        """_summary_
        Confirmation de l'ajout de la valeur de l'attribut global
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) in catalog['global_attribute']:
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global attribute name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global attribute name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global attribute name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global attribute name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_add_cancel(self):
        
        """_summary_
        Annulation de l'ajout de la valeur de l'attribut global
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.setEnabled(False)
    
    
    def global_attribute_value_add(self):
        
        """_summary_
        Ajout de la valeur de l'attribut global dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.currentText()
        # Récupération de la valeur de l'attribut global choisi dans la liste déroulante
        global_attribute_value: str = self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide
            if global_attribute_value != "":
                # Ajout de la valeur de l'attribut global à partir de l'outil d'agencement
                catalog = outilsArrangement.global_attribute_value_add(catalog, global_attribute_name, global_attribute_value)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Information added.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information added.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect information.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect information.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_name_modify_confirm(self):
        
        """_summary_
        Confirmation de la modification de l'attribut global
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) in catalog['global_attribute'] and global_attribute_name not in self.mandatory_global_attribute_list:
                self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global attribute name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global attribute name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global attribute name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global attribute name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_name_modify_cancel(self):
        
        """_summary_
        Annulation de la modification de l'attribut global
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.setEnabled(False)
    
    
    def global_attribute_name_modify(self):
        
        """_summary_
        Modification de l'attribut global dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.currentText()
        # Récupération du nouvel attribut global choisi dans la liste déroulante
        global_attribute_new_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if global_attribute_new_name != "" and any(char.isspace() for char in global_attribute_new_name) == False and global_attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_new_name)) == True:
                # Si le nom du nouvel attribut global n'est pas un attribut global obligatoire
                if global_attribute_new_name not in self.mandatory_global_attribute_list:
                    # Modification de l'attribut global à partir de l'outil d'agencement
                    catalog = outilsArrangement.global_attribute_name_modify(catalog, global_attribute_name, global_attribute_new_name)
                    # Ecriture du catalogue
                    self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                    self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.setEnabled(True)
                    self.vuecatalogsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(False)
                    self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.setEnabled(False)
                    self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global attribute name modified.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global attribute name modified.\n", "green")
                # Sinon
                else:
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The name of a mandatory global attribute cannot be modified.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The name of a mandatory global attribute cannot be modified.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global attribute name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global attribute name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_modify_confirm(self):
        
        """_summary_
        Confirmation de la modification de la valeur de l'attribut global
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) in catalog['global_attribute'] and global_attribute_name != "_FillValue":
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.setEnabled(True)
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global attribute name selected.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global attribute name selected.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global attribute name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global attribute name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_value_modify_cancel(self):
        
        """_summary_
        Annulation de la modification de la valeur de l'attribut global
        """
        
        # Grisage et dégrisage des zones nécessaires
        self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.setEnabled(False)
    
    
    def global_attribute_value_modify(self):
        
        """_summary_
        Modification de la valeur de l'attribut global dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.currentText()
        # Récupération de la valeur du nouvel attribut global choisi dans la liste déroulante
        global_attribute_new_value: str = self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si la nouvelle valeur de l'attribut global n'est pas vide
            if global_attribute_new_value != "":
                # Modification de la valeur de l'attribut global à partir de l'outil d'agencement
                catalog = outilsArrangement.global_attribute_value_modify(catalog, global_attribute_name, global_attribute_new_value)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.setEnabled(True)
                self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(False)
                self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.setEnabled(False)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Information modified.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information modified.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect information.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect information.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def global_attribute_name_delete(self):
        
        """_summary_
        Suppression de l'attribut global dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.delete_name_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il y a au minimum 1 attribut global
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) in catalog['global_attribute'] and len(list(catalog['global_attribute'].keys())) > 1 and global_attribute_name not in self.mandatory_global_attribute_list:
                # Suppression de l'attribut global à partir de l'outil d'agencement
                catalog = outilsArrangement.global_attribute_name_delete(catalog, global_attribute_name)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Global attribute deleted.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global attribute deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global attribute name. The model structure must depend on at least 1 global attribute. Please enter a new global attribute first.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global attribute name. The model structure must depend on at least 1 global attribute. Please enter a new global attribute first.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
        
    def global_attribute_value_delete(self):
        
        """_summary_
        Suppression de la valeur de l'attribut global dans la vue à partir de l'outil d'agencement
        """
        
        # Récupération de l'attribut global choisi dans la liste déroulante
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_combobox.currentText()
        # Lecture du catalogue
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) in catalog['global_attribute'] and global_attribute_name != "_FillValue":
                # Suppression de la valeur de l'attribut global à partir de l'outil d'agencement
                catalog = outilsArrangement.global_attribute_value_delete(catalog, global_attribute_name)
                # Ecriture du catalogue
                self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Information deleted.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information deleted.\n", "green")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global attribute name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global attribute name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
