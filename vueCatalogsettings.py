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
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.add_dimension(), "Add")
        self.tabwidget.addTab(self.modify_dimension(), "Modify")
        self.tabwidget.addTab(self.delete_dimension(), "Delete")
        
        self.dimensiontab_layout.addWidget(self.tabwidget)
        
        self.setLayout(self.dimensiontab_layout)
    
    
    def add_dimension(self):
        
        self.add_tabwidget = QTabWidget()
        
        self.add_name_groupbox = QGroupBox()
        self.add_name_layout = QVBoxLayout()
        self.add_name_label = QLabel("New Dimension Name")
        self.add_name_lineedit = QLineEdit("Enter New Dimension Name")
        self.add_name_button = QPushButton("Add New Dimension")
        
        self.add_name_layout.addWidget(self.add_name_label)
        self.add_name_layout.addWidget(self.add_name_lineedit)
        self.add_name_layout.addWidget(self.add_name_button)
        self.add_name_groupbox.setLayout(self.add_name_layout)
        
        self.add_tabwidget.addTab(self.add_name_groupbox, "Name")
        
        return self.add_tabwidget
    
    
    def modify_dimension(self):
        
        self.modify_tabwidget = QTabWidget()
        
        self.modify_name_groupbox = QGroupBox()
        self.modify_name_layout = QVBoxLayout()
        self.modify_name_label = QLabel("Dimension Name")
        self.modify_name_lineedit = QLineEdit("Enter Dimension Name")
        self.modify_name_confirm_button = QPushButton("Confirm")
        self.modify_name_cancel_button = QPushButton("Cancel")
        self.modify_new_name_label = QLabel("New Dimension Name")
        self.modify_new_name_lineedit = QLineEdit("Enter New Dimension Name")
        self.modify_new_name_modify_button = QPushButton("Modify Dimension")
        
        self.modify_name_lineedit.setEnabled(True)
        self.modify_name_confirm_button.setEnabled(True)
        self.modify_name_cancel_button.setEnabled(False)
        self.modify_new_name_lineedit.setEnabled(False)
        self.modify_new_name_modify_button.setEnabled(False)
        
        self.modify_name_layout.addWidget(self.modify_name_label)
        self.modify_name_layout.addWidget(self.modify_name_lineedit)
        self.modify_name_layout.addWidget(self.modify_name_confirm_button)
        self.modify_name_layout.addWidget(self.modify_name_cancel_button)
        self.modify_name_layout.addWidget(self.modify_new_name_label)
        self.modify_name_layout.addWidget(self.modify_new_name_lineedit)
        self.modify_name_layout.addWidget(self.modify_new_name_modify_button)
        self.modify_name_groupbox.setLayout(self.modify_name_layout)
        
        self.modify_tabwidget.addTab(self.modify_name_groupbox, "Name")
        
        return self.modify_tabwidget
    
    
    def delete_dimension(self):
        
        self.delete_tabwidget = QTabWidget()
        
        self.delete_name_groupbox = QGroupBox()
        self.delete_name_layout = QVBoxLayout()
        self.delete_name_label = QLabel("Dimension Name")
        self.delete_name_lineedit = QLineEdit("Enter Dimension Name")
        self.delete_name_button = QPushButton("Delete Dimension")
        
        self.delete_name_layout.addWidget(self.delete_name_label)
        self.delete_name_layout.addWidget(self.delete_name_lineedit)
        self.delete_name_layout.addWidget(self.delete_name_button)
        self.delete_name_groupbox.setLayout(self.delete_name_layout)
        
        self.delete_tabwidget.addTab(self.delete_name_groupbox, "Name")
        
        return self.delete_tabwidget




# Définition de la classe VariableTabWidget




