# Importation des bibliothèques




import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPlainTextEdit, QPushButton, QGroupBox, QTabWidget, QLineEdit




# Définition de la classe DimensionTabWidget




class DimensionTabWidget(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.dimensiontab_layout = QVBoxLayout()
        self.dimensiontab_tabwidget = QTabWidget()
        
        self.dimensiontab_tabwidget.addTab(self.add_dimension(), "Add")
        self.dimensiontab_tabwidget.addTab(self.modify_dimension(), "Modify")
        self.dimensiontab_tabwidget.addTab(self.delete_dimension(), "Delete")
        
        self.dimensiontab_layout.addWidget(self.dimensiontab_tabwidget)
        
        self.setLayout(self.dimensiontab_layout)
    
    
    def add_dimension(self):
        
        self.dimensiontab_add_tabwidget = QTabWidget()
        
        self.dimensiontab_add_name_groupbox = QGroupBox()
        self.dimensiontab_add_name_layout = QVBoxLayout()
        self.dimensiontab_add_name_label = QLabel("New Dimension Name")
        self.dimensiontab_add_name_lineedit = QLineEdit("Enter New Dimension Name")
        self.dimensiontab_add_name_button = QPushButton("Add New Dimension")
        
        self.dimensiontab_add_name_layout.addWidget(self.dimensiontab_add_name_label)
        self.dimensiontab_add_name_layout.addWidget(self.dimensiontab_add_name_lineedit)
        self.dimensiontab_add_name_layout.addWidget(self.dimensiontab_add_name_button)
        self.dimensiontab_add_name_groupbox.setLayout(self.dimensiontab_add_name_layout)
        
        self.dimensiontab_add_tabwidget.addTab(self.dimensiontab_add_name_groupbox, "Name")
        
        return self.dimensiontab_add_tabwidget
    
    
    def modify_dimension(self):
        
        self.dimensiontab_modify_tabwidget = QTabWidget()
        
        self.dimensiontab_modify_name_groupbox = QGroupBox()
        self.dimensiontab_modify_name_layout = QVBoxLayout()
        self.dimensiontab_modify_name_label = QLabel("Dimension Name")
        self.dimensiontab_modify_name_lineedit = QLineEdit("Enter Dimension Name")
        self.dimensiontab_modify_name_confirm_button = QPushButton("Confirm")
        self.dimensiontab_modify_name_cancel_button = QPushButton("Cancel")
        self.dimensiontab_modify_new_name_label = QLabel("New Dimension Name")
        self.dimensiontab_modify_new_name_lineedit = QLineEdit("Enter New Dimension Name")
        self.dimensiontab_modify_new_name_modify_button = QPushButton("Modify Dimension")
        
        self.dimensiontab_modify_name_layout.addWidget(self.dimensiontab_modify_name_label)
        self.dimensiontab_modify_name_layout.addWidget(self.dimensiontab_modify_name_lineedit)
        self.dimensiontab_modify_name_layout.addWidget(self.dimensiontab_modify_name_confirm_button)
        self.dimensiontab_modify_name_layout.addWidget(self.dimensiontab_modify_name_cancel_button)
        self.dimensiontab_modify_name_layout.addWidget(self.dimensiontab_modify_new_name_label)
        self.dimensiontab_modify_name_layout.addWidget(self.dimensiontab_modify_new_name_lineedit)
        self.dimensiontab_modify_name_layout.addWidget(self.dimensiontab_modify_new_name_modify_button)
        self.dimensiontab_modify_name_groupbox.setLayout(self.dimensiontab_modify_name_layout)
        
        self.dimensiontab_modify_tabwidget.addTab(self.dimensiontab_modify_name_groupbox, "Name")
        
        return self.dimensiontab_modify_tabwidget
    
    
    def delete_dimension(self):
        
        self.dimensiontab_delete_tabwidget = QTabWidget()
        
        self.dimensiontab_delete_name_groupbox = QGroupBox()
        self.dimensiontab_delete_name_layout = QVBoxLayout()
        self.dimensiontab_delete_name_label = QLabel("Dimension Name")
        self.dimensiontab_delete_name_lineedit = QLineEdit("Enter Dimension Name")
        self.dimensiontab_delete_name_button = QPushButton("Delete Dimension")
        
        self.dimensiontab_delete_name_layout.addWidget(self.dimensiontab_delete_name_label)
        self.dimensiontab_delete_name_layout.addWidget(self.dimensiontab_delete_name_lineedit)
        self.dimensiontab_delete_name_layout.addWidget(self.dimensiontab_delete_name_button)
        self.dimensiontab_delete_name_groupbox.setLayout(self.dimensiontab_delete_name_layout)
        
        self.dimensiontab_delete_tabwidget.addTab(self.dimensiontab_delete_name_groupbox, "Name")
        
        return self.dimensiontab_delete_tabwidget
        



# Définition de la classe VariableTabWidget




class VariableTabWidget(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.variabletab_layout = QVBoxLayout()
        self.variabletab_tabwidget = QTabWidget()
        
        self.variabletab_tabwidget.addTab(self.add_variable(), "Add")
        self.variabletab_tabwidget.addTab(self.modify_variable(), "Modify")
        self.variabletab_tabwidget.addTab(self.delete_variable(), "Delete")
        
        self.variabletab_layout.addWidget(self.variabletab_tabwidget)
        
        self.setLayout(self.variabletab_layout)
    
    
    def add_variable(self):
        
        self.variabletab_add_tabwidget = QTabWidget()
        
        self.variabletab_add_name_groupbox = QGroupBox()
        self.variabletab_add_name_layout = QVBoxLayout()
        self.variabletab_add_name_label = QLabel("New Variable Name")
        self.variabletab_add_name_lineedit = QLineEdit("Enter New Variable Name")
        self.variabletab_add_dimension_label = QLabel("New Variable Dimension")
        self.variabletab_add_dimension_lineedit = QLineEdit("Enter New Variable Dimension")
        self.variabletab_add_name_button = QPushButton("Add New Variable")
        
        self.variabletab_add_name_layout.addWidget(self.variabletab_add_name_label)
        self.variabletab_add_name_layout.addWidget(self.variabletab_add_name_lineedit)
        self.variabletab_add_name_layout.addWidget(self.variabletab_add_dimension_label)
        self.variabletab_add_name_layout.addWidget(self.variabletab_add_dimension_lineedit)
        self.variabletab_add_name_layout.addWidget(self.variabletab_add_name_button)
        self.variabletab_add_name_groupbox.setLayout(self.variabletab_add_name_layout)
        
        self.variabletab_add_attribute_groupbox = QGroupBox()
        self.variabletab_add_attribute_layout = QVBoxLayout()
        self.variabletab_add_attribute_label = QLabel("Attribute Name")
        self.variabletab_add_attribute_lineedit = QLineEdit("Enter New Attribute Name")
        self.variabletab_add_attribute_button = QPushButton("Add New Attribute")
        
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_label)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_lineedit)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_button)
        self.variabletab_add_attribute_groupbox.setLayout(self.variabletab_add_attribute_layout)
        
        self.variabletab_add_tabwidget.addTab(self.variabletab_add_name_groupbox, "Name")
        self.variabletab_add_tabwidget.addTab(self.variabletab_add_attribute_groupbox, "Attribute")
        
        return self.variabletab_add_tabwidget
    
    
    def modify_variable(self):
        
        self.variabletab_modify_tabwidget = QTabWidget()
        
        self.variabletab_modify_name_groupbox = QGroupBox()
        self.variabletab_modify_name_layout = QVBoxLayout()
        self.variabletab_modify_name_label = QLabel("Variable Name")
        self.variabletab_modify_name_lineedit = QLineEdit("Enter Variable Name")
        self.variabletab_modify_name_confirm_button = QPushButton("Confirm")
        self.variabletab_modify_name_cancel_button = QPushButton("Cancel")
        self.variabletab_modify_new_name_label = QLabel("New Variable Name")
        self.variabletab_modify_new_name_lineedit = QLineEdit("Enter New Variable Name")
        self.variabletab_modify_dimension_label = QLabel("New Variable Dimension")
        self.variabletab_modify_dimension_lineedit = QLineEdit("Enter New Variable Dimension")
        self.variabletab_modify_new_name_modify_button = QPushButton("Modify Variable")
        
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_name_label)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_name_lineedit)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_name_confirm_button)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_name_cancel_button)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_new_name_label)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_new_name_lineedit)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_dimension_label)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_dimension_lineedit)
        self.variabletab_modify_name_layout.addWidget(self.variabletab_modify_new_name_modify_button)
        self.variabletab_modify_name_groupbox.setLayout(self.variabletab_modify_name_layout)
        
        self.variabletab_modify_attribute_groupbox = QGroupBox()
        self.variabletab_modify_attribute_layout = QVBoxLayout()
        self.variabletab_modify_attribute_label = QLabel("Attribute Name")
        self.variabletab_modify_attribute_lineedit = QLineEdit("Enter Attribute Name")
        self.variabletab_modify_attribute_confirm_button = QPushButton("Confirm")
        self.variabletab_modify_attribute_cancel_button = QPushButton("Cancel")
        self.variabletab_modify_new_attribute_label = QLabel("New Attribute Name")
        self.variabletab_modify_new_attribute_lineedit = QLineEdit("Enter New Attribute Name")
        self.variabletab_modify_new_attribute_modify_button = QPushButton("Modify Attribute")
        
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_label)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_lineedit)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_confirm_button)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_cancel_button)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_label)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_lineedit)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_modify_button)
        self.variabletab_modify_attribute_groupbox.setLayout(self.variabletab_modify_attribute_layout)
        
        self.variabletab_modify_tabwidget.addTab(self.variabletab_modify_name_groupbox, "Name")
        self.variabletab_modify_tabwidget.addTab(self.variabletab_modify_attribute_groupbox, "Attribute")
        
        return self.variabletab_modify_tabwidget
    
    
    def delete_variable(self):
        
        self.variabletab_delete_tabwidget = QTabWidget()
        
        self.variabletab_delete_name_groupbox = QGroupBox()
        self.variabletab_delete_name_layout = QVBoxLayout()
        self.variabletab_delete_name_label = QLabel("Variable Name")
        self.variabletab_delete_name_lineedit = QLineEdit("Enter Variable Name")
        self.variabletab_delete_name_button = QPushButton("Delete Variable")
        
        self.variabletab_delete_name_layout.addWidget(self.variabletab_delete_name_label)
        self.variabletab_delete_name_layout.addWidget(self.variabletab_delete_name_lineedit)
        self.variabletab_delete_name_layout.addWidget(self.variabletab_delete_name_button)
        self.variabletab_delete_name_groupbox.setLayout(self.variabletab_delete_name_layout)
        
        self.variabletab_delete_attribute_groupbox = QGroupBox()
        self.variabletab_delete_attribute_layout = QVBoxLayout()
        self.variabletab_delete_attribute_label = QLabel("Attribute Name")
        self.variabletab_delete_attribute_lineedit = QLineEdit("Enter Attribute Name")
        self.variabletab_delete_attribute_button = QPushButton("Delete Attribute")
        
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_label)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_lineedit)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_button)
        self.variabletab_delete_attribute_groupbox.setLayout(self.variabletab_delete_attribute_layout)
        
        self.variabletab_delete_tabwidget.addTab(self.variabletab_delete_name_groupbox, "Name")
        self.variabletab_delete_tabwidget.addTab(self.variabletab_delete_attribute_groupbox, "Attribute")
        
        return self.variabletab_delete_tabwidget

    
    
    
