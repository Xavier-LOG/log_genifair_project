# Définition de la classe controleurFilesettings




class controleurFilesettings:


    # Constructeur par défaut

    
    def __init__(self, vuefilesettings):
        
        super().__init__()        
        self.vuefilesettings = vuefilesettings
    
    
    # Définition des méthodes
    
    
    def confirm(self):
        
        self.vuefilesettings.groupbox_slider.setEnabled(False)
        self.vuefilesettings.groupbox_confirm_button.setEnabled(False)
        self.vuefilesettings.groupbox_cancel_button.setEnabled(True)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.setEnabled(True)
        if self.vuefilesettings.groupbox_slider.sliderPosition() == 0:
            self.vuefilesettings.vuemainwindow.vuetoolbar.controleurtoolbar.row_number = 100
        elif self.vuefilesettings.groupbox_slider.sliderPosition() == 1:
            self.vuefilesettings.vuemainwindow.vuetoolbar.controleurtoolbar.row_number = 1000
        elif self.vuefilesettings.groupbox_slider.sliderPosition() == 2:
            self.vuefilesettings.vuemainwindow.vuetoolbar.controleurtoolbar.row_number = 10000
        elif self.vuefilesettings.groupbox_slider.sliderPosition() == 3:
            self.vuefilesettings.vuemainwindow.vuetoolbar.controleurtoolbar.row_number = None
        self.vuefilesettings.vuemainwindow.vuelogs.controleurlogs.add_log("Row file limit has been selected. Please, choose a new catalog type to proceed.\n")
        self.vuefilesettings.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Row file limit has been selected. Please, choose a new catalog type to proceed.\n", "green")
    
    
    def cancel(self):
        
        self.vuefilesettings.groupbox_slider.setEnabled(True)
        self.vuefilesettings.groupbox_confirm_button.setEnabled(True)
        self.vuefilesettings.groupbox_cancel_button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setChecked(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_time_series_catalog_checkbox.setChecked(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_profile_catalog_checkbox.setChecked(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_sample_catalog_checkbox.setChecked(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogviewer.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogsettings.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogsettings.button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.groupbox_save_button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.groupbox_confirm_button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_trajectory_catalog_checkbox.setEnabled(True)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_time_series_catalog_checkbox.setEnabled(True)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_profile_catalog_checkbox.setEnabled(True)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_sample_catalog_checkbox.setEnabled(True)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_confirm_button.setEnabled(True)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_cancel_button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_restore_button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.vuecatalogtype.groupbox_open_button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.tabwidget.setTabEnabled(1, False)
        self.vuefilesettings.vuemainwindow.tabwidget.setCurrentIndex(0)
        self.vuefilesettings.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.clearContents()
        self.vuefilesettings.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setRowCount(20)
        self.vuefilesettings.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setColumnCount(20)
        self.vuefilesettings.vuemainwindow.vueconversion.vuedataframeviewer.groupbox_tablewidget.setHorizontalHeaderLabels([str(i + 1) for i in range(20)])
        self.vuefilesettings.vuemainwindow.vueconversion.vuenetcdfviewer.groupbox_textarea.setPlainText("")
        self.vuefilesettings.vuemainwindow.vuefileviewer.groupbox_textarea.setPlainText("")
        self.vuefilesettings.vuemainwindow.vuetoolbar.menu_file_button.setEnabled(False)
        self.vuefilesettings.vuemainwindow.vuecatalog.modelecatalog.path_list_files = ["", []]
        self.vuefilesettings.vuemainwindow.vuetoolbar.controleurtoolbar.file_list = []
        self.vuefilesettings.vuemainwindow.vuetoolbar.controleurtoolbar.dataframe_list = []
        self.vuefilesettings.vuemainwindow.vuelogs.controleurlogs.add_log("Row file limit has been cancelled. Please, choose the maximum number of rows in the file to choose a new catalog type.\n")
        self.vuefilesettings.vuemainwindow.vuelogs.controleurlogs.add_colored_log("Row file limit has been cancelled. Please, choose the maximum number of rows in the file to choose a new catalog type.\n", "orange")