class VariableTabWidget(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.variabletab_layout = QVBoxLayout()
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.add_variable(), "Add")
        self.tabwidget.addTab(self.modify_variable(), "Modify")
        self.tabwidget.addTab(self.delete_variable(), "Delete")
        
        self.variabletab_layout.addWidget(self.tabwidget)
        
        self.setLayout(self.variabletab_layout)
    
    
    def add_variable(self):
        
        self.add_tabwidget = QTabWidget()
        
        self.add_name_groupbox = QGroupBox()
        self.add_name_layout = QVBoxLayout()
        self.add_name_label = QLabel("New Variable Name")
        self.add_name_lineedit = QLineEdit("Enter New Variable Name")
        self.add_dimension_label = QLabel("New Variable Dimension")
        self.add_dimension_lineedit = QLineEdit("Enter New Variable Dimension")
        self.add_name_button = QPushButton("Add New Variable")
        
        self.add_name_layout.addWidget(self.add_name_label)
        self.add_name_layout.addWidget(self.add_name_lineedit)
        self.add_name_layout.addWidget(self.add_dimension_label)
        self.add_name_layout.addWidget(self.add_dimension_lineedit)
        self.add_name_layout.addWidget(self.add_name_button)
        self.add_name_groupbox.setLayout(self.add_name_layout)
        
        self.add_attribute_groupbox = QGroupBox()
        self.add_attribute_layout = QVBoxLayout()
        self.add_attribute_variable_label = QLabel("Variable Name")
        self.add_attribute_variable_lineedit = QLineEdit("Enter Variable Name")
        self.add_attribute_variable_confirm_button = QPushButton("Confirm")
        self.add_attribute_variable_cancel_button = QPushButton("Cancel")
        self.add_attribute_label = QLabel("Variable Information Name")
        self.add_attribute_lineedit = QLineEdit("Enter New Variable Information Name")
        self.add_attribute_value_label = QLabel("Variable Information Value")
        self.add_attribute_value_lineedit = QLineEdit("Enter New Variable Information Value")
        self.add_attribute_button = QPushButton("Add New Variable Information")
        
        self.add_attribute_variable_lineedit.setEnabled(True)
        self.add_attribute_variable_confirm_button.setEnabled(True)
        self.add_attribute_variable_cancel_button.setEnabled(False)
        self.add_attribute_lineedit.setEnabled(False)
        self.add_attribute_value_lineedit.setEnabled(False)
        self.add_attribute_button.setEnabled(False)
        
        self.add_attribute_layout.addWidget(self.add_attribute_variable_label)
        self.add_attribute_layout.addWidget(self.add_attribute_variable_lineedit)
        self.add_attribute_layout.addWidget(self.add_attribute_variable_confirm_button)
        self.add_attribute_layout.addWidget(self.add_attribute_variable_cancel_button)
        self.add_attribute_layout.addWidget(self.add_attribute_label)
        self.add_attribute_layout.addWidget(self.add_attribute_lineedit)
        self.add_attribute_layout.addWidget(self.add_attribute_value_label)
        self.add_attribute_layout.addWidget(self.add_attribute_value_lineedit)
        self.add_attribute_layout.addWidget(self.add_attribute_button)
        self.add_attribute_groupbox.setLayout(self.add_attribute_layout)
        
        self.add_tabwidget.addTab(self.add_name_groupbox, "Name")
        self.add_tabwidget.addTab(self.add_attribute_groupbox, "Variable Information")
        
        return self.add_tabwidget
    
    
    def modify_variable(self):
        
        self.modify_tabwidget = QTabWidget()
        
        self.modify_name_groupbox = QGroupBox()
        self.modify_name_layout = QVBoxLayout()
        self.modify_name_label = QLabel("Variable Name")
        self.modify_name_lineedit = QLineEdit("Enter Variable Name")
        self.modify_name_confirm_button = QPushButton("Confirm")
        self.modify_name_cancel_button = QPushButton("Cancel")
        self.modify_new_name_label = QLabel("New Variable Name")
        self.modify_new_name_lineedit = QLineEdit("Enter New Variable Name")
        self.modify_dimension_label = QLabel("New Variable Dimension")
        self.modify_dimension_lineedit = QLineEdit("Enter New Variable Dimension")
        self.modify_new_name_modify_button = QPushButton("Modify Variable")
        
        self.modify_name_lineedit.setEnabled(True)
        self.modify_name_confirm_button.setEnabled(True)
        self.modify_name_cancel_button.setEnabled(False)
        self.modify_new_name_lineedit.setEnabled(False)
        self.modify_dimension_lineedit.setEnabled(False)
        self.modify_new_name_modify_button.setEnabled(False)
        
        self.modify_name_layout.addWidget(self.modify_name_label)
        self.modify_name_layout.addWidget(self.modify_name_lineedit)
        self.modify_name_layout.addWidget(self.modify_name_confirm_button)
        self.modify_name_layout.addWidget(self.modify_name_cancel_button)
        self.modify_name_layout.addWidget(self.modify_new_name_label)
        self.modify_name_layout.addWidget(self.modify_new_name_lineedit)
        self.modify_name_layout.addWidget(self.modify_dimension_label)
        self.modify_name_layout.addWidget(self.modify_dimension_lineedit)
        self.modify_name_layout.addWidget(self.modify_new_name_modify_button)
        self.modify_name_groupbox.setLayout(self.modify_name_layout)
        
        self.modify_attribute_groupbox = QGroupBox()
        self.modify_attribute_layout = QVBoxLayout()
        self.modify_attribute_variable_label = QLabel("Variable Name")
        self.modify_attribute_variable_lineedit = QLineEdit("Enter Variable Name")
        self.modify_attribute_variable_confirm_button = QPushButton("Confirm")
        self.modify_attribute_variable_cancel_button = QPushButton("Cancel")
        self.modify_attribute_label = QLabel("Variable Information Name")
        self.modify_attribute_lineedit = QLineEdit("Enter Variable Information Name")
        self.modify_attribute_confirm_button = QPushButton("Confirm")
        self.modify_attribute_cancel_button = QPushButton("Cancel")
        self.modify_new_attribute_label = QLabel("New Variable Information Name")
        self.modify_new_attribute_lineedit = QLineEdit("Enter New Variable Information Name")
        self.modify_new_attribute_value_label = QLabel("New Variable Information Value")
        self.modify_new_attribute_value_lineedit = QLineEdit("Enter New Variable Information Value")
        self.modify_new_attribute_modify_button = QPushButton("Modify Variable Information")
        
        self.modify_attribute_variable_lineedit.setEnabled(True)
        self.modify_attribute_variable_confirm_button.setEnabled(True)
        self.modify_attribute_variable_cancel_button.setEnabled(False)
        self.modify_attribute_lineedit.setEnabled(False)
        self.modify_attribute_confirm_button.setEnabled(False)
        self.modify_attribute_cancel_button.setEnabled(False)
        self.modify_new_attribute_lineedit.setEnabled(False)
        self.modify_new_attribute_value_lineedit.setEnabled(False)
        self.modify_new_attribute_modify_button.setEnabled(False)
        
        self.modify_attribute_layout.addWidget(self.modify_attribute_variable_label)
        self.modify_attribute_layout.addWidget(self.modify_attribute_variable_lineedit)
        self.modify_attribute_layout.addWidget(self.modify_attribute_variable_confirm_button)
        self.modify_attribute_layout.addWidget(self.modify_attribute_variable_cancel_button)
        self.modify_attribute_layout.addWidget(self.modify_attribute_label)
        self.modify_attribute_layout.addWidget(self.modify_attribute_lineedit)
        self.modify_attribute_layout.addWidget(self.modify_attribute_confirm_button)
        self.modify_attribute_layout.addWidget(self.modify_attribute_cancel_button)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_label)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_lineedit)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_value_label)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_value_lineedit)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_modify_button)
        self.modify_attribute_groupbox.setLayout(self.modify_attribute_layout)
        
        self.modify_tabwidget.addTab(self.modify_name_groupbox, "Name")
        self.modify_tabwidget.addTab(self.modify_attribute_groupbox, "Variable Information")
        
        return self.modify_tabwidget
    
    
    def delete_variable(self):
        
        self.delete_tabwidget = QTabWidget()
        
        self.delete_name_groupbox = QGroupBox()
        self.delete_name_layout = QVBoxLayout()
        self.delete_name_label = QLabel("Variable Name")
        self.delete_name_lineedit = QLineEdit("Enter Variable Name")
        self.delete_name_button = QPushButton("Delete Variable")
        
        self.delete_name_layout.addWidget(self.delete_name_label)
        self.delete_name_layout.addWidget(self.delete_name_lineedit)
        self.delete_name_layout.addWidget(self.delete_name_button)
        self.delete_name_groupbox.setLayout(self.delete_name_layout)
        
        self.delete_attribute_groupbox = QGroupBox()
        self.delete_attribute_layout = QVBoxLayout()
        self.delete_attribute_variable_label = QLabel("Variable Name")
        self.delete_attribute_variable_lineedit = QLineEdit("Enter Variable Name")
        self.delete_attribute_confirm_button = QPushButton("Confirm")
        self.delete_attribute_cancel_button = QPushButton("Cancel")
        self.delete_attribute_label = QLabel("Variable Information Name")
        self.delete_attribute_lineedit = QLineEdit("Enter Variable Information Name")
        self.delete_attribute_button = QPushButton("Delete Variable Information")
        
        self.delete_attribute_variable_lineedit.setEnabled(True)
        self.delete_attribute_confirm_button.setEnabled(True)
        self.delete_attribute_cancel_button.setEnabled(False)
        self.delete_attribute_lineedit.setEnabled(False)
        self.delete_attribute_button.setEnabled(False)
        
        self.delete_attribute_layout.addWidget(self.delete_attribute_variable_label)
        self.delete_attribute_layout.addWidget(self.delete_attribute_variable_lineedit)
        self.delete_attribute_layout.addWidget(self.delete_attribute_confirm_button)
        self.delete_attribute_layout.addWidget(self.delete_attribute_cancel_button)
        self.delete_attribute_layout.addWidget(self.delete_attribute_label)
        self.delete_attribute_layout.addWidget(self.delete_attribute_lineedit)
        self.delete_attribute_layout.addWidget(self.delete_attribute_button)
        self.delete_attribute_groupbox.setLayout(self.delete_attribute_layout)
        
        self.delete_tabwidget.addTab(self.delete_name_groupbox, "Name")
        self.delete_tabwidget.addTab(self.delete_attribute_groupbox, "Variable Information")
        
        return self.delete_tabwidget

    
    
    
