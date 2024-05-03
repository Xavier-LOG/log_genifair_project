# Importation des bibliothèques




import pandas as pd
from datetime import datetime
import re




# Définition de la classe controleurArrangementsettings




class controleurArrangementsettings:


    # Constructeur par défaut
        
    
    def __init__(self, vuearrangementsettings):
        
        super().__init__()
        self.vuearrangementsettings = vuearrangementsettings
        self.dataframe = pd.DataFrame()
        self.signal = self.vuearrangementsettings.vuearrangement.vuemainwindow.vuetoolbar.controleurtoolbar.signal
        self.signal.connect(self.set_dataframe)

    
    # Définition des méthodes
    
    
    def set_dataframe(self, obj):
        
        self.dataframe = obj[1][0]
    
    
    def fill_arrangement(self):
        
        dimension_name: str = ""
        # Si les chemins de fichier existent
        if self.vuearrangementsettings.vuearrangement.modelearrangement.path_list_files[1]:
            # Si le dataframe existe
            if not self.dataframe.empty:
                arrangement = {
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
                        ":Conventions": "CF-1.6, SeaDataNet_1.0",
                        ":institution": "NaN",
                        ":source": "NaN",
                        ":request_for_aknowledgement": "If you use the data in presentation or in publications, please acknowledge. Send us also a reprint or preprint of publications using the data for inclusion in our bibliography.",
                        ":citation": "NaN",
                        ":license": "The data is not intended for legal use. However, it may be used and redistributed for free.",
                        ":summary": "NaN",
                        ":principal_investigator": "NaN",
                        ":principal_investigator_email": "NaN",
                        ":metadata_contact": "NaN",
                        ":contributor_name": "NaN",
                        ":contributor_role": "NaN",
                        ":contact": "NaN",
                        ":comments": "NaN",
                        ":history": "NaN"
                    }
                }
                if self.vuearrangementsettings.vuearrangement.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.isChecked() or self.vuearrangementsettings.vuearrangement.vuearrangementtype.groupbox_time_series_arrangement_checkbox.isChecked():
                    dimension_name = "Time"
                    arrangement['variable'][dimension_name.lower()] = {
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
                    arrangement['global_attribute'][':coordinates'] = dimension_name
                    arrangement['global_attribute'][':time_coverage_start'] = "NaN"
                    arrangement['global_attribute'][':time_coverage_end'] = "NaN"
                    arrangement['global_attribute'][':update_interval'] = "NaN"
                    if self.vuearrangementsettings.vuearrangement.vuearrangementtype.groupbox_trajectory_arrangement_checkbox.isChecked():  
                        arrangement['global_attribute'][':title'] = "Trajectory"
                        arrangement['global_attribute'][':featureType'] = "Trajectory"
                        arrangement['global_attribute'][':cdm_data_type'] = "Trajectory"
                    else:
                        arrangement['global_attribute'][':title'] = "Timeseries"
                        arrangement['global_attribute'][':featureType'] = "TimeSeries"
                        arrangement['global_attribute'][':cdm_data_type'] = "TimeSeries"
                elif self.vuearrangementsettings.vuearrangement.vuearrangementtype.groupbox_profile_arrangement_checkbox.isChecked():
                    dimension_name = "Depth"
                    arrangement['variable'][dimension_name.lower()] = {
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
                    arrangement['global_attribute'][':coordinates'] = dimension_name
                    arrangement['global_attribute'][':title'] = "Profile"
                    arrangement['global_attribute'][':featureType'] = "Profile"
                    arrangement['global_attribute'][':cdm_data_type'] = "Profile"
                elif self.vuearrangementsettings.vuearrangement.vuearrangementtype.groupbox_sample_arrangement_checkbox.isChecked():
                    dimension_name = "Sample"
                    arrangement['variable'][dimension_name.lower()] = {
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
                    arrangement['global_attribute'][':coordinates'] = dimension_name
                    arrangement['global_attribute'][':title'] = "Sample"
                
                arrangement['dimension'][dimension_name] = {
                        "values": []
                }
                arrangement['global_attribute'][':date_created'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                
                # Parcours de chaque colonne du dataframe
                for column in self.dataframe.columns:
                    if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower() not in arrangement['variable']:
                        if re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().startswith('station') or re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower().endswith('station'):
                            arrangement['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
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
                            arrangement['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
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
                            arrangement['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
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
                        else:
                            arrangement['variable'][re.sub(r'[^a-zA-Z0-9\s_]', '', column.split(",")[0].strip("_")).replace(' ','_').lower()] = {
                                "dimension" : [dimension_name],
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
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()            
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Empty dataframe. Arrangement will not be filled.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Empty dataframe. Arrangement will not be filled.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("No path file. Arrangement will not be filled.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("No path file. Arrangement will not be filled.\n", "red")
    
    
    def dimension_name_add(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.add_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il n'est pas dans l'agencement
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name not in arrangement['dimension'] and dimension_name not in arrangement['global_attribute'][':coordinates'] and dimension_name.lower() not in arrangement['variable']:
                arrangement['dimension'][dimension_name] = {
                    "values": []
                }
                arrangement['variable'][dimension_name.lower()] = {
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
                arrangement['global_attribute'][':coordinates'] += ", " + dimension_name
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension added.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension added.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def dimension_value_add_confirm(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et s'il est inclu dans l'agencement
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in arrangement['dimension']:
                self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_lineedit.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_confirm_button.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_cancel_button.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.add_value_lineedit.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.add_value_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def dimension_value_add_cancel(self):
        
        self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_lineedit.setEnabled(True)
        self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_confirm_button.setEnabled(True)
        self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_cancel_button.setEnabled(False)
        self.vuearrangementsettings.dimension_tabwidget.add_value_lineedit.setEnabled(False)
        self.vuearrangementsettings.dimension_tabwidget.add_value_button.setEnabled(False)
    
    
    def dimension_value_add(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_lineedit.text()
        dimension_value: str = self.vuearrangementsettings.dimension_tabwidget.add_value_lineedit.text()
        value_checked: int = 0
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Parcours des valeurs de la dimension
            for value in dimension_value.split(','):
                # Si la valeur est un nombre entier ou flottant
                if bool(re.match(r'^[\d.]+$', value)) == True:
                    value_checked += 1
            # Si toutes les valeurs de la dimension sont correctes
            if value_checked == len(dimension_value.split(',')):
                arrangement['dimension'][dimension_name]['values'] = [word.replace(' ', '') for word in dimension_value.split(',')]
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_lineedit.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_confirm_button.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.add_value_dimension_cancel_button.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.add_value_lineedit.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.add_value_button.setEnabled(False)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension value added.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension value added.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension values.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension values.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
            
    
    def dimension_name_modify_confirm(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.modify_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans l'agencement
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in arrangement['dimension'] and dimension_name in arrangement['global_attribute'][':coordinates'] and dimension_name.lower() in arrangement['variable']:
                self.vuearrangementsettings.dimension_tabwidget.modify_name_lineedit.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_name_confirm_button.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_name_lineedit.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_name_modify_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
        
    
    def dimension_name_modify_cancel(self):
        
        self.vuearrangementsettings.dimension_tabwidget.modify_name_lineedit.setEnabled(True)
        self.vuearrangementsettings.dimension_tabwidget.modify_name_confirm_button.setEnabled(True)
        self.vuearrangementsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuearrangementsettings.dimension_tabwidget.modify_new_name_lineedit.setEnabled(False)
        self.vuearrangementsettings.dimension_tabwidget.modify_new_name_modify_button.setEnabled(False)
    
    
    def dimension_name_modify(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.modify_name_lineedit.text()
        dimension_new_name: str = self.vuearrangementsettings.dimension_tabwidget.modify_new_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la nouvelle dimension n'est pas vide, s'il ne contient aucun espace blanc et si le premier caractère est en majuscule
            if dimension_new_name != "" and any(char.isspace() for char in dimension_new_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_new_name)) == True:
                arrangement['dimension'][dimension_new_name] = {
                    'values': arrangement['dimension'][dimension_name]['values']
                }
            
                # Recherche des variables ayant pour dimension dimension_name
                for variable_name in arrangement['variable']:
                    if 'dimension' in arrangement['variable'][variable_name] and dimension_name in arrangement['variable'][variable_name]['dimension']:
                        arrangement['variable'][variable_name]['dimension'] = [word.replace(dimension_name, dimension_new_name) for word in arrangement['variable'][variable_name]['dimension']]
                
                arrangement['global_attribute'][':coordinates'] = arrangement['global_attribute'][':coordinates'].replace(dimension_name, dimension_new_name)
                
                del arrangement['dimension'][dimension_name]
            
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.dimension_tabwidget.modify_name_lineedit.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_name_confirm_button.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_name_cancel_button.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_name_lineedit.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_name_modify_button.setEnabled(False)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name modified.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name modified.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")


    def dimension_value_modify_confirm(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans l'agencement
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in arrangement['dimension'] and dimension_name in arrangement['global_attribute'][':coordinates'] and dimension_name.lower() in arrangement['variable']:
                self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_lineedit.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_confirm_button.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_cancel_button.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_value_lineedit.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_value_modify_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def dimension_value_modify_cancel(self):
        
        self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_lineedit.setEnabled(True)
        self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_confirm_button.setEnabled(True)
        self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_cancel_button.setEnabled(False)
        self.vuearrangementsettings.dimension_tabwidget.modify_new_value_lineedit.setEnabled(False)
        self.vuearrangementsettings.dimension_tabwidget.modify_new_value_modify_button.setEnabled(False)
    
    
    def dimension_value_modify(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_lineedit.text()
        dimension_value: str = self.vuearrangementsettings.dimension_tabwidget.modify_new_value_lineedit.text()
        value_checked: int = 0
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Parcours des valeurs de la dimension
            for value in dimension_value.split(','):
                # Si la valeur est un nombre entier ou flottant
                if bool(re.match(r'^[\d.]+$', value)) == True:
                    value_checked += 1
            # Si toutes les valeurs de la dimension sont correctes
            if value_checked == len(dimension_value.split(',')):
                arrangement['dimension'][dimension_name]['values'] = [word.replace(' ', '') for word in dimension_value.split(',')]
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_lineedit.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_confirm_button.setEnabled(True)
                self.vuearrangementsettings.dimension_tabwidget.modify_value_dimension_cancel_button.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_value_lineedit.setEnabled(False)
                self.vuearrangementsettings.dimension_tabwidget.modify_new_value_modify_button.setEnabled(False)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension value modified.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension value modified.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension values.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension values.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")

    
    def dimension_name_delete(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.delete_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule, s'il n'y a que des lettres ou des chiffres mais pas seulement que des chiffres, s'il est inclu dans l'agencement et s'il y a au minimum plusieurs dimensions
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in arrangement['dimension'] and dimension_name in arrangement['global_attribute'][':coordinates'] and dimension_name.lower() in arrangement['variable'] and len(arrangement['dimension']) > 1:
                variables_to_remove = []
                # Recherche des variables ayant pour dimension dimension_name
                for variable_name in arrangement['variable']:
                    if 'dimension' in arrangement['variable'][variable_name] and dimension_name in arrangement['variable'][variable_name]['dimension']:
                        variables_to_remove.append(variable_name)
                        
                # S'il y a au minimum une variable de dimension différente de la dimension à supprimer dans l'agencement
                if len(variables_to_remove) < len(arrangement['variable']):
                    for variable in variables_to_remove:
                        if len(arrangement['variable'][variable]['dimension']) == 1:
                            # Suppression des variables ayant pour dimension dimension_name
                            del arrangement['variable'][variable]
                        elif len(arrangement['variable'][variable]['dimension']) == 2:
                            arrangement['variable'][variable]['dimension'].remove(dimension_name)
            
                    arrangement['global_attribute'][':coordinates'] = arrangement['global_attribute'][':coordinates'].replace(dimension_name, '')
                    
                    del arrangement['dimension'][dimension_name]
            
                    self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                    self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension name deleted.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension name deleted.\n", "green")
                # Sinon
                else:
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("The model structure must depend on at least 1 variable. Please enter a new variable with another dimension first.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The model structure must depend on at least 1 variable. Please enter a new variable with another dimension first.\n", "red")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name. The model structure must depend on at least 1 dimension. Please enter a new dimension first.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name. The model structure must depend on at least 1 dimension. Please enter a new dimension first.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def dimension_value_delete(self):
        
        dimension_name: str = self.vuearrangementsettings.dimension_tabwidget.delete_value_dimension_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la dimension n'est pas vide, s'il ne contient aucun espace blanc, si le premier caractère est en majuscule et s'il est inclu dans l'agencement
            if dimension_name != "" and any(char.isspace() for char in dimension_name) == False and dimension_name[0].isupper() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', dimension_name)) == True and dimension_name in arrangement['dimension'] and dimension_name in arrangement['global_attribute'][':coordinates'] and dimension_name.lower() in arrangement['variable']:
                arrangement['dimension'][dimension_name]['values'] = []
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Dimension value deleted.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Dimension value deleted.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_name_add(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.add_name_lineedit.text()
        variable_dimension: str = self.vuearrangementsettings.variable_tabwidget.add_dimension_lineedit.text()
        variable_dimension_list: list = []
        variable_dimension_checked: int = 0
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans l'agencement
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name not in arrangement['variable']:
                variable_dimension_list = [word.replace(' ', '') for word in variable_dimension.split(',')]
                for element in variable_dimension_list:
                    if element in arrangement['dimension']:
                        variable_dimension_checked += 1
                       
                if variable_dimension_checked == len(variable_dimension_list):
                    if [word for word in ['latitude', 'lat'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in arrangement['variable']:
                        arrangement['variable'][variable_name] = {
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
                    elif [word for word in ['longitude', 'lon'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in arrangement['variable']:
                        arrangement['variable'][variable_name] = {
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
                    elif [word for word in ['depth', 'profondeur'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in arrangement['variable']:
                        arrangement['variable'][variable_name] = {
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
                    elif [word for word in ['time', 'temps', 'date'] if variable_name.startswith(word) or variable_name.endswith(word)] and variable_name not in arrangement['variable']:
                        arrangement['variable'][variable_name] = {
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
                                ":standard_name": variable_name,
                                ":long_name": variable_name.replace('_', ' ').capitalize(),
                                ":sdn_parameter_name": "Elapsed time relative to 1970-01-01T00:00:00Z",
                                ":sdn_paramter_urn": "SDN:P01::ELTMEP01",
                                "column_name": "datetime"
                            }
                        }
                    else:
                        arrangement['variable'][variable_name] = {
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
                    self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                    self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name added.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name added.\n", "green")
                # Sinon
                else:
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension.\n", "red")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_attribute_add_confirm(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la nouvelle variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in arrangement['variable']:
                self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_confirm_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_value_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_attribute_add_cancel(self):
        
        self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_lineedit.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_confirm_button.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.add_attribute_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.add_attribute_value_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.add_attribute_button.setEnabled(False)
    
    
    def variable_attribute_add(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_lineedit.text()
        attribute_name: str = self.vuearrangementsettings.variable_tabwidget.add_attribute_lineedit.text()
        attribute_value: str = self.vuearrangementsettings.variable_tabwidget.add_attribute_value_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom du nouvel attribut et de la nouvelle valeur ne sont pas vides et si le nom du nouvel attribut ne contient aucun espace blanc
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and attribute_name not in arrangement['variable'][variable_name]['attribute'] and attribute_value != "":
                arrangement['variable'][variable_name]["attribute"][":" + attribute_name] = attribute_value
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_confirm_button.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_variable_cancel_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_value_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.add_attribute_button.setEnabled(False)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information name added.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information name added.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_name_modify_confirm(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.modify_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in arrangement['variable']:
                self.vuearrangementsettings.variable_tabwidget.modify_name_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_name_confirm_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_new_name_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_dimension_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_new_name_modify_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_name_modify_cancel(self):
        
        self.vuearrangementsettings.variable_tabwidget.modify_name_lineedit.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.modify_name_confirm_button.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_name_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_dimension_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_name_modify_button.setEnabled(False)
    
    
    def variable_name_modify(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.modify_name_lineedit.text()
        variable_new_name: str = self.vuearrangementsettings.variable_tabwidget.modify_new_name_lineedit.text()
        dimension_name: str = self.vuearrangementsettings.variable_tabwidget.modify_dimension_lineedit.text()
        dimension_name_list: list = []
        dimension_name_checked: int = 0
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True:
                dimension_name_list = [word.replace(' ', '') for word in dimension_name.split(',')]
                for element in dimension_name_list:
                    if element in arrangement['dimension']:
                        dimension_name_checked += 1
                        
                if dimension_name_checked == len(dimension_name_list):
                    arrangement['variable'][variable_new_name] = {
                        "dimension" : dimension_name_list,
                        "attribute" : arrangement['variable'][variable_name]['attribute']
                    }
                    if variable_new_name != variable_name:
                        del arrangement['variable'][variable_name]
                    self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                    self.vuearrangementsettings.variable_tabwidget.modify_name_lineedit.setEnabled(True)
                    self.vuearrangementsettings.variable_tabwidget.modify_name_confirm_button.setEnabled(True)
                    self.vuearrangementsettings.variable_tabwidget.modify_name_cancel_button.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_new_name_lineedit.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_dimension_lineedit.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_new_name_modify_button.setEnabled(False)
                    self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name and dimension name modified.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name and dimension name modified.\n", "green")
                # Sinon
                else:
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect dimension.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect dimension.\n", "red")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_attribute_variable_modify_confirm(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in arrangement['variable']:
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_attribute_variable_modify_cancel(self):
        
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)
    
    
    def variable_attribute_modify_confirm(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.text()
        attribute_name: str = self.vuearrangementsettings.variable_tabwidget.modify_attribute_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de l'attribut n'est pas vide, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and attribute_name in arrangement['variable'][variable_name]['attribute']:
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_attribute_modify_cancel(self):
        
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)


    def variable_attribute_modify(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.text()
        attribute_name: str = self.vuearrangementsettings.variable_tabwidget.modify_attribute_lineedit.text()
        attribute_new_name: str = self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_lineedit.text()
        attribute_new_value: str = self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_value_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom du nouvel attribut n'est pas vide, si la première lettre est en minuscule et si la nouvelle valeur de l'attribut n'est pas vide
            if attribute_new_name != "" and any(char.isspace() for char in attribute_new_name) == False and attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_new_name)) == True and attribute_new_value != "":
                # Si le nom du nouvel attribut n'est pas un attribut obligatoire
                if attribute_new_name not in ['dtype', 'units', 'sdn_uom_name', 'sdn_uom_urn', 'standard_name', 'long_name', 'sdn_parameter_name', 'sdn_paramter_urn']:
                    arrangement['variable'][variable_name]['attribute'][":" + attribute_new_name] = arrangement['variable'][variable_name]['attribute'].pop(":" + attribute_name)
                    arrangement['variable'][variable_name]['attribute'][":" + attribute_new_name] = attribute_new_value
                    self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                    self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_lineedit.setEnabled(True)
                    self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_confirm_button.setEnabled(True)
                    self.vuearrangementsettings.variable_tabwidget.modify_attribute_variable_cancel_button.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_attribute_lineedit.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_attribute_confirm_button.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_attribute_cancel_button.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_lineedit.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_value_lineedit.setEnabled(False)
                    self.vuearrangementsettings.variable_tabwidget.modify_new_attribute_modify_button.setEnabled(False)
                    self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information name modified.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information name modified.\n", "green")
                # Sinon
                else:
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("The name of a mandatory variable attribute cannot be modified.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The name of a mandatory variable attribute cannot be modified.\n", "red")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_name_delete(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.delete_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule, s'il est inclu dans l'agencement et s'il y a au minimum plusieurs variables
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in arrangement['variable'] and len(arrangement['variable']) > 1:
                del arrangement['variable'][variable_name]
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable deleted.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable deleted.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name. The model structure must depend on at least 1 variable. Please enter a new variable first.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name. The model structure must depend on at least 1 variable. Please enter a new variable first.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_attribute_delete_confirm(self):
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.delete_attribute_variable_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de la variable n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if variable_name != "" and any(char.isspace() for char in variable_name) == False and variable_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', variable_name)) == True and variable_name in arrangement['variable']:
                self.vuearrangementsettings.variable_tabwidget.delete_attribute_variable_lineedit.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.delete_attribute_confirm_button.setEnabled(False)
                self.vuearrangementsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.delete_attribute_lineedit.setEnabled(True)
                self.vuearrangementsettings.variable_tabwidget.delete_attribute_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def variable_attribute_delete_cancel(self):
        
        self.vuearrangementsettings.variable_tabwidget.delete_attribute_variable_lineedit.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.delete_attribute_confirm_button.setEnabled(True)
        self.vuearrangementsettings.variable_tabwidget.delete_attribute_cancel_button.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.delete_attribute_lineedit.setEnabled(False)
        self.vuearrangementsettings.variable_tabwidget.delete_attribute_button.setEnabled(False)
    
    
    def variable_attribute_delete(self):        
        
        variable_name: str = self.vuearrangementsettings.variable_tabwidget.delete_attribute_variable_lineedit.text()
        attribute_name: str = self.vuearrangementsettings.variable_tabwidget.delete_attribute_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de l'attribut n'est pas vide, si la première lettre est en minuscule, s'il est inclu dans l'agencement et s'il y a au minimum plusieurs attributs
            if attribute_name != "" and any(char.isspace() for char in attribute_name) == False and attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', attribute_name)) == True and attribute_name in arrangement['variable'][variable_name]['attribute'] and len(arrangement['variable'][variable_name]['attribute']) > 1:
                # Si le nom de l'attribut n'est pas un attribut obligatoire
                if attribute_name not in ['dtype', 'units', 'sdn_uom_name', 'sdn_uom_urn', 'standard_name', 'long_name', 'sdn_parameter_name', 'sdn_paramter_urn']:
                    del arrangement['variable'][variable_name]['attribute'][":" + attribute_name]
                    self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                    self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Variable information deleted.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Variable information deleted.\n", "green")
                # Sinon
                else:
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("The name of a mandatory variable attribute cannot be modified.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The name of a mandatory variable attribute cannot be modified.\n", "red")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect variable information name. The model structure must depend on at least 1 attribute. Please enter a new attribute first.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect variable information name. The model structure must depend on at least 1 attribute. Please enter a new attribute first.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")


    def global_attribute_name_add(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.add_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il n'est pas dans l'agencement
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and global_attribute_name not in arrangement['global_attribute']:
                arrangement['global_attribute'][":" + global_attribute_name] = "NaN"
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name added.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name added.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_value_add_confirm(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and global_attribute_name in arrangement['global_attribute']:
                self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_lineedit.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_confirm_button.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.add_value_lineedit.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.add_value_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_value_add_cancel(self):
        
        self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_lineedit.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_confirm_button.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(False)
        self.vuearrangementsettings.attribute_tabwidget.add_value_lineedit.setEnabled(False)
        self.vuearrangementsettings.attribute_tabwidget.add_value_button.setEnabled(False)
    
    
    def global_attribute_value_add(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_lineedit.text()
        global_attribute_value: str = self.vuearrangementsettings.attribute_tabwidget.add_value_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom du nouvel attribut global n'est pas vide
            if global_attribute_value != "":
                arrangement['global_attribute'][":" + global_attribute_name] = global_attribute_value
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_lineedit.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_confirm_button.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.add_value_attribute_cancel_button.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.add_value_lineedit.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.add_value_button.setEnabled(False)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Information added.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information added.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect information.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect information.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_name_modify_confirm(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.modify_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and global_attribute_name in arrangement['global_attribute']:
                self.vuearrangementsettings.attribute_tabwidget.modify_name_lineedit.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.modify_name_confirm_button.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.modify_new_name_lineedit.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.modify_new_name_modify_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_name_modify_cancel(self):
        
        self.vuearrangementsettings.attribute_tabwidget.modify_name_lineedit.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.modify_name_confirm_button.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(False)
        self.vuearrangementsettings.attribute_tabwidget.modify_new_name_lineedit.setEnabled(False)
        self.vuearrangementsettings.attribute_tabwidget.modify_new_name_modify_button.setEnabled(False)
    
    
    def global_attribute_name_modify(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.modify_name_lineedit.text()
        global_attribute_new_name: str = self.vuearrangementsettings.attribute_tabwidget.modify_new_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom du nouvel attribut global n'est pas vide, s'il ne contient aucun espace blanc et si la première lettre est en minuscule
            if global_attribute_new_name != "" and any(char.isspace() for char in global_attribute_new_name) == False and global_attribute_new_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_new_name)) == True:
                # Si le nom du nouvel attribut global n'est pas un attribut global obligatoire
                if global_attribute_new_name not in ['_FillValue', 'coordinates', 'date_created', 'time_coverage_start', 'time_coverage_end', 'update_interval', 'title', 'project', 'Conventions', 'institution', 'source', 'request_for_aknowledgement', 'citation', 'license', 'summary', 'principal_investigator', 'principal_investigator_email', 'metadata_contact', 'contributor_name', 'contributor_role', 'contact', 'featureType', 'cdm_data_type', 'comments', 'history']:
                    arrangement['global_attribute'][":" + global_attribute_new_name] = arrangement['global_attribute'][":" + global_attribute_name]
                    del arrangement['global_attribute'][":" + global_attribute_name]
                    self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                    self.vuearrangementsettings.attribute_tabwidget.modify_name_lineedit.setEnabled(True)
                    self.vuearrangementsettings.attribute_tabwidget.modify_name_confirm_button.setEnabled(True)
                    self.vuearrangementsettings.attribute_tabwidget.modify_name_cancel_button.setEnabled(False)
                    self.vuearrangementsettings.attribute_tabwidget.modify_new_name_lineedit.setEnabled(False)
                    self.vuearrangementsettings.attribute_tabwidget.modify_new_name_modify_button.setEnabled(False)
                    self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name modified.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name modified.\n", "green")
                # Sinon
                else:
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("The name of a mandatory global attribute cannot be modified.\n")
                    self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("The name of a mandatory global attribute cannot be modified.\n", "red")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_value_modify_confirm(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and global_attribute_name in arrangement['global_attribute']:
                self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_lineedit.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_confirm_button.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.modify_new_value_lineedit.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.modify_new_value_modify_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_value_modify_cancel(self):
        
        self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_lineedit.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_confirm_button.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(False)
        self.vuearrangementsettings.attribute_tabwidget.modify_new_value_lineedit.setEnabled(False)
        self.vuearrangementsettings.attribute_tabwidget.modify_new_value_modify_button.setEnabled(False)
    
    
    def global_attribute_value_modify(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_lineedit.text()
        global_attribute_new_value: str = self.vuearrangementsettings.attribute_tabwidget.modify_new_value_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si la nouvelle valeur de l'attribut global n'est pas vide
            if global_attribute_new_value != "":
                arrangement['global_attribute'][":" + global_attribute_name] = global_attribute_new_value
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_lineedit.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_confirm_button.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.modify_value_attribute_cancel_button.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.modify_new_value_lineedit.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.modify_new_value_modify_button.setEnabled(False)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Information modified.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information modified.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect information.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect information.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_name_delete(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.delete_name_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule, s'il est inclu dans l'agencement et s'il y a au minimum 1 attribut global
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and global_attribute_name in arrangement['global_attribute'] and len(list(arrangement['global_attribute'].keys())) > 1:
                del arrangement['global_attribute'][":" + global_attribute_name]
                self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
                self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Global information deleted.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information deleted.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name. The model structure must depend on at least 1 global information. Please enter a new global information first.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name. The model structure must depend on at least 1 global information. Please enter a new global information first.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_value_delete_confirm(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            # Si le nom de l'attribut global n'est pas vide, s'il ne contient aucun espace blanc, si la première lettre est en minuscule et s'il est inclu dans l'agencement
            if global_attribute_name != "" and any(char.isspace() for char in global_attribute_name) == False and global_attribute_name[0].islower() == True and bool(re.match(r'^[a-zA-Z0-9_]*$', global_attribute_name)) == True and global_attribute_name in arrangement['global_attribute']:
                self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_lineedit.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_confirm_button.setEnabled(False)
                self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_cancel_button.setEnabled(True)
                self.vuearrangementsettings.attribute_tabwidget.delete_value_button.setEnabled(True)
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Global information name selected.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Global information name selected.\n", "green")
            # Sinon
            else:
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Incorrect global information name.\n")
                self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Incorrect global information name.\n", "red")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
    
    
    def global_attribute_value_delete_cancel(self):
        
        self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_lineedit.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_confirm_button.setEnabled(True)
        self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_cancel_button.setEnabled(False)
        self.vuearrangementsettings.attribute_tabwidget.delete_value_button.setEnabled(False)
    
    
    def global_attribute_value_delete(self):
        
        global_attribute_name: str = self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_lineedit.text()
        arrangement = self.vuearrangementsettings.vuearrangement.modelearrangement.read_json()
        # Si l'agencement existe
        if arrangement:
            arrangement['global_attribute'][":" + global_attribute_name] = "NaN"
            self.vuearrangementsettings.vuearrangement.modelearrangement.write_json(arrangement)
            self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_lineedit.setEnabled(True)
            self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_confirm_button.setEnabled(True)
            self.vuearrangementsettings.attribute_tabwidget.delete_value_attribute_cancel_button.setEnabled(False)
            self.vuearrangementsettings.attribute_tabwidget.delete_value_button.setEnabled(False)
            self.vuearrangementsettings.vuearrangement.vuearrangementviewer.controleurarrangementviewer.load_arrangement()
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Information deleted.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Information deleted.\n", "green")
        # Sinon
        else:
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_log("Unknown arrangement type.\n")
            self.vuearrangementsettings.vuearrangement.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Unknown arrangement type.\n", "red")
