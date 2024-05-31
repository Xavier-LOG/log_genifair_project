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
        self.datetime_catalog = ['datetime', 'date', 'time', 'temps', 'heure', 'hour', 'minute', 'seconde', 'yyyy-mm-ddthh:mm:ss', 'yyyy/mm/ddthh:mm:ss', 'yyyy-mm-dd hh:mm:ss', 'yyyy/mm/dd hh:mm:ss', 'yyyy-mm-dd', 'yyyy/mm/dd', 'dd-mm-yyyy', 'dd/mm/yyyy', 'hh:mm:ss', 'hh:mm:ss.sss']
        self.optional_dimension_name_list = ['Depth', 'Latitude', 'Longitude', 'Sample', 'Station', 'Time']
        self.optional_dimension_value_list = ['400, 500, 600, 700', '400, 450, 500, 550, 600, 650, 700', '1, 2', '1, 2, 3', '1, 2, 3, 4', '1, 2, 3, 4, 5', '1, 2, 3, 4, 5, 6', '1, 2, 3, 4, 5, 6, 7', '1, 2, 3, 4, 5, 6, 7, 8', '1, 2, 3, 4, 5, 6, 7, 8, 9', '1, 2, 3, 4, 5, 6, 7, 8, 9, 10']
        self.optional_variable_name_list = ['sea_surface_temperature', 'sea_bottom_temperature', 'sea_surface_salinity', 'sea_bottom_salinity', 'sea_surface_pressure', 'sea_bottom_pressure', 'sea_surface_height', 'sea_bottom_depth', 'sea_surface_oxygen_concentration', 'sea_bottom_oxygen_concentration', 'sea_surface_chlorophyll_concentration', 'sea_bottom_chlorophyll_concentration']
        self.mandatory_variable_attribute_list = ['dtype', 'units', 'sdn_uom_name', 'sdn_uom_urn', 'standard_name', 'long_name', 'sdn_parameter_name', 'sdn_paramter_urn']
        self.optional_variable_attribute_list = ['axis', 'calendar', 'comment', 'coverage_content_type', 'inverse_flattening', 'origin', 'scale_factor', 'valid_max', 'valid_min']
        self.mandatory_global_attribute_list = ['_FillValue', 'coordinates', 'title', 'project', 'Conventions', 'institution', 'source', 'request_for_aknowledgement', 'citation', 'license', 'references', 'summary', 'principal_investigator', 'principal_investigator_email', 'metadata_contact', 'contributor_name', 'contributor_role', 'contact', 'featureType', 'cdm_data_type', 'comments', 'history', 'creator_email', 'creator_name', 'creator_url']
        self.optional_global_attribute_list = ['comment', 'date_created', 'date_modified', 'geospatial_lat_max', 'geospatial_lat_min', 'geospatial_lat_resolution', 'geospatial_lat_units', 'geospatial_lon_max', 'geospatial_lon_min', 'geospatial_lon_resolution', 'geospatial_lon_units', 'geospatial_vertical_max', 'geospatial_vertical_min', 'geospatial_vertical_positive', 'geospatial_vertical_resolution', 'keywords', 'keywords_vocabulary', 'platform', 'time_coverage_start', 'time_coverage_end']
        self.catalog_signal = self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.signal
        self.catalog_signal.connect(self.fill_combobox)
        self.dataframe_signal = self.vuecatalogsettings.vuecatalog.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.dataframe_signal.connect(self.set_dataframe)

    
    # Définition des méthodes
    
    
    def set_dataframe(self, obj):
        
        self.dataframe: pd.DataFrame = obj[1][0]
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        if catalog and not self.dataframe.empty:
            if ":time_coverage_start" in catalog['global_attribute'] and ":time_coverage_end" in catalog['global_attribute']:
                for column in self.dataframe.columns:
                    if [word for word in self.datetime_catalog if re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
                        if isinstance(self.dataframe.iloc[0][column], datetime) or isinstance(self.dataframe.iloc[0][column], date):   
                            catalog['global_attribute'][":time_coverage_start"] = self.dataframe.iloc[0][column].strftime("%Y-%m-%d")
                        elif isinstance(self.dataframe.iloc[0][column], time):
                            catalog['global_attribute'][":time_coverage_start"] = self.dataframe.iloc[0][column].strftime("%H:%M:%S")
                        elif isinstance(self.dataframe.iloc[0][column], pd.Timestamp):
                            catalog['global_attribute'][":time_coverage_start"] = datetime.fromtimestamp(self.dataframe.iloc[0][column]).strftime("%Y-%m-%d")
                        elif isinstance(self.dataframe.iloc[0][column], str):
                            catalog['global_attribute'][":time_coverage_start"] = str(self.dataframe.iloc[0][column])
                        if isinstance(self.dataframe.iloc[-1][column], datetime) or isinstance(self.dataframe.iloc[-1][column], date):   
                            catalog['global_attribute'][":time_coverage_end"] = self.dataframe.iloc[-1][column].strftime("%Y-%m-%d")
                        elif isinstance(self.dataframe.iloc[-1][column], time):
                            catalog['global_attribute'][":time_coverage_end"] = self.dataframe.iloc[-1][column].strftime("%H:%M:%S")
                        elif isinstance(self.dataframe.iloc[-1][column], pd.Timestamp):
                            catalog['global_attribute'][":time_coverage_end"] = datetime.fromtimestamp(self.dataframe.iloc[-1][column]).strftime("%Y-%m-%d")
                        elif isinstance(self.dataframe.iloc[-1][column], str):
                            catalog['global_attribute'][":time_coverage_end"] = str(self.dataframe.iloc[-1][column])
    
    
    def eventFilter(self, source, event):
        
        if event.type() == QEvent.Type.ToolTip:
            if source == self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox or source == self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox:
                index = source.currentIndex()
                if index == 0:
                    QToolTip.showText(event.globalPos(), "Indicates the direction of data in a specific dimension, such as time (axis: “T”), etc.")
                elif index == 1:
                    QToolTip.showText(event.globalPos(), "Specifies the type of calendar used to interpret dates (calendar: “gregorian”)")
                elif index == 2:
                    QToolTip.showText(event.globalPos(), "Additional textual description providing explanations and details about a variable")
                elif index == 3:
                    QToolTip.showText(event.globalPos(), "Describes the type of data contained, such as thematic data (coverage_content_type: “coordinate”)")
                elif index == 4:
                    QToolTip.showText(event.globalPos(), "Indicates the measure of the Earth's flatness")
                elif index == 5:
                    QToolTip.showText(event.globalPos(), "Indicates data source (origin: “01-JAN-1970 00:00:00”)")
                elif index == 6:
                    QToolTip.showText(event.globalPos(), "Adjusts stored values to a specific scale (scale_factor: “0.1”)")
                elif index == 7:
                    QToolTip.showText(event.globalPos(), "Specifies the maximum valid value for a given variable")
                elif index == 8:
                    QToolTip.showText(event.globalPos(), "Specifies the minimum valid value for a given variable")
                else:
                    QToolTip.hideText()
            elif source == self.vuecatalogsettings.attribute_tabwidget.add_name_combobox or source == self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox:
                index = source.currentIndex()
                if index == 0:
                    QToolTip.showText(event.globalPos(), "Brief description or remarks on the data contained in the file")
                elif index == 1:
                    QToolTip.showText(event.globalPos(), "Indicates the date on which the file was first created or generated")
                elif index == 2:
                    QToolTip.showText(event.globalPos(), "Indicates the last time the file was modified")
                elif index == 3:
                    QToolTip.showText(event.globalPos(), "Indicates the maximum latitude of geospatial data")
                elif index == 4:
                    QToolTip.showText(event.globalPos(), "Indicates the minimum latitude of geospatial data")
                elif index == 5:
                    QToolTip.showText(event.globalPos(), "Indicates the spatial resolution of the data in latitude")
                elif index == 6:
                    QToolTip.showText(event.globalPos(), "Specifies the unit used to measure latitude, often in degrees north or south of the equator")
                elif index == 7:
                    QToolTip.showText(event.globalPos(), "Indicates the maximum longitude of geospatial data")
                elif index == 8:
                    QToolTip.showText(event.globalPos(), "Indicates the minimum longitude of geospatial data")
                elif index == 9:
                    QToolTip.showText(event.globalPos(), "Indicates the spatial resolution of the data in longitude")
                elif index == 10:
                    QToolTip.showText(event.globalPos(), "Specifies the unit used to measure longitude, often in degrees east or west in relation to the Greenwich meridian")
                elif index == 11:
                    QToolTip.showText(event.globalPos(), "Indicates the maximum value of the geospatial vertical dimension, often used to represent the maximum depth or altitude of geospatial data")
                elif index == 12:
                    QToolTip.showText(event.globalPos(), "Indicates the minimum value of the geospatial vertical dimension, often used to represent the minimum depth or altitude of geospatial data")
                elif index == 13:
                    QToolTip.showText(event.globalPos(), "Indicates the positive direction of the vertical axis, for example “up” to indicate that values increase with altitude")
                elif index == 14:
                    QToolTip.showText(event.globalPos(), "Indicates the precision with which data is represented along the vertical axis")
                elif index == 15:
                    QToolTip.showText(event.globalPos(), "Keywords describing the content and subject of the file")
                elif index == 16:
                    QToolTip.showText(event.globalPos(), "Indicates the vocabulary used to describe the keywords associated with the data")
                elif index == 17:
                    QToolTip.showText(event.globalPos(), "Provides information on the platform from which the data was collected or generated, such as the type of sensor or instrument used")
                elif index == 18:
                    QToolTip.showText(event.globalPos(), "Specifies the start of the period of temporal data coverage")
                elif index == 19:
                    QToolTip.showText(event.globalPos(), "Specifies the end of the period of temporal data coverage")
                else:
                    QToolTip.hideText()
            return True
        return super().eventFilter(source, event)
    
    
    def fill_combobox(self, obj):
        
        catalog = obj
        # Si le catalogue existe
        if catalog:
            
            self.vuecatalogsettings.dimension_tabwidget.add_name_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.add_name_combobox.addItems(self.optional_dimension_name_list)
            
            self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.addItems(self.optional_dimension_value_list)
            
            self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.addItems(list(catalog['dimension'].keys()))
            self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.addItems(self.optional_dimension_name_list)
            self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.addItems(self.optional_dimension_value_list)
            
            self.vuecatalogsettings.dimension_tabwidget.delete_name_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.delete_name_combobox.addItems(list(catalog['dimension'].keys()))
            self.vuecatalogsettings.dimension_tabwidget.delete_value_dimension_combobox.clear()
            self.vuecatalogsettings.dimension_tabwidget.delete_value_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            
            self.vuecatalogsettings.variable_tabwidget.add_name_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.add_name_combobox.addItems(self.optional_variable_name_list)
            self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.addItems(list(catalog['variable'].keys()))
            self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.addItems(self.optional_variable_attribute_list)
            self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.installEventFilter(self)
            self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.clear()
            
            self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.addItems(list(catalog['variable'].keys()))
            self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.addItems(self.optional_variable_name_list)
            self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.addItems(list(catalog['dimension'].keys()))
            
            self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.addItems(list(catalog['variable'].keys()))
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.addItems(self.optional_variable_attribute_list)
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.installEventFilter(self)
            self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.clear()
            
            self.vuecatalogsettings.variable_tabwidget.delete_name_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.delete_name_combobox.addItems(list(catalog['variable'].keys()))
            self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.clear()
            self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.addItems(list(catalog['variable'].keys()))
            
            self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.clear()
            self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.addItems(self.optional_global_attribute_list)
            self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.installEventFilter(self)
            self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.clear()
            self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.clear()
            
            self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.clear()
            self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.clear()
            self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.addItems(self.optional_global_attribute_list)
            self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.installEventFilter(self)
            self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.clear()
            self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.clear()
            
            self.vuecatalogsettings.attribute_tabwidget.delete_name_combobox.clear()
            self.vuecatalogsettings.attribute_tabwidget.delete_name_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
            self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_combobox.clear()
            self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_combobox.addItems([key[1:] for key in list(catalog['global_attribute'].keys())])
    
    
    def fill_catalog(self):
        
        dimension_name: str = ""
        # Si les chemins de fichier existent
        if self.vuecatalogsettings.vuecatalog.modelecatalog.path_list_files[1]:
            # Si le dataframe existe
            if not self.dataframe.empty:
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
                        ":institution": "NaN",
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
                if self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked() or self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_time_series_catalog_checkbox.isChecked():
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
                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                    catalog['global_attribute'][':time_coverage_start'] = "NaN"
                    catalog['global_attribute'][':time_coverage_end'] = "NaN"
                    if self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_trajectory_catalog_checkbox.isChecked():  
                        catalog['global_attribute'][':title'] = "Trajectory"
                        catalog['global_attribute'][':featureType'] = "Trajectory"
                        catalog['global_attribute'][':cdm_data_type'] = "Trajectory"
                    else:
                        catalog['global_attribute'][':title'] = "Timeseries"
                        catalog['global_attribute'][':featureType'] = "TimeSeries"
                        catalog['global_attribute'][':cdm_data_type'] = "TimeSeries"
                elif self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_profile_catalog_checkbox.isChecked():
                    dimension_name = "Depth"
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
                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                    catalog['global_attribute'][':title'] = "Profile"
                    catalog['global_attribute'][':featureType'] = "Profile"
                    catalog['global_attribute'][':cdm_data_type'] = "Profile"
                elif self.vuecatalogsettings.vuecatalog.vuecatalogtype.groupbox_sample_catalog_checkbox.isChecked():
                    dimension_name = "Sample"
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
                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                    catalog['global_attribute'][':title'] = "Sample"
                
                catalog['dimension'][dimension_name] = {
                        "values": []
                }
                catalog['global_attribute'][':date_created'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                
                # Parcours de chaque colonne du dataframe
                for column in self.dataframe.columns:
                    if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower() not in catalog['variable']:
                        if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith('station') or re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith('station'):
                            catalog['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
                                "dimension" : ['Station'],
                                "attribute" : {
                                    ":dtype": str(self.dataframe[column].dtype),
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
                        elif [word for word in ['latitude', 'lat'] if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
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
                        elif [word for word in ['longitude', 'lon'] if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
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
                        elif [word for word in self.datetime_catalog if re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith(word) or re.sub(r'[^a-zA-Z/:.-_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith(word)]:
                            if 'time' not in catalog['variable']:
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
                                if dimension_name not in catalog['global_attribute'][':coordinates']:
                                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
                                if isinstance(self.dataframe.iloc[0][column], datetime) or isinstance(self.dataframe.iloc[0][column], date):   
                                    catalog['global_attribute'][":time_coverage_start"] = self.dataframe.iloc[0][column].strftime("%Y-%m-%d")
                                elif isinstance(self.dataframe.iloc[0][column], time):
                                    catalog['global_attribute'][":time_coverage_start"] = self.dataframe.iloc[0][column].strftime("%H:%M:%S")
                                elif isinstance(self.dataframe.iloc[0][column], pd.Timestamp):
                                    catalog['global_attribute'][":time_coverage_start"] = datetime.fromtimestamp(self.dataframe.iloc[0][column]).strftime("%Y-%m-%d")
                                elif isinstance(self.dataframe.iloc[0][column], str):
                                    catalog['global_attribute'][":time_coverage_start"] = str(self.dataframe.iloc[0][column])
                                if isinstance(self.dataframe.iloc[-1][column], datetime) or isinstance(self.dataframe.iloc[-1][column], date):   
                                    catalog['global_attribute'][":time_coverage_end"] = self.dataframe.iloc[-1][column].strftime("%Y-%m-%d")
                                elif isinstance(self.dataframe.iloc[-1][column], time):
                                    catalog['global_attribute'][":time_coverage_end"] = self.dataframe.iloc[-1][column].strftime("%H:%M:%S")
                                elif isinstance(self.dataframe.iloc[-1][column], pd.Timestamp):
                                    catalog['global_attribute'][":time_coverage_end"] = datetime.fromtimestamp(self.dataframe.iloc[-1][column]).strftime("%Y-%m-%d")
                                elif isinstance(self.dataframe.iloc[-1][column], str):
                                    catalog['global_attribute'][":time_coverage_end"] = str(self.dataframe.iloc[-1][column])
                        else:
                            if not re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith('unnamed'):
                                catalog['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
                                    "dimension" : [dimension_name],
                                    "attribute" : {
                                        ":dtype": str(self.dataframe[column].dtype),
                                        ":units": re.sub(r'[^\u0391-\u03A9\u03B1-\u03C9-a-zA-Z\s/%._]', '', column.split(",")[1].strip("_")).replace(' ','').lower() if len(column.split(",")) == 2 else "NaN",
                                        ":sdn_uom_name": re.sub(r'[^\u0391-\u03A9\u03B1-\u03C9-a-zA-Z\s/%._]', '', column.split(",")[1].strip("_")).replace(' ','').lower() if len(column.split(",")) == 2 else "NaN",
                                        ":sdn_uom_urn": "urn:sdn:parameter:" + re.sub(r'[^\u0391-\u03A9\u03B1-\u03C9-a-zA-Z\s/%._]', '', column.split(",")[1].strip("_")).replace(' ','').lower() if len(column.split(",")) == 2 else "NaN",
                                        ":standard_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower(),
                                        ":long_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace('_', ' ').lower().capitalize(),
                                        ":sdn_parameter_name": re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower(),
                                        ":sdn_paramter_urn": "urn:sdn:parameter:" + str(re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()),
                                        "column_name": str(column)
                                    }
                                }
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
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.add_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il n'est pas dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name not in catalog['dimension'] and dimension_name not in catalog['global_attribute'][':coordinates'].replace(' ', '').split(','):
                catalog['dimension'][dimension_name] = {
                    "values": []
                }
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
                if dimension_name not in catalog['global_attribute'][':coordinates'].replace(' ', '').split(','):
                    catalog['global_attribute'][':coordinates'] += ", " + dimension_name
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
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension']:
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
        
        self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_cancel_button.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.setEnabled(False)
    
    
    def dimension_value_add(self):
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.add_value_dimension_combobox.currentText()
        dimension_value: str = self.vuecatalogsettings.dimension_tabwidget.add_value_combobox.currentText()
        value_checked: int = 0
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
                # Parcours des valeurs de la dimension
                for value in dimension_value.split(','):
                    # Si la valeur contient des points, des chiffres ou des tirets
                    if bool(re.match(r'^[\d\s.-]+$', value)) == True:
                        if (value.count("-") == 0 or value.count("-") == 1) and (value.count(".") == 0 or value.count(".") == 1):
                            if "-" in value and value[0] == "-" and len(value) > 1:
                                if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 2:
                                    value_checked += 1
                                elif "." not in value:
                                    value_checked += 1
                            elif "-" not in value:
                                if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 1:
                                    value_checked += 1
                                elif "." not in value:
                                    value_checked += 1
                # Si toutes les valeurs de la dimension sont correctes
                if value_checked == len(dimension_value.split(',')):
                    catalog['dimension'][dimension_name]['values'] = [word.replace(' ', '') for word in dimension_value.split(',')]
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
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
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
        
        self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.setEnabled(False)
    
    
    def dimension_name_modify(self):
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_name_combobox.currentText()
        dimension_new_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_new_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il n'est pas dans le catalogue
            if dimension_new_name != "" and any(char.isspace() for char in dimension_new_name) == False and dimension_new_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_new_name)) == True and dimension_new_name not in catalog['dimension']:
                catalog['dimension'][dimension_new_name] = {
                    'values': catalog['dimension'][dimension_name]['values']
                }
            
                # Recherche de la variable de la dimension
                for variable_name in catalog['variable']:
                    if 'dimension' in catalog['variable'][variable_name] and dimension_name in catalog['variable'][variable_name]['dimension']:
                        if variable_name == dimension_name.lower():
                            for word in [":axis", ":standard_name", ":long_name", ":sdn_parameter_name", ":sdn_parameter_urn"]:
                                if word in catalog['variable'][variable_name]['attribute']:
                                    if dimension_name.lower() in catalog['variable'][variable_name]['attribute'][word]:
                                        catalog['variable'][variable_name]['attribute'][word] = catalog['variable'][variable_name]['attribute'][word].replace(dimension_name.lower(), dimension_new_name.lower())
                                    elif dimension_name in catalog['variable'][variable_name]['attribute'][word]:
                                        catalog['variable'][variable_name]['attribute'][word] = catalog['variable'][variable_name]['attribute'][word].replace(dimension_name, dimension_new_name)
                            catalog['variable'][dimension_new_name.lower()] = {
                                'dimension' : [word.replace(dimension_name, dimension_new_name) for word in catalog['variable'][variable_name]['dimension']],
                                'attribute' : catalog['variable'][variable_name]['attribute']
                            }
                            del catalog['variable'][variable_name]
                            break
            
                # Recherche des variables ayant pour dimension dimension_name
                for variable_name in catalog['variable']:
                    if 'dimension' in catalog['variable'][variable_name] and dimension_name in catalog['variable'][variable_name]['dimension']:
                        catalog['variable'][variable_name]['dimension'] = [word.replace(dimension_name, dimension_new_name) for word in catalog['variable'][variable_name]['dimension']]
                
                catalog['global_attribute'][':coordinates'] = catalog['global_attribute'][':coordinates'].replace(dimension_name, dimension_new_name)
                
                del catalog['dimension'][dimension_name]
            
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
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
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
        
        self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.setEnabled(True)
        self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_cancel_button.setEnabled(False)
        self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.setEnabled(False)
    
    
    def dimension_value_modify(self):
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.modify_value_dimension_combobox.currentText()
        dimension_value: str = self.vuecatalogsettings.dimension_tabwidget.modify_new_value_combobox.currentText()
        value_checked: int = 0
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Parcours des valeurs de la dimension
            for value in dimension_value.split(','):
                # Si la valeur contient des points, des chiffres ou des tirets
                if bool(re.match(r'^[\d\s.-]+$', value)) == True:
                    if (value.count("-") == 0 or value.count("-") == 1) and (value.count(".") == 0 or value.count(".") == 1):
                        if "-" in value and value[0] == "-" and len(value) > 1:
                            if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 2:
                                value_checked += 1
                            elif "." not in value:
                                value_checked += 1
                        elif "-" not in value:
                            if "." in value and bool(re.search(r'\d\.\d', value)) == True and len(value) > 1:
                                value_checked += 1
                            elif "." not in value:
                                value_checked += 1
            # Si toutes les valeurs de la dimension sont correctes
            if value_checked == len(dimension_value.split(',')) or dimension_value == "":
                if value_checked == len(dimension_value.split(',')):
                    catalog['dimension'][dimension_name]['values'] = [word.replace(' ', '') for word in dimension_value.split(',')]
                elif dimension_value == "":
                    catalog['dimension'][dimension_name]['values'] = []
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
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.delete_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule, s'il n'y a que des lettres ou des chiffres mais pas seulement que des chiffres, s'il est inclu dans le catalogue et s'il y a au minimum plusieurs dimensions
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable'] and len(catalog['dimension']) > 1:
                variables_to_remove = []
                # Recherche des variables ayant pour dimension dimension_name
                for variable_name in catalog['variable']:
                    if 'dimension' in catalog['variable'][variable_name] and dimension_name in catalog['variable'][variable_name]['dimension']:
                        variables_to_remove.append(variable_name)
                        
                # S'il y a au minimum une variable de dimension différente de la dimension à supprimer dans le catalogue
                if len(variables_to_remove) < len(catalog['variable']):
                    for variable in variables_to_remove:
                        if len(catalog['variable'][variable]['dimension']) == 1:
                            # Suppression des variables ayant pour dimension dimension_name
                            del catalog['variable'][variable]
                        elif len(catalog['variable'][variable]['dimension']) == 2:
                            catalog['variable'][variable]['dimension'].remove(dimension_name)
            
                    catalog['global_attribute'][':coordinates'] = ', '.join([word.replace(' ','') for word in catalog['global_attribute'][':coordinates'].split(',') if dimension_name != word.replace(' ','')])
                    
                    del catalog['dimension'][dimension_name]
            
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
        
        dimension_name: str = self.vuecatalogsettings.dimension_tabwidget.delete_value_dimension_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans le catalogue
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in catalog['dimension'] and dimension_name in catalog['global_attribute'][':coordinates'].replace(' ', '').split(',') and dimension_name.lower() in catalog['variable']:
                catalog['dimension'][dimension_name]['values'] = []
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
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name not in catalog['variable']:
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
        
        self.vuecatalogsettings.variable_tabwidget.add_name_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.setEnabled(False)

    
    def variable_name_add(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_name_combobox.currentText()
        variable_dimension: str = self.vuecatalogsettings.variable_tabwidget.add_dimension_combobox.currentText()
        variable_dimension_list: list = []
        variable_dimension_checked: int = 0
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name not in catalog['variable']:
                variable_dimension_list = [word.replace(' ', '') for word in variable_dimension.split(',')]
                for element in variable_dimension_list:
                    if element in catalog['dimension']:
                        variable_dimension_checked += 1
                       
                if variable_dimension_checked == len(variable_dimension_list):
                    if [word for word in ['latitude', 'lat'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in catalog['variable']:
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
                    elif [word for word in ['longitude', 'lon'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in catalog['variable']:
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
                    elif [word for word in ['depth', 'profondeur'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in catalog['variable']:
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
                    elif [word for word in self.datetime_catalog if variable_name.startswith(word) or variable_name.endswith(word)] and 'time' not in catalog['variable']:
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
                        catalog['global_attribute'][':time_coverage_start'] = "NaN"
                        catalog['global_attribute'][':time_coverage_end'] = "NaN"
                    else:
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
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in catalog['variable']:
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
        
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.setEnabled(False)
    
    
    def variable_attribute_add_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.currentText()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut n'est pas vide et si le nom du nouvel attribut ne contient aucun espace blanc
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) not in catalog['variable'][variable_name]['attribute']:
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
        
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.setEnabled(False)
    
    
    def variable_attribute_add(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_variable_combobox.currentText()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_combobox.currentText()
        attribute_value: str = self.vuecatalogsettings.variable_tabwidget.add_attribute_value_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut et de la nouvelle valeur ne sont pas vides et si le nom du nouvel attribut ne contient aucun espace blanc
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) not in catalog['variable'][variable_name]['attribute'] and attribute_value != "":
                catalog['variable'][variable_name]["attribute"][":" + attribute_name] = attribute_value
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
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.currentText()
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
        
        self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(False)
    
    
    def variable_new_name_modify_confirm(self):
        
        variable_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if variable_new_name != "" and any(char.isspace() for char in variable_new_name) == False and variable_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_new_name)) == True:
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
        
        self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.setEnabled(False)
    
    
    def variable_name_modify(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_name_combobox.currentText()
        variable_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_name_combobox.currentText()
        dimension_name: str = self.vuecatalogsettings.variable_tabwidget.modify_dimension_combobox.currentText()
        dimension_name_list: list = []
        dimension_name_checked: int = 0
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if variable_new_name != "" and any(char.isspace() for char in variable_new_name) == False and variable_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_new_name)) == True:
                dimension_name_list = [word.replace(' ', '') for word in dimension_name.split(',')]
                for element in dimension_name_list:
                    if element in catalog['dimension']:
                        dimension_name_checked += 1
                        
                if dimension_name_checked == len(dimension_name_list):
                    if len(catalog['variable'][variable_name]['dimension']) == 1:
                        if variable_new_name != "time" and variable_new_name.capitalize() != catalog['variable'][variable_new_name]['dimension'][0]:
                            catalog['variable'][variable_new_name] = {
                                "dimension" : dimension_name_list,
                                "attribute" : catalog['variable'][variable_name]['attribute']
                            }
                            if variable_new_name != variable_name:
                                del catalog['variable'][variable_name]
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
                    elif len(catalog['variable'][variable_name]['dimension']) > 1:
                        catalog['variable'][variable_new_name] = {
                            "dimension" : dimension_name_list,
                            "attribute" : catalog['variable'][variable_name]['attribute']
                        }
                        if variable_new_name != variable_name:
                            del catalog['variable'][variable_name]
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
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.currentText()
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
        
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)
    
    
    def variable_attribute_modify_confirm(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.currentText()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut n'est pas vide, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il n'est pas un attribut obligatoire
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) in catalog['variable'][variable_name]['attribute'] and attribute_name not in self.mandatory_variable_attribute_list:
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
        
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)


    def variable_new_attribute_modify_confirm(self):
        
        attribute_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut n'est pas vide, si la première lettre est en minuscule et s'il n'est pas un attribut obligatoire
            if attribute_new_name != "" and any(char.isspace() for char in attribute_new_name) == False and attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_new_name)) == True and attribute_new_name not in self.mandatory_variable_attribute_list:
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
        
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.setEnabled(False)


    def variable_attribute_modify(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_variable_combobox.currentText()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.modify_attribute_combobox.currentText()
        attribute_new_name: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_combobox.currentText()
        attribute_new_value: str = self.vuecatalogsettings.variable_tabwidget.modify_new_attribute_value_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut n'est pas vide, si la première lettre est en minuscule et si la nouvelle valeur de l'attribut n'est pas vide
            if attribute_new_name != "" and any(char.isspace() for char in attribute_new_name) == False and attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_new_name)) == True and attribute_new_value != "":
                # Si le nom du nouvel attribut n'est pas un attribut obligatoire
                if attribute_new_name not in self.mandatory_variable_attribute_list:
                    catalog['variable'][variable_name]['attribute'][":" + attribute_new_name] = catalog['variable'][variable_name]['attribute'].pop(":" + attribute_name)
                    catalog['variable'][variable_name]['attribute'][":" + attribute_new_name] = attribute_new_value
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
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The name of a mandatory variable attribute cannot be modified.\n")
                    self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The name of a mandatory variable attribute cannot be modified.\n", "red")
            # Sinon
            else:
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown catalog type.\n")
            self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown catalog type.\n", "red")
    
    
    def variable_name_delete(self):
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il y a au minimum plusieurs variables
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in catalog['variable'] and len(catalog['variable']) > 1:
                if len(catalog['variable'][variable_name]['dimension']) == 1:
                    # Si le nom de la variable n'est pas celui d'une variable de dimension
                    if variable_name != "time" and variable_name.capitalize() != catalog['variable'][variable_name]['dimension'][0]:
                        del catalog['variable'][variable_name]
                        self.vuecatalogsettings.vuecatalog.modelecatalog.write_json(catalog)
                        self.vuecatalogsettings.vuecatalog.vuecatalogviewer.controleurcatalogviewer.load_catalog()
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("Variable deleted.\n")
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable deleted.\n", "green")
                    # Sinon
                    else:
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_log("The variable " + variable_name + " of the dimension " + catalog['variable'][variable_name]['dimension'][0] + " cannot be deleted.\n")
                        self.vuecatalogsettings.vuecatalog.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The variable " + variable_name + " of the dimension " + catalog['variable'][variable_name]['dimension'][0] + " cannot be deleted.\n", "red")
                elif len(catalog['variable'][variable_name]['dimension']) > 1:
                    del catalog['variable'][variable_name]
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
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.currentText()
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
        
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.setEnabled(True)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.setEnabled(False)
    
    
    def variable_attribute_delete(self):        
        
        variable_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_variable_combobox.currentText()
        attribute_name: str = self.vuecatalogsettings.variable_tabwidget.delete_attribute_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut n'est pas vide, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il y a au minimum plusieurs attributs
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and (":" + attribute_name) in catalog['variable'][variable_name]['attribute'] and len(catalog['variable'][variable_name]['attribute']) > 1:
                # Si le nom de l'attribut n'est pas un attribut obligatoire
                if attribute_name not in self.mandatory_variable_attribute_list:
                    del catalog['variable'][variable_name]['attribute'][":" + attribute_name]
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
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) not in catalog['global_attribute']:
                catalog['global_attribute'][":" + global_attribute_name] = "NaN"
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
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.currentText()
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
        
        self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.setEnabled(False)
    
    
    def global_attribute_value_add(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.add_value_attribute_combobox.currentText()
        global_attribute_value: str = self.vuecatalogsettings.attribute_tabwidget.add_value_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide
            if global_attribute_value != "":
                catalog['global_attribute'][":" + global_attribute_name] = global_attribute_value
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
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.currentText()
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
        
        self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.setEnabled(False)
    
    
    def global_attribute_name_modify(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_name_combobox.currentText()
        global_attribute_new_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_new_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if global_attribute_new_name != "" and any(char.isspace() for char in global_attribute_new_name) == False and global_attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_new_name)) == True:
                # Si le nom du nouvel attribut global n'est pas un attribut global obligatoire
                if global_attribute_new_name not in self.mandatory_global_attribute_list:
                    catalog['global_attribute'][":" + global_attribute_new_name] = catalog['global_attribute'][":" + global_attribute_name]
                    del catalog['global_attribute'][":" + global_attribute_name]
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
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.currentText()
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
        
        self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.setEnabled(True)
        self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(False)
        self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.setEnabled(False)
    
    
    def global_attribute_value_modify(self):
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.modify_value_attribute_combobox.currentText()
        global_attribute_new_value: str = self.vuecatalogsettings.attribute_tabwidget.modify_new_value_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si la nouvelle valeur de l'attribut global n'est pas vide
            if global_attribute_new_value != "":
                catalog['global_attribute'][":" + global_attribute_name] = global_attribute_new_value
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
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.delete_name_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule, s'il est inclu dans le catalogue et s'il y a au minimum 1 attribut global
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) in catalog['global_attribute'] and len(list(catalog['global_attribute'].keys())) > 1 and global_attribute_name not in self.mandatory_global_attribute_list:
                del catalog['global_attribute'][":" + global_attribute_name]
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
        
        global_attribute_name: str = self.vuecatalogsettings.attribute_tabwidget.delete_value_attribute_combobox.currentText()
        catalog = self.vuecatalogsettings.vuecatalog.modelecatalog.read_json()
        # Si le catalogue existe
        if catalog:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans le catalogue
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and (":" + global_attribute_name) in catalog['global_attribute'] and global_attribute_name != "_FillValue":
                catalog['global_attribute'][":" + global_attribute_name] = "NaN"
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