# Définition de la classe AttributeTabWidget




class AttributeTabWidget(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.attributetab_layout = QVBoxLayout()
        self.attributetab_tabwidget = QTabWidget()
        
        self.attributetab_tabwidget.addTab(self.add_attribute(), "Add")
        self.attributetab_tabwidget.addTab(self.modify_attribute(), "Modify")
        self.attributetab_tabwidget.addTab(self.delete_attribute(), "Delete")
        
        self.attributetab_layout.addWidget(self.attributetab_tabwidget)
        
        self.setLayout(self.attributetab_layout)
    
    
    def add_attribute(self):
        
        self.attributetab_add_tabwidget = QTabWidget()
        
        self.attributetab_add_name_groupbox = QGroupBox()
        self.attributetab_add_name_layout = QVBoxLayout()
        self.attributetab_add_name_label = QLabel("New Attribute Name")
        self.attributetab_add_name_lineedit = QLineEdit("Enter New Attribute Name")
        self.attributetab_add_name_button = QPushButton("Add New Attribute")
        
        self.attributetab_add_name_layout.addWidget(self.attributetab_add_name_label)
        self.attributetab_add_name_layout.addWidget(self.attributetab_add_name_lineedit)
        self.attributetab_add_name_layout.addWidget(self.attributetab_add_name_button)
        self.attributetab_add_name_groupbox.setLayout(self.attributetab_add_name_layout)
        
        self.attributetab_add_attribute_groupbox = QGroupBox()
        self.attributetab_add_attribute_layout = QVBoxLayout()
        self.attributetab_add_attribute_label = QLabel("New Attribute Value")
        self.attributetab_add_attribute_lineedit = QLineEdit("Enter New Attribute Value")
        self.attributetab_add_attribute_button = QPushButton("Add New Attribute Value")
        
        self.attributetab_add_attribute_layout.addWidget(self.attributetab_add_attribute_label)
        self.attributetab_add_attribute_layout.addWidget(self.attributetab_add_attribute_lineedit)
        self.attributetab_add_attribute_layout.addWidget(self.attributetab_add_attribute_button)
        self.attributetab_add_attribute_groupbox.setLayout(self.attributetab_add_attribute_layout)
        
        self.attributetab_add_tabwidget.addTab(self.attributetab_add_name_groupbox, "Name")
        self.attributetab_add_tabwidget.addTab(self.attributetab_add_attribute_groupbox, "Attribute")
        
        return self.attributetab_add_tabwidget
    
    
    def modify_attribute(self):
        
        self.attributetab_modify_tabwidget = QTabWidget()
        
        self.attributetab_modify_name_groupbox = QGroupBox()
        self.attributetab_modify_name_layout = QVBoxLayout()
        self.attributetab_modify_name_label = QLabel("Attribute Name")
        self.attributetab_modify_name_lineedit = QLineEdit("Enter Attribute Name")
        self.attributetab_modify_name_confirm_button = QPushButton("Confirm")
        self.attributetab_modify_name_cancel_button = QPushButton("Cancel")
        self.attributetab_modify_new_name_label = QLabel("New Attribute Name")
        self.attributetab_modify_new_name_lineedit = QLineEdit("Enter New Attribute Name")
        self.attributetab_modify_new_name_modify_button = QPushButton("Modify Attribute")
        
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_label)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_lineedit)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_confirm_button)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_cancel_button)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_new_name_label)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_new_name_lineedit)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_new_name_modify_button)
        self.attributetab_modify_name_groupbox.setLayout(self.attributetab_modify_name_layout)
        
        self.attributetab_modify_attribute_groupbox = QGroupBox()
        self.attributetab_modify_attribute_layout = QVBoxLayout()
        self.attributetab_modify_attribute_label = QLabel("Attribute Value")
        self.attributetab_modify_attribute_lineedit = QLineEdit("Enter Attribute Value")
        self.attributetab_modify_attribute_confirm_button = QPushButton("Confirm")
        self.attributetab_modify_attribute_cancel_button = QPushButton("Cancel")
        self.attributetab_modify_new_attribute_label = QLabel("New Attribute Value")
        self.attributetab_modify_new_attribute_lineedit = QLineEdit("Enter New Attribute Value")
        self.attributetab_modify_new_attribute_modify_button = QPushButton("Modify Attribute")
        
        self.attributetab_modify_attribute_layout.addWidget(self.attributetab_modify_attribute_label)
        self.attributetab_modify_attribute_layout.addWidget(self.attributetab_modify_attribute_lineedit)
        self.attributetab_modify_attribute_layout.addWidget(self.attributetab_modify_attribute_confirm_button)
        self.attributetab_modify_attribute_layout.addWidget(self.attributetab_modify_attribute_cancel_button)
        self.attributetab_modify_attribute_layout.addWidget(self.attributetab_modify_new_attribute_label)
        self.attributetab_modify_attribute_layout.addWidget(self.attributetab_modify_new_attribute_lineedit)
        self.attributetab_modify_attribute_layout.addWidget(self.attributetab_modify_new_attribute_modify_button)
        self.attributetab_modify_attribute_groupbox.setLayout(self.attributetab_modify_attribute_layout)
        
        self.attributetab_modify_tabwidget.addTab(self.attributetab_modify_name_groupbox, "Name")
        self.attributetab_modify_tabwidget.addTab(self.attributetab_modify_attribute_groupbox, "Attribute")
        
        return self.attributetab_modify_tabwidget
    
    
    def delete_attribute(self):
        
        self.attributetab_delete_tabwidget = QTabWidget()
        
        self.attributetab_delete_name_groupbox = QGroupBox()
        self.attributetab_delete_name_layout = QVBoxLayout()
        self.attributetab_delete_name_label = QLabel("Attribute Name")
        self.attributetab_delete_name_lineedit = QLineEdit("Enter Attribute Name")
        self.attributetab_delete_name_button = QPushButton("Delete Attribute")
        
        self.attributetab_delete_name_layout.addWidget(self.attributetab_delete_name_label)
        self.attributetab_delete_name_layout.addWidget(self.attributetab_delete_name_lineedit)
        self.attributetab_delete_name_layout.addWidget(self.attributetab_delete_name_button)
        self.attributetab_delete_name_groupbox.setLayout(self.attributetab_delete_name_layout)
        
        self.attributetab_delete_attribute_groupbox = QGroupBox()
        self.attributetab_delete_attribute_layout = QVBoxLayout()
        self.attributetab_delete_attribute_label = QLabel("Attribute Value")
        self.attributetab_delete_attribute_lineedit = QLineEdit("Enter Attribute Value")
        self.attributetab_delete_attribute_button = QPushButton("Delete Attribute Value")
        
        self.attributetab_delete_attribute_layout.addWidget(self.attributetab_delete_attribute_label)
        self.attributetab_delete_attribute_layout.addWidget(self.attributetab_delete_attribute_lineedit)
        self.attributetab_delete_attribute_layout.addWidget(self.attributetab_delete_attribute_button)
        self.attributetab_delete_attribute_groupbox.setLayout(self.attributetab_delete_attribute_layout)
        
        self.attributetab_delete_tabwidget.addTab(self.attributetab_delete_name_groupbox, "Name")
        self.attributetab_delete_tabwidget.addTab(self.attributetab_delete_attribute_groupbox, "Attribute")
        
        return self.attributetab_delete_tabwidget





