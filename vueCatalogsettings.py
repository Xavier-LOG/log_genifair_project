# Importation des fichiers




from controleurCatalogsettings import controleurCatalogsettings




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QGroupBox, QTabWidget, QLineEdit




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
        
        self.dimensiontab_modify_name_lineedit.setEnabled(True)
        self.dimensiontab_modify_name_confirm_button.setEnabled(True)
        self.dimensiontab_modify_name_cancel_button.setEnabled(False)
        self.dimensiontab_modify_new_name_lineedit.setEnabled(False)
        self.dimensiontab_modify_new_name_modify_button.setEnabled(False)
        
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
        self.variabletab_add_attribute_variable_label = QLabel("Variable Name")
        self.variabletab_add_attribute_variable_lineedit = QLineEdit("Enter Variable Name")
        self.variabletab_add_attribute_variable_confirm_button = QPushButton("Confirm")
        self.variabletab_add_attribute_variable_cancel_button = QPushButton("Cancel")
        self.variabletab_add_attribute_label = QLabel("Variable Information Name")
        self.variabletab_add_attribute_lineedit = QLineEdit("Enter New Variable Information Name")
        self.variabletab_add_attribute_value_label = QLabel("Variable Information Value")
        self.variabletab_add_attribute_value_lineedit = QLineEdit("Enter New Variable Information Value")
        self.variabletab_add_attribute_button = QPushButton("Add New Variable Information")
        
        self.variabletab_add_attribute_variable_lineedit.setEnabled(True)
        self.variabletab_add_attribute_variable_confirm_button.setEnabled(True)
        self.variabletab_add_attribute_variable_cancel_button.setEnabled(False)
        self.variabletab_add_attribute_lineedit.setEnabled(False)
        self.variabletab_add_attribute_value_lineedit.setEnabled(False)
        self.variabletab_add_attribute_button.setEnabled(False)
        
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_variable_label)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_variable_lineedit)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_variable_confirm_button)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_variable_cancel_button)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_label)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_lineedit)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_value_label)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_value_lineedit)
        self.variabletab_add_attribute_layout.addWidget(self.variabletab_add_attribute_button)
        self.variabletab_add_attribute_groupbox.setLayout(self.variabletab_add_attribute_layout)
        
        self.variabletab_add_tabwidget.addTab(self.variabletab_add_name_groupbox, "Name")
        self.variabletab_add_tabwidget.addTab(self.variabletab_add_attribute_groupbox, "Variable Information")
        
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
        
        self.variabletab_modify_name_lineedit.setEnabled(True)
        self.variabletab_modify_name_confirm_button.setEnabled(True)
        self.variabletab_modify_name_cancel_button.setEnabled(False)
        self.variabletab_modify_new_name_lineedit.setEnabled(False)
        self.variabletab_modify_dimension_lineedit.setEnabled(False)
        self.variabletab_modify_new_name_modify_button.setEnabled(False)
        
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
        self.variabletab_modify_attribute_variable_label = QLabel("Variable Name")
        self.variabletab_modify_attribute_variable_lineedit = QLineEdit("Enter Variable Name")
        self.variabletab_modify_attribute_variable_confirm_button = QPushButton("Confirm")
        self.variabletab_modify_attribute_variable_cancel_button = QPushButton("Cancel")
        self.variabletab_modify_attribute_label = QLabel("Variable Information Name")
        self.variabletab_modify_attribute_lineedit = QLineEdit("Enter Variable Information Name")
        self.variabletab_modify_attribute_confirm_button = QPushButton("Confirm")
        self.variabletab_modify_attribute_cancel_button = QPushButton("Cancel")
        self.variabletab_modify_new_attribute_label = QLabel("New Variable Information Name")
        self.variabletab_modify_new_attribute_lineedit = QLineEdit("Enter New Variable Information Name")
        self.variabletab_modify_new_attribute_value_label = QLabel("New Variable Information Value")
        self.variabletab_modify_new_attribute_value_lineedit = QLineEdit("Enter New Variable Information Value")
        self.variabletab_modify_new_attribute_modify_button = QPushButton("Modify Variable Information")
        
        self.variabletab_modify_attribute_variable_lineedit.setEnabled(True)
        self.variabletab_modify_attribute_variable_confirm_button.setEnabled(True)
        self.variabletab_modify_attribute_variable_cancel_button.setEnabled(False)
        self.variabletab_modify_attribute_lineedit.setEnabled(False)
        self.variabletab_modify_attribute_confirm_button.setEnabled(False)
        self.variabletab_modify_attribute_cancel_button.setEnabled(False)
        self.variabletab_modify_new_attribute_lineedit.setEnabled(False)
        self.variabletab_modify_new_attribute_value_lineedit.setEnabled(False)
        self.variabletab_modify_new_attribute_modify_button.setEnabled(False)
        
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_variable_label)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_variable_lineedit)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_variable_confirm_button)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_variable_cancel_button)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_label)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_lineedit)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_confirm_button)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_attribute_cancel_button)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_label)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_lineedit)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_value_label)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_value_lineedit)
        self.variabletab_modify_attribute_layout.addWidget(self.variabletab_modify_new_attribute_modify_button)
        self.variabletab_modify_attribute_groupbox.setLayout(self.variabletab_modify_attribute_layout)
        
        self.variabletab_modify_tabwidget.addTab(self.variabletab_modify_name_groupbox, "Name")
        self.variabletab_modify_tabwidget.addTab(self.variabletab_modify_attribute_groupbox, "Variable Information")
        
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
        self.variabletab_delete_attribute_variable_label = QLabel("Variable Name")
        self.variabletab_delete_attribute_variable_lineedit = QLineEdit("Enter Variable Name")
        self.variabletab_delete_attribute_confirm_button = QPushButton("Confirm")
        self.variabletab_delete_attribute_cancel_button = QPushButton("Cancel")
        self.variabletab_delete_attribute_label = QLabel("Variable Information Name")
        self.variabletab_delete_attribute_lineedit = QLineEdit("Enter Variable Information Name")
        self.variabletab_delete_attribute_button = QPushButton("Delete Variable Information")
        
        self.variabletab_delete_attribute_variable_lineedit.setEnabled(True)
        self.variabletab_delete_attribute_confirm_button.setEnabled(True)
        self.variabletab_delete_attribute_cancel_button.setEnabled(False)
        self.variabletab_delete_attribute_lineedit.setEnabled(False)
        self.variabletab_delete_attribute_button.setEnabled(False)
        
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_variable_label)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_variable_lineedit)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_confirm_button)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_cancel_button)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_label)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_lineedit)
        self.variabletab_delete_attribute_layout.addWidget(self.variabletab_delete_attribute_button)
        self.variabletab_delete_attribute_groupbox.setLayout(self.variabletab_delete_attribute_layout)
        
        self.variabletab_delete_tabwidget.addTab(self.variabletab_delete_name_groupbox, "Name")
        self.variabletab_delete_tabwidget.addTab(self.variabletab_delete_attribute_groupbox, "Variable Information")
        
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
        self.attributetab_add_name_label = QLabel("New Global Information Name")
        self.attributetab_add_name_lineedit = QLineEdit("Enter New Global Information Name")
        self.attributetab_add_name_button = QPushButton("Add New Global Information")
        
        self.attributetab_add_name_layout.addWidget(self.attributetab_add_name_label)
        self.attributetab_add_name_layout.addWidget(self.attributetab_add_name_lineedit)
        self.attributetab_add_name_layout.addWidget(self.attributetab_add_name_button)
        self.attributetab_add_name_groupbox.setLayout(self.attributetab_add_name_layout)
        
        self.attributetab_add_value_groupbox = QGroupBox()
        self.attributetab_add_value_layout = QVBoxLayout()
        self.attributetab_add_value_attribute_label = QLabel("Global Information Name")
        self.attributetab_add_value_attribute_lineedit = QLineEdit("Enter Global Information Name")
        self.attributetab_add_value_attribute_confirm_button = QPushButton("Confirm")
        self.attributetab_add_value_attribute_cancel_button = QPushButton("Cancel")
        self.attributetab_add_value_label = QLabel("New Global Information Value")
        self.attributetab_add_value_lineedit = QLineEdit("Enter New Global Information Value")
        self.attributetab_add_value_button = QPushButton("Add New Global Information Value")
        
        self.attributetab_add_value_attribute_lineedit.setEnabled(True)
        self.attributetab_add_value_attribute_confirm_button.setEnabled(True)
        self.attributetab_add_value_attribute_cancel_button.setEnabled(False)
        self.attributetab_add_value_lineedit.setEnabled(False)
        self.attributetab_add_value_button.setEnabled(False)
        
        self.attributetab_add_value_layout.addWidget(self.attributetab_add_value_attribute_label)
        self.attributetab_add_value_layout.addWidget(self.attributetab_add_value_attribute_lineedit)
        self.attributetab_add_value_layout.addWidget(self.attributetab_add_value_attribute_confirm_button)
        self.attributetab_add_value_layout.addWidget(self.attributetab_add_value_attribute_cancel_button)
        self.attributetab_add_value_layout.addWidget(self.attributetab_add_value_label)
        self.attributetab_add_value_layout.addWidget(self.attributetab_add_value_lineedit)
        self.attributetab_add_value_layout.addWidget(self.attributetab_add_value_button)
        self.attributetab_add_value_groupbox.setLayout(self.attributetab_add_value_layout)
        
        self.attributetab_add_tabwidget.addTab(self.attributetab_add_name_groupbox, "Name")
        self.attributetab_add_tabwidget.addTab(self.attributetab_add_value_groupbox, "Information")
        
        return self.attributetab_add_tabwidget
    
    
    def modify_attribute(self):
        
        self.attributetab_modify_tabwidget = QTabWidget()
        
        self.attributetab_modify_name_groupbox = QGroupBox()
        self.attributetab_modify_name_layout = QVBoxLayout()
        self.attributetab_modify_name_label = QLabel("Global Information Name")
        self.attributetab_modify_name_lineedit = QLineEdit("Enter Global Information Name")
        self.attributetab_modify_name_confirm_button = QPushButton("Confirm")
        self.attributetab_modify_name_cancel_button = QPushButton("Cancel")
        self.attributetab_modify_new_name_label = QLabel("New Global Information Name")
        self.attributetab_modify_new_name_lineedit = QLineEdit("Enter New Global Information Name")
        self.attributetab_modify_new_name_modify_button = QPushButton("Modify Global Information")
        
        self.attributetab_modify_name_lineedit.setEnabled(True)
        self.attributetab_modify_name_confirm_button.setEnabled(True)
        self.attributetab_modify_name_cancel_button.setEnabled(False)
        self.attributetab_modify_new_name_lineedit.setEnabled(False)
        self.attributetab_modify_new_name_modify_button.setEnabled(False)
        
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_label)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_lineedit)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_confirm_button)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_name_cancel_button)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_new_name_label)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_new_name_lineedit)
        self.attributetab_modify_name_layout.addWidget(self.attributetab_modify_new_name_modify_button)
        self.attributetab_modify_name_groupbox.setLayout(self.attributetab_modify_name_layout)
        
        self.attributetab_modify_value_groupbox = QGroupBox()
        self.attributetab_modify_value_layout = QVBoxLayout()
        self.attributetab_modify_value_attribute_label = QLabel("Global Information Name")
        self.attributetab_modify_value_attribute_lineedit = QLineEdit("Enter Global Information Name")
        self.attributetab_modify_value_attribute_confirm_button = QPushButton("Confirm")
        self.attributetab_modify_value_attribute_cancel_button = QPushButton("Cancel")
        self.attributetab_modify_new_value_label = QLabel("New Global Information Value")
        self.attributetab_modify_new_value_lineedit = QLineEdit("Enter New Global Information Value")
        self.attributetab_modify_new_value_modify_button = QPushButton("Modify Global Information")
        
        self.attributetab_modify_value_attribute_lineedit.setEnabled(True)
        self.attributetab_modify_value_attribute_confirm_button.setEnabled(True)
        self.attributetab_modify_value_attribute_cancel_button.setEnabled(False)
        self.attributetab_modify_new_value_lineedit.setEnabled(False)
        self.attributetab_modify_new_value_modify_button.setEnabled(False)
        
        self.attributetab_modify_value_layout.addWidget(self.attributetab_modify_value_attribute_label)
        self.attributetab_modify_value_layout.addWidget(self.attributetab_modify_value_attribute_lineedit)
        self.attributetab_modify_value_layout.addWidget(self.attributetab_modify_value_attribute_confirm_button)
        self.attributetab_modify_value_layout.addWidget(self.attributetab_modify_value_attribute_cancel_button)
        self.attributetab_modify_value_layout.addWidget(self.attributetab_modify_new_value_label)
        self.attributetab_modify_value_layout.addWidget(self.attributetab_modify_new_value_lineedit)
        self.attributetab_modify_value_layout.addWidget(self.attributetab_modify_new_value_modify_button)
        self.attributetab_modify_value_groupbox.setLayout(self.attributetab_modify_value_layout)
        
        self.attributetab_modify_tabwidget.addTab(self.attributetab_modify_name_groupbox, "Name")
        self.attributetab_modify_tabwidget.addTab(self.attributetab_modify_value_groupbox, "Information")
        
        return self.attributetab_modify_tabwidget
    
    
    def delete_attribute(self):
        
        self.attributetab_delete_tabwidget = QTabWidget()
        
        self.attributetab_delete_name_groupbox = QGroupBox()
        self.attributetab_delete_name_layout = QVBoxLayout()
        self.attributetab_delete_name_label = QLabel("Global Information Name")
        self.attributetab_delete_name_lineedit = QLineEdit("Enter Global Information Name")
        self.attributetab_delete_name_button = QPushButton("Delete Global Information")
        
        self.attributetab_delete_name_layout.addWidget(self.attributetab_delete_name_label)
        self.attributetab_delete_name_layout.addWidget(self.attributetab_delete_name_lineedit)
        self.attributetab_delete_name_layout.addWidget(self.attributetab_delete_name_button)
        self.attributetab_delete_name_groupbox.setLayout(self.attributetab_delete_name_layout)
        
        self.attributetab_delete_value_groupbox = QGroupBox()
        self.attributetab_delete_value_layout = QVBoxLayout()
        self.attributetab_delete_value_attribute_label = QLabel("Global Information Name")
        self.attributetab_delete_value_attribute_lineedit = QLineEdit("Enter Global Information Name")
        self.attributetab_delete_value_attribute_confirm_button = QPushButton("Confirm")
        self.attributetab_delete_value_attribute_cancel_button = QPushButton("Cancel")
        self.attributetab_delete_value_button = QPushButton("Delete Global Information Value")
        
        self.attributetab_delete_value_attribute_lineedit.setEnabled(True)
        self.attributetab_delete_value_attribute_confirm_button.setEnabled(True)
        self.attributetab_delete_value_attribute_cancel_button.setEnabled(False)
        self.attributetab_delete_value_button.setEnabled(False)
        
        self.attributetab_delete_value_layout.addWidget(self.attributetab_delete_value_attribute_label)
        self.attributetab_delete_value_layout.addWidget(self.attributetab_delete_value_attribute_lineedit)
        self.attributetab_delete_value_layout.addWidget(self.attributetab_delete_value_attribute_confirm_button)
        self.attributetab_delete_value_layout.addWidget(self.attributetab_delete_value_attribute_cancel_button)
        self.attributetab_delete_value_layout.addWidget(self.attributetab_delete_value_button)
        self.attributetab_delete_value_groupbox.setLayout(self.attributetab_delete_value_layout)
        
        self.attributetab_delete_tabwidget.addTab(self.attributetab_delete_name_groupbox, "Name")
        self.attributetab_delete_tabwidget.addTab(self.attributetab_delete_value_groupbox, "Information")
        
        return self.attributetab_delete_tabwidget