# Définition de la classe AttributeTabWidget




class AttributeTabWidget(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.attributetab_layout = QVBoxLayout()
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.add_attribute(), "Add")
        self.tabwidget.addTab(self.modify_attribute(), "Modify")
        self.tabwidget.addTab(self.delete_attribute(), "Delete")
        
        self.attributetab_layout.addWidget(self.tabwidget)
        
        self.setLayout(self.attributetab_layout)
    
    
    def add_attribute(self):
        
        self.add_tabwidget = QTabWidget()
        
        self.add_name_groupbox = QGroupBox()
        self.add_name_layout = QVBoxLayout()
        self.add_name_label = QLabel("New Global Information Name")
        self.add_name_lineedit = QLineEdit("Enter New Global Information Name")
        self.add_name_button = QPushButton("Add New Global Information")
        
        self.add_name_layout.addWidget(self.add_name_label)
        self.add_name_layout.addWidget(self.add_name_lineedit)
        self.add_name_layout.addWidget(self.add_name_button)
        self.add_name_groupbox.setLayout(self.add_name_layout)
        
        self.add_value_groupbox = QGroupBox()
        self.add_value_layout = QVBoxLayout()
        self.add_value_attribute_label = QLabel("Global Information Name")
        self.add_value_attribute_lineedit = QLineEdit("Enter Global Information Name")
        self.add_value_attribute_confirm_button = QPushButton("Confirm")
        self.add_value_attribute_cancel_button = QPushButton("Cancel")
        self.add_value_label = QLabel("New Global Information Value")
        self.add_value_lineedit = QLineEdit("Enter New Global Information Value")
        self.add_value_button = QPushButton("Add New Global Information Value")
        
        self.add_value_attribute_lineedit.setEnabled(True)
        self.add_value_attribute_confirm_button.setEnabled(True)
        self.add_value_attribute_cancel_button.setEnabled(False)
        self.add_value_lineedit.setEnabled(False)
        self.add_value_button.setEnabled(False)
        
        self.add_value_layout.addWidget(self.add_value_attribute_label)
        self.add_value_layout.addWidget(self.add_value_attribute_lineedit)
        self.add_value_layout.addWidget(self.add_value_attribute_confirm_button)
        self.add_value_layout.addWidget(self.add_value_attribute_cancel_button)
        self.add_value_layout.addWidget(self.add_value_label)
        self.add_value_layout.addWidget(self.add_value_lineedit)
        self.add_value_layout.addWidget(self.add_value_button)
        self.add_value_groupbox.setLayout(self.add_value_layout)
        
        self.add_tabwidget.addTab(self.add_name_groupbox, "Name")
        self.add_tabwidget.addTab(self.add_value_groupbox, "Information")
        
        return self.add_tabwidget
    
    
    def modify_attribute(self):
        
        self.modify_tabwidget = QTabWidget()
        
        self.modify_name_groupbox = QGroupBox()
        self.modify_name_layout = QVBoxLayout()
        self.modify_name_label = QLabel("Global Information Name")
        self.modify_name_lineedit = QLineEdit("Enter Global Information Name")
        self.modify_name_confirm_button = QPushButton("Confirm")
        self.modify_name_cancel_button = QPushButton("Cancel")
        self.modify_new_name_label = QLabel("New Global Information Name")
        self.modify_new_name_lineedit = QLineEdit("Enter New Global Information Name")
        self.modify_new_name_modify_button = QPushButton("Modify Global Information")
        
        self.modify_name_lineedit.setEnabled(True)
        self.modify_name_confirm_button.setEnabled(True)
        self.modify_name_cancel_button.setEnabled(False)
        self.modify_new_name_lineedit.setEnabled(False)
        self.modify_new_name_modify_button.setEnabled(False)
        
        self.modify_name_layout.addWidget(self.modify_name_label)
        self.modify_name_layout.addWidget(self.modify_name_lineedit)
        self.modify_name_layout.addWidget(self.modify_name_confirm_button)
        self.modify_name_layout.addWidget(self.modify_name_cancel_button)
        self.modify_name_layout.addWidget(self.modify_new_name_label)
        self.modify_name_layout.addWidget(self.modify_new_name_lineedit)
        self.modify_name_layout.addWidget(self.modify_new_name_modify_button)
        self.modify_name_groupbox.setLayout(self.modify_name_layout)
        
        self.modify_value_groupbox = QGroupBox()
        self.modify_value_layout = QVBoxLayout()
        self.modify_value_attribute_label = QLabel("Global Information Name")
        self.modify_value_attribute_lineedit = QLineEdit("Enter Global Information Name")
        self.modify_value_attribute_confirm_button = QPushButton("Confirm")
        self.modify_value_attribute_cancel_button = QPushButton("Cancel")
        self.modify_new_value_label = QLabel("New Global Information Value")
        self.modify_new_value_lineedit = QLineEdit("Enter New Global Information Value")
        self.modify_new_value_modify_button = QPushButton("Modify Global Information")
        
        self.modify_value_attribute_lineedit.setEnabled(True)
        self.modify_value_attribute_confirm_button.setEnabled(True)
        self.modify_value_attribute_cancel_button.setEnabled(False)
        self.modify_new_value_lineedit.setEnabled(False)
        self.modify_new_value_modify_button.setEnabled(False)
        
        self.modify_value_layout.addWidget(self.modify_value_attribute_label)
        self.modify_value_layout.addWidget(self.modify_value_attribute_lineedit)
        self.modify_value_layout.addWidget(self.modify_value_attribute_confirm_button)
        self.modify_value_layout.addWidget(self.modify_value_attribute_cancel_button)
        self.modify_value_layout.addWidget(self.modify_new_value_label)
        self.modify_value_layout.addWidget(self.modify_new_value_lineedit)
        self.modify_value_layout.addWidget(self.modify_new_value_modify_button)
        self.modify_value_groupbox.setLayout(self.modify_value_layout)
        
        self.modify_tabwidget.addTab(self.modify_name_groupbox, "Name")
        self.modify_tabwidget.addTab(self.modify_value_groupbox, "Information")
        
        return self.modify_tabwidget
    
    
    def delete_attribute(self):
        
        self.delete_tabwidget = QTabWidget()
        
        self.delete_name_groupbox = QGroupBox()
        self.delete_name_layout = QVBoxLayout()
        self.delete_name_label = QLabel("Global Information Name")
        self.delete_name_lineedit = QLineEdit("Enter Global Information Name")
        self.delete_name_button = QPushButton("Delete Global Information")
        
        self.delete_name_layout.addWidget(self.delete_name_label)
        self.delete_name_layout.addWidget(self.delete_name_lineedit)
        self.delete_name_layout.addWidget(self.delete_name_button)
        self.delete_name_groupbox.setLayout(self.delete_name_layout)
        
        self.delete_value_groupbox = QGroupBox()
        self.delete_value_layout = QVBoxLayout()
        self.delete_value_attribute_label = QLabel("Global Information Name")
        self.delete_value_attribute_lineedit = QLineEdit("Enter Global Information Name")
        self.delete_value_attribute_confirm_button = QPushButton("Confirm")
        self.delete_value_attribute_cancel_button = QPushButton("Cancel")
        self.delete_value_button = QPushButton("Delete Global Information Value")
        
        self.delete_value_attribute_lineedit.setEnabled(True)
        self.delete_value_attribute_confirm_button.setEnabled(True)
        self.delete_value_attribute_cancel_button.setEnabled(False)
        self.delete_value_button.setEnabled(False)
        
        self.delete_value_layout.addWidget(self.delete_value_attribute_label)
        self.delete_value_layout.addWidget(self.delete_value_attribute_lineedit)
        self.delete_value_layout.addWidget(self.delete_value_attribute_confirm_button)
        self.delete_value_layout.addWidget(self.delete_value_attribute_cancel_button)
        self.delete_value_layout.addWidget(self.delete_value_button)
        self.delete_value_groupbox.setLayout(self.delete_value_layout)
        
        self.delete_tabwidget.addTab(self.delete_name_groupbox, "Name")
        self.delete_tabwidget.addTab(self.delete_value_groupbox, "Information")
        
        return self.delete_tabwidget




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

        self.groupbox = QGroupBox("Catalog Settings")
        self.groupbox_layout = QVBoxLayout()
        self.tabwidget = QTabWidget()
        self.dimension_tabwidget = DimensionTabWidget()
        self.variable_tabwidget = VariableTabWidget()
        self.attribute_tabwidget = AttributeTabWidget()

        self.tabwidget.addTab(self.dimension_tabwidget, "Dimension")
        self.tabwidget.addTab(self.variable_tabwidget, "Variable")
        self.tabwidget.addTab(self.attribute_tabwidget, "Global Information")

        self.groupbox_layout.addWidget(self.tabwidget)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuecatalogsettings_layout.addWidget(self.groupbox)
    
    
    def connect_signals(self):
        
        self.dimension_tabwidget.add_name_button.clicked.connect(self.controleurcatalogsettings.dimension_name_add)
        
        self.dimension_tabwidget.modify_name_confirm_button.clicked.connect(self.controleurcatalogsettings.dimension_name_modify_confirm)
        self.dimension_tabwidget.modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.dimension_name_modify_cancel)
        self.dimension_tabwidget.modify_new_name_modify_button.clicked.connect(self.controleurcatalogsettings.dimension_name_modify)
        
        self.dimension_tabwidget.delete_name_button.clicked.connect(self.controleurcatalogsettings.dimension_name_delete)
        
        self.variable_tabwidget.add_name_button.clicked.connect(self.controleurcatalogsettings.variable_name_add)
        self.variable_tabwidget.add_attribute_variable_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_add_confirm)
        self.variable_tabwidget.add_attribute_variable_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_add_cancel)
        self.variable_tabwidget.add_attribute_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_add)
        
        self.variable_tabwidget.modify_name_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_name_modify_confirm)
        self.variable_tabwidget.modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_name_modify_cancel)
        self.variable_tabwidget.modify_new_name_modify_button.clicked.connect(self.controleurcatalogsettings.variable_name_modify)
        self.variable_tabwidget.modify_attribute_variable_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_variable_modify_confirm)
        self.variable_tabwidget.modify_attribute_variable_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_variable_modify_cancel)
        self.variable_tabwidget.modify_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_modify_confirm)
        self.variable_tabwidget.modify_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_modify_cancel)
        self.variable_tabwidget.modify_new_attribute_modify_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_modify)
        
        self.variable_tabwidget.delete_name_button.clicked.connect(self.controleurcatalogsettings.variable_name_delete)
        self.variable_tabwidget.delete_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_delete_confirm)
        self.variable_tabwidget.delete_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_delete_cancel)
        self.variable_tabwidget.delete_attribute_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_delete)
        
        self.attribute_tabwidget.add_name_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_add)
        self.attribute_tabwidget.add_value_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_add_confirm)
        self.attribute_tabwidget.add_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_add_cancel)
        self.attribute_tabwidget.add_value_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_add)
        
        self.attribute_tabwidget.modify_name_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_modify_confirm)
        self.attribute_tabwidget.modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_modify_cancel)
        self.attribute_tabwidget.modify_new_name_modify_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_modify)
        self.attribute_tabwidget.modify_value_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_modify_confirm)
        self.attribute_tabwidget.modify_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_modify_cancel)
        self.attribute_tabwidget.modify_new_value_modify_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_modify)
        
        self.attribute_tabwidget.delete_name_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_delete)
        self.attribute_tabwidget.delete_value_attribute_confirm_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_delete_confirm)
        self.attribute_tabwidget.delete_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_delete_cancel)
        self.attribute_tabwidget.delete_value_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_delete)




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