# Définition de la classe vueNetCDF




class vueNetCDF(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()


    # Définition des méthodes
    
    
    def init_ui(self):

        self.vuenetcdf_layout = QVBoxLayout()
        self.vuenetcdf_groupbox = QGroupBox("NetCDF Model")
        self.vuenetcdf_groupbox_layout = QVBoxLayout()
        self.vuenetcdf_textarea = QPlainTextEdit()
        
        self.vuenetcdf_textarea.setReadOnly(True)
        self.load_catalog()
        
        self.vuenetcdf_groupbox_layout.addWidget(self.vuenetcdf_textarea)
        self.vuenetcdf_groupbox.setLayout(self.vuenetcdf_groupbox_layout)

        self.vuenetcdf_label = QLabel("NetCDF Model Settings")

        self.vuenetcdf_tabwidget = QTabWidget()
        self.vuenetcdf_dimension_tabwidget = DimensionTabWidget()
        self.vuenetcdf_variable_tabwidget = VariableTabWidget()
        self.vuenetcdf_attribute_tabwidget = AttributeTabWidget()

        self.vuenetcdf_tabwidget.addTab(self.vuenetcdf_dimension_tabwidget, "Dimension")
        self.vuenetcdf_tabwidget.addTab(self.vuenetcdf_variable_tabwidget, "Variable")
        self.vuenetcdf_tabwidget.addTab(self.vuenetcdf_attribute_tabwidget, "Attribute")

        self.vuenetcdf_button = QPushButton("Confirm NetCDF Model")

        self.vuenetcdf_layout.addWidget(self.vuenetcdf_groupbox)
        self.vuenetcdf_layout.addWidget(self.vuenetcdf_label)
        self.vuenetcdf_layout.addWidget(self.vuenetcdf_tabwidget)
        self.vuenetcdf_layout.addWidget(self.vuenetcdf_button)

        self.setLayout(self.vuenetcdf_layout)
    
    
    def load_catalog(self):
        
        # Chargement le fichier JSON
        with open('./catalog.json', 'r') as f:
            catalog = json.load(f)
            
        # Accès à chaque valeur de chaque attribut du catalogue
        variable_catalog = catalog['variable']
        dimension_catalog = catalog['dimension']
        global_attribute_catalog = catalog['global_attribute']
        
        # Affichage des dimensions du catalogue
        self.vuenetcdf_textarea.appendPlainText(str("\nDimensions :\n"))
        for dimension in dimension_catalog:
            self.vuenetcdf_textarea.appendPlainText(str(f"\t{dimension}"))
        
        # Affichage des variables du catalogue
        self.vuenetcdf_textarea.appendPlainText("\nVariables :")
        for variable_name, variable_data in variable_catalog.items():
            self.vuenetcdf_textarea.appendPlainText(str("\n\tNom de la variable : ") + str(variable_name))
            self.vuenetcdf_textarea.appendPlainText(str("\tDimension :") + str(variable_data['dimension']))
            self.vuenetcdf_textarea.appendPlainText(str("\tAttributs :"))
            for attribute_name, attribute_value in variable_data['attribute'].items():
                self.vuenetcdf_textarea.appendPlainText(str(f"\t\t{attribute_name} : {attribute_value}"))
        
        # Affichage des attributs globaux du catalogue
        self.vuenetcdf_textarea.appendPlainText(str("\nAttributs globaux :\n"))
        for global_attribute_name, global_attribute_value in global_attribute_catalog.items():
            self.vuenetcdf_textarea.appendPlainText(str(f"\t{global_attribute_name} : {global_attribute_value}"))




# Programme principal




if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    mainwindow.setCentralWidget(vueNetCDF())
    mainwindow.show()
    sys.exit(app.exec())