# Définition de la classe vueCatalogsettings




class vueCatalogsettings(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.vuecatalog = parent
        self.controleurcatalogsettings = controleurCatalogsettings(self)
        self.init_ui()
        self.connect_signals()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        # Layout associé à l'instance de la classe vueCatalogsettings
        self.vuecatalogsettings_layout = QVBoxLayout(self)

        self.vuecatalogsettings_groupbox = QGroupBox("Catalog Settings")
        self.vuecatalogsettings_groupbox_layout = QVBoxLayout()
        self.vuecatalogsettings_tabwidget = QTabWidget()
        self.vuecatalogsettings_dimension_tabwidget = DimensionTabWidget()
        self.vuecatalogsettings_variable_tabwidget = VariableTabWidget()
        self.vuecatalogsettings_attribute_tabwidget = AttributeTabWidget()

        self.vuecatalogsettings_tabwidget.addTab(self.vuecatalogsettings_dimension_tabwidget, "Dimension")
        self.vuecatalogsettings_tabwidget.addTab(self.vuecatalogsettings_variable_tabwidget, "Variable")
        self.vuecatalogsettings_tabwidget.addTab(self.vuecatalogsettings_attribute_tabwidget, "Global Information")

        self.vuecatalogsettings_groupbox_layout.addWidget(self.vuecatalogsettings_tabwidget)
        self.vuecatalogsettings_groupbox.setLayout(self.vuecatalogsettings_groupbox_layout)
        
        self.vuecatalogsettings_layout.addWidget(self.vuecatalogsettings_groupbox)
    
    
    def connect_signals(self):
        
        self.vuecatalogsettings_dimension_tabwidget.dimensiontab_add_name_button.clicked.connect(self.controleurcatalogsettings.dimension_name_add)
        
        self.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_confirm_button.clicked.connect(self.controleurcatalogsettings.dimension_name_modify_confirm)
        self.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.dimension_name_modify_cancel)
        self.vuecatalogsettings_dimension_tabwidget.dimensiontab_modify_new_name_modify_button.clicked.connect(self.controleurcatalogsettings.dimension_name_modify)
        
        self.vuecatalogsettings_dimension_tabwidget.dimensiontab_delete_name_button.clicked.connect(self.controleurcatalogsettings.dimension_name_delete)
        
        self.vuecatalogsettings_variable_tabwidget.variabletab_add_name_button.clicked.connect(self.controleurcatalogsettings.variable_name_add)
        self.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_add_confirm)
        self.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_variable_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_add_cancel)
        self.vuecatalogsettings_variable_tabwidget.variabletab_add_attribute_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_add)
        
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_name_modify_confirm)
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_name_modify_cancel)
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_name_modify_button.clicked.connect(self.controleurcatalogsettings.variable_name_modify)
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_variable_modify_confirm)
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_variable_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_variable_modify_cancel)
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_modify_confirm)
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_modify_cancel)
        self.vuecatalogsettings_variable_tabwidget.variabletab_modify_new_attribute_modify_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_modify)
        
        self.vuecatalogsettings_variable_tabwidget.variabletab_delete_name_button.clicked.connect(self.controleurcatalogsettings.variable_name_delete)
        self.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_delete_confirm)
        self.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_delete_cancel)
        self.vuecatalogsettings_variable_tabwidget.variabletab_delete_attribute_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_delete)
        
        self.vuecatalogsettings_attribute_tabwidget.attributetab_add_name_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_add)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_add_confirm)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_add_cancel)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_add_value_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_add)
        
        self.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_modify_confirm)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_modify_cancel)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_name_modify_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_modify)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_modify_confirm)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_modify_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_modify_cancel)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_modify_new_value_modify_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_modify)
        
        self.vuecatalogsettings_attribute_tabwidget.attributetab_delete_name_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_delete)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_delete_confirm)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_delete_cancel)
        self.vuecatalogsettings_attribute_tabwidget.attributetab_delete_value_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_delete)




# Programme principal




if __name__ == "__main__":
    
    from vueMainwindow import vueMainwindow
    from vueCatalog import vueCatalog
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow
    
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    vuemainwindow = vueMainwindow()
    vuecatalog = vueCatalog(vuemainwindow)
    mainwindow.setCentralWidget(vueCatalogsettings(vuecatalog))
    mainwindow.show()
    sys.exit(app.exec())
