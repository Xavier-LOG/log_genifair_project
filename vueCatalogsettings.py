# Importation des fichiers




from controleurCatalogsettings import controleurCatalogsettings




# Importation des bibliothèques




from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton, QGroupBox, QTabWidget, QScrollArea, QComboBox




# Définition de la classe DimensionTabWidget




class DimensionTabWidget(QWidget):
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        super().__init__()
        self.init_ui()
    
    
    # Définition des méthodes
    
    
    def init_ui(self):
        
        self.dimensiontab_layout = QVBoxLayout()
        self.dimensiontab_scrollarea = QScrollArea()
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.add_dimension(), "Add")
        self.tabwidget.addTab(self.modify_dimension(), "Modify")
        self.tabwidget.addTab(self.delete_dimension(), "Delete")
        
        self.dimensiontab_scrollarea.setWidgetResizable(True)
        self.dimensiontab_scrollarea.setWidget(self.tabwidget)
        
        self.dimensiontab_layout.addWidget(self.dimensiontab_scrollarea)
        
        self.setLayout(self.dimensiontab_layout)
    
    
    def add_dimension(self):
        
        self.add_tabwidget = QTabWidget()
        
        self.add_name_groupbox = QGroupBox()
        self.add_name_layout = QVBoxLayout()
        self.add_name_label = QLabel("New Dimension Name")
        self.add_name_combobox = QComboBox()
        
        self.add_name_combobox.setEditable(True)
        
        self.add_name_layout.addWidget(self.add_name_label)
        self.add_name_layout.addWidget(self.add_name_combobox)
        self.add_name_groupbox.setLayout(self.add_name_layout)
        
        self.add_value_groupbox = QGroupBox()
        self.add_value_layout = QVBoxLayout()
        self.add_value_dimension_label = QLabel("Dimension Name")
        self.add_value_dimension_combobox = QComboBox()
        self.add_value_dimension_cancel_button = QPushButton("Cancel")
        self.add_value_label = QLabel("New Dimension Value")
        self.add_value_combobox = QComboBox()
        
        self.add_value_dimension_combobox.setEditable(True)
        self.add_value_combobox.setEditable(True)
        
        self.add_value_dimension_combobox.setEnabled(True)
        self.add_value_dimension_cancel_button.setEnabled(False)
        self.add_value_combobox.setEnabled(False)
        
        self.add_value_layout.addWidget(self.add_value_dimension_label)
        self.add_value_layout.addWidget(self.add_value_dimension_combobox)
        self.add_value_layout.addWidget(self.add_value_dimension_cancel_button)
        self.add_value_layout.addWidget(self.add_value_label)
        self.add_value_layout.addWidget(self.add_value_combobox)
        self.add_value_groupbox.setLayout(self.add_value_layout)
        
        self.add_tabwidget.addTab(self.add_name_groupbox, "Name")
        self.add_tabwidget.addTab(self.add_value_groupbox, "Value")
        
        return self.add_tabwidget
    
    
    def modify_dimension(self):
        
        self.modify_tabwidget = QTabWidget()
        
        self.modify_name_groupbox = QGroupBox()
        self.modify_name_layout = QVBoxLayout()
        self.modify_name_label = QLabel("Dimension Name")
        self.modify_name_combobox = QComboBox()
        self.modify_name_cancel_button = QPushButton("Cancel")
        self.modify_new_name_label = QLabel("New Dimension Name")
        self.modify_new_name_combobox = QComboBox()
        self.modify_new_name_modify_button = QPushButton("Modify Dimension Name")
        
        self.modify_name_combobox.setEditable(True)
        self.modify_new_name_combobox.setEditable(True)
        
        self.modify_name_combobox.setEnabled(True)
        self.modify_name_cancel_button.setEnabled(False)
        self.modify_new_name_combobox.setEnabled(False)
        self.modify_new_name_modify_button.setEnabled(False)
        
        self.modify_name_layout.addWidget(self.modify_name_label)
        self.modify_name_layout.addWidget(self.modify_name_combobox)
        self.modify_name_layout.addWidget(self.modify_name_cancel_button)
        self.modify_name_layout.addWidget(self.modify_new_name_label)
        self.modify_name_layout.addWidget(self.modify_new_name_combobox)
        self.modify_name_groupbox.setLayout(self.modify_name_layout)
        
        self.modify_value_groupbox = QGroupBox()
        self.modify_value_layout = QVBoxLayout()
        self.modify_value_dimension_label = QLabel("Dimension Name")
        self.modify_value_dimension_combobox = QComboBox()
        self.modify_value_dimension_cancel_button = QPushButton("Cancel")
        self.modify_new_value_label = QLabel("New Dimension Value")
        self.modify_new_value_combobox = QComboBox()
        
        self.modify_value_dimension_combobox.setEditable(True)
        self.modify_new_value_combobox.setEditable(True)
        
        self.modify_value_dimension_combobox.setEnabled(True)
        self.modify_value_dimension_cancel_button.setEnabled(False)
        self.modify_new_value_combobox.setEnabled(False)
        
        self.modify_value_layout.addWidget(self.modify_value_dimension_label)
        self.modify_value_layout.addWidget(self.modify_value_dimension_combobox)
        self.modify_value_layout.addWidget(self.modify_value_dimension_cancel_button)
        self.modify_value_layout.addWidget(self.modify_new_value_label)
        self.modify_value_layout.addWidget(self.modify_new_value_combobox)
        self.modify_value_groupbox.setLayout(self.modify_value_layout)
        
        self.modify_tabwidget.addTab(self.modify_name_groupbox, "Name")
        self.modify_tabwidget.addTab(self.modify_value_groupbox, "Value")
        
        return self.modify_tabwidget
    
    
    def delete_dimension(self):
        
        self.delete_tabwidget = QTabWidget()
        
        self.delete_name_groupbox = QGroupBox()
        self.delete_name_layout = QVBoxLayout()
        self.delete_name_label = QLabel("Dimension Name")
        self.delete_name_combobox = QComboBox()
        
        self.delete_name_combobox.setEditable(True)
        
        self.delete_name_layout.addWidget(self.delete_name_label)
        self.delete_name_layout.addWidget(self.delete_name_combobox)
        self.delete_name_groupbox.setLayout(self.delete_name_layout)
        
        self.delete_value_groupbox = QGroupBox()
        self.delete_value_layout = QVBoxLayout()
        self.delete_value_dimension_label = QLabel("Dimension Name")
        self.delete_value_dimension_combobox = QComboBox()
        
        self.delete_value_dimension_combobox.setEditable(True)
        
        self.delete_value_layout.addWidget(self.delete_value_dimension_label)
        self.delete_value_layout.addWidget(self.delete_value_dimension_combobox)
        self.delete_value_groupbox.setLayout(self.delete_value_layout)
        
        self.delete_tabwidget.addTab(self.delete_name_groupbox, "Name")
        self.delete_tabwidget.addTab(self.delete_value_groupbox, "Value")
        
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
        self.variabletab_scrollarea = QScrollArea()
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.add_variable(), "Add")
        self.tabwidget.addTab(self.modify_variable(), "Modify")
        self.tabwidget.addTab(self.delete_variable(), "Delete")
        
        self.variabletab_scrollarea.setWidgetResizable(True)
        self.variabletab_scrollarea.setWidget(self.tabwidget)
        
        self.variabletab_layout.addWidget(self.variabletab_scrollarea)
        
        self.setLayout(self.variabletab_layout)
    
    
    def add_variable(self):
        
        self.add_tabwidget = QTabWidget()
        
        self.add_name_groupbox = QGroupBox()
        self.add_name_layout = QVBoxLayout()
        self.add_name_label = QLabel("New Variable Name")
        self.add_name_combobox = QComboBox()
        self.add_name_cancel_button = QPushButton("Cancel")
        self.add_dimension_label = QLabel("New Variable Dimension")
        self.add_dimension_combobox = QComboBox()
        
        self.add_name_combobox.setEditable(True)
        self.add_dimension_combobox.setEditable(True)
        
        self.add_name_combobox.setEnabled(True)
        self.add_dimension_combobox.setEnabled(False)
        self.add_name_cancel_button.setEnabled(False)
        
        self.add_name_layout.addWidget(self.add_name_label)
        self.add_name_layout.addWidget(self.add_name_combobox)
        self.add_name_layout.addWidget(self.add_name_cancel_button)
        self.add_name_layout.addWidget(self.add_dimension_label)
        self.add_name_layout.addWidget(self.add_dimension_combobox)
        self.add_name_groupbox.setLayout(self.add_name_layout)
        
        self.add_attribute_groupbox = QGroupBox()
        self.add_attribute_layout = QVBoxLayout()
        self.add_attribute_variable_label = QLabel("Variable Name")
        self.add_attribute_variable_combobox = QComboBox()
        self.add_attribute_variable_cancel_button = QPushButton("Cancel")
        self.add_attribute_label = QLabel("Variable Attribute Name")
        self.add_attribute_combobox = QComboBox()
        self.add_attribute_cancel_button = QPushButton("Cancel")
        self.add_attribute_value_label = QLabel("Variable Attribute Value")
        self.add_attribute_value_combobox = QComboBox()
        
        self.add_attribute_variable_combobox.setEditable(True)
        self.add_attribute_combobox.setEditable(True)
        self.add_attribute_value_combobox.setEditable(True)
        
        self.add_attribute_variable_combobox.setEnabled(True)
        self.add_attribute_variable_cancel_button.setEnabled(False)
        self.add_attribute_combobox.setEnabled(False)
        self.add_attribute_cancel_button.setEnabled(False)
        self.add_attribute_value_combobox.setEnabled(False)
        
        self.add_attribute_layout.addWidget(self.add_attribute_variable_label)
        self.add_attribute_layout.addWidget(self.add_attribute_variable_combobox)
        self.add_attribute_layout.addWidget(self.add_attribute_variable_cancel_button)
        self.add_attribute_layout.addWidget(self.add_attribute_label)
        self.add_attribute_layout.addWidget(self.add_attribute_combobox)
        self.add_attribute_layout.addWidget(self.add_attribute_cancel_button)
        self.add_attribute_layout.addWidget(self.add_attribute_value_label)
        self.add_attribute_layout.addWidget(self.add_attribute_value_combobox)
        self.add_attribute_groupbox.setLayout(self.add_attribute_layout)
        
        self.add_tabwidget.addTab(self.add_name_groupbox, "Name")
        self.add_tabwidget.addTab(self.add_attribute_groupbox, "Attribute")
        
        return self.add_tabwidget
    
    
    def modify_variable(self):
        
        self.modify_tabwidget = QTabWidget()
        
        self.modify_name_groupbox = QGroupBox()
        self.modify_name_layout = QVBoxLayout()
        self.modify_name_label = QLabel("Variable Name")
        self.modify_name_combobox = QComboBox()
        self.modify_name_cancel_button = QPushButton("Cancel")
        self.modify_new_name_label = QLabel("New Variable Name")
        self.modify_new_name_combobox = QComboBox()
        self.modify_new_name_cancel_button = QPushButton("Cancel")
        self.modify_dimension_label = QLabel("New Variable Dimension")
        self.modify_dimension_combobox = QComboBox()
        
        self.modify_name_combobox.setEditable(True)
        self.modify_new_name_combobox.setEditable(True)
        self.modify_dimension_combobox.setEditable(True)
        
        self.modify_name_combobox.setEnabled(True)
        self.modify_name_cancel_button.setEnabled(False)
        self.modify_new_name_combobox.setEnabled(False)
        self.modify_new_name_cancel_button.setEnabled(False)
        self.modify_dimension_combobox.setEnabled(False)
        
        self.modify_name_layout.addWidget(self.modify_name_label)
        self.modify_name_layout.addWidget(self.modify_name_combobox)
        self.modify_name_layout.addWidget(self.modify_name_cancel_button)
        self.modify_name_layout.addWidget(self.modify_new_name_label)
        self.modify_name_layout.addWidget(self.modify_new_name_combobox)
        self.modify_name_layout.addWidget(self.modify_new_name_cancel_button)
        self.modify_name_layout.addWidget(self.modify_dimension_label)
        self.modify_name_layout.addWidget(self.modify_dimension_combobox)
        self.modify_name_groupbox.setLayout(self.modify_name_layout)
        
        self.modify_attribute_groupbox = QGroupBox()
        self.modify_attribute_layout = QVBoxLayout()
        self.modify_attribute_variable_label = QLabel("Variable Name")
        self.modify_attribute_variable_combobox = QComboBox()
        self.modify_attribute_variable_cancel_button = QPushButton("Cancel")
        self.modify_attribute_label = QLabel("Variable Attribute Name")
        self.modify_attribute_combobox = QComboBox()
        self.modify_attribute_cancel_button = QPushButton("Cancel")
        self.modify_new_attribute_label = QLabel("New Variable Attribute Name")
        self.modify_new_attribute_combobox = QComboBox()
        self.modify_new_attribute_cancel_button = QPushButton("Cancel")
        self.modify_new_attribute_value_label = QLabel("New Variable Attribute Value")
        self.modify_new_attribute_value_combobox = QComboBox()
        
        self.modify_attribute_variable_combobox.setEditable(True)
        self.modify_attribute_combobox.setEditable(True)
        self.modify_new_attribute_combobox.setEditable(True)
        self.modify_new_attribute_value_combobox.setEditable(True)
        
        self.modify_attribute_variable_combobox.setEnabled(True)
        self.modify_attribute_variable_cancel_button.setEnabled(False)
        self.modify_attribute_combobox.setEnabled(False)
        self.modify_attribute_cancel_button.setEnabled(False)
        self.modify_new_attribute_combobox.setEnabled(False)
        self.modify_new_attribute_cancel_button.setEnabled(False)
        self.modify_new_attribute_value_combobox.setEnabled(False)
        
        self.modify_attribute_layout.addWidget(self.modify_attribute_variable_label)
        self.modify_attribute_layout.addWidget(self.modify_attribute_variable_combobox)
        self.modify_attribute_layout.addWidget(self.modify_attribute_variable_cancel_button)
        self.modify_attribute_layout.addWidget(self.modify_attribute_label)
        self.modify_attribute_layout.addWidget(self.modify_attribute_combobox)
        self.modify_attribute_layout.addWidget(self.modify_attribute_cancel_button)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_label)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_combobox)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_cancel_button)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_value_label)
        self.modify_attribute_layout.addWidget(self.modify_new_attribute_value_combobox)
        self.modify_attribute_groupbox.setLayout(self.modify_attribute_layout)
        
        self.modify_tabwidget.addTab(self.modify_name_groupbox, "Name")
        self.modify_tabwidget.addTab(self.modify_attribute_groupbox, "Attribute")
        
        return self.modify_tabwidget
    
    
    def delete_variable(self):
        
        self.delete_tabwidget = QTabWidget()
        
        self.delete_name_groupbox = QGroupBox()
        self.delete_name_layout = QVBoxLayout()
        self.delete_name_label = QLabel("Variable Name")
        self.delete_name_combobox = QComboBox()
        
        self.delete_name_combobox.setEditable(True)
        
        self.delete_name_layout.addWidget(self.delete_name_label)
        self.delete_name_layout.addWidget(self.delete_name_combobox)
        self.delete_name_groupbox.setLayout(self.delete_name_layout)
        
        self.delete_attribute_groupbox = QGroupBox()
        self.delete_attribute_layout = QVBoxLayout()
        self.delete_attribute_variable_label = QLabel("Variable Name")
        self.delete_attribute_variable_combobox = QComboBox()
        self.delete_attribute_cancel_button = QPushButton("Cancel")
        self.delete_attribute_label = QLabel("Variable Attribute Name")
        self.delete_attribute_combobox = QComboBox()
        
        self.delete_attribute_variable_combobox.setEditable(True)
        self.delete_attribute_combobox.setEditable(True)
        
        self.delete_attribute_variable_combobox.setEnabled(True)
        self.delete_attribute_cancel_button.setEnabled(False)
        self.delete_attribute_combobox.setEnabled(False)
        
        self.delete_attribute_layout.addWidget(self.delete_attribute_variable_label)
        self.delete_attribute_layout.addWidget(self.delete_attribute_variable_combobox)
        self.delete_attribute_layout.addWidget(self.delete_attribute_cancel_button)
        self.delete_attribute_layout.addWidget(self.delete_attribute_label)
        self.delete_attribute_layout.addWidget(self.delete_attribute_combobox)
        self.delete_attribute_groupbox.setLayout(self.delete_attribute_layout)
        
        self.delete_tabwidget.addTab(self.delete_name_groupbox, "Name")
        self.delete_tabwidget.addTab(self.delete_attribute_groupbox, "Attribute")
        
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
        self.attributetab_scrollarea = QScrollArea()
        self.tabwidget = QTabWidget()
        
        self.tabwidget.addTab(self.add_attribute(), "Add")
        self.tabwidget.addTab(self.modify_attribute(), "Modify")
        self.tabwidget.addTab(self.delete_attribute(), "Delete")
        
        self.attributetab_scrollarea.setWidgetResizable(True)
        self.attributetab_scrollarea.setWidget(self.tabwidget)
        
        self.attributetab_layout.addWidget(self.attributetab_scrollarea)
        
        self.setLayout(self.attributetab_layout)
    
    
    def add_attribute(self):
        
        self.add_tabwidget = QTabWidget()
        
        self.add_name_groupbox = QGroupBox()
        self.add_name_layout = QVBoxLayout()
        self.add_name_label = QLabel("New Global Attribute Name")
        self.add_name_combobox = QComboBox()
        
        self.add_name_combobox.setEditable(True)
        
        self.add_name_layout.addWidget(self.add_name_label)
        self.add_name_layout.addWidget(self.add_name_combobox)
        self.add_name_groupbox.setLayout(self.add_name_layout)
        
        self.add_value_groupbox = QGroupBox()
        self.add_value_layout = QVBoxLayout()
        self.add_value_attribute_label = QLabel("Global Attribute Name")
        self.add_value_attribute_combobox = QComboBox()
        self.add_value_attribute_cancel_button = QPushButton("Cancel")
        self.add_value_label = QLabel("New Global Attribute Value")
        self.add_value_combobox = QComboBox()
        
        self.add_value_attribute_combobox.setEditable(True)
        self.add_value_combobox.setEditable(True)
        
        self.add_value_attribute_combobox.setEnabled(True)
        self.add_value_attribute_cancel_button.setEnabled(False)
        self.add_value_combobox.setEnabled(False)
        
        self.add_value_layout.addWidget(self.add_value_attribute_label)
        self.add_value_layout.addWidget(self.add_value_attribute_combobox)
        self.add_value_layout.addWidget(self.add_value_attribute_cancel_button)
        self.add_value_layout.addWidget(self.add_value_label)
        self.add_value_layout.addWidget(self.add_value_combobox)
        self.add_value_groupbox.setLayout(self.add_value_layout)
        
        self.add_tabwidget.addTab(self.add_name_groupbox, "Name")
        self.add_tabwidget.addTab(self.add_value_groupbox, "Value")
        
        return self.add_tabwidget
    
    
    def modify_attribute(self):
        
        self.modify_tabwidget = QTabWidget()
        
        self.modify_name_groupbox = QGroupBox()
        self.modify_name_layout = QVBoxLayout()
        self.modify_name_label = QLabel("Global Attribute Name")
        self.modify_name_combobox = QComboBox()
        self.modify_name_cancel_button = QPushButton("Cancel")
        self.modify_new_name_label = QLabel("New Global Attribute Name")
        self.modify_new_name_combobox = QComboBox()
        
        self.modify_name_combobox.setEditable(True)
        self.modify_new_name_combobox.setEditable(True)
        
        self.modify_name_combobox.setEnabled(True)
        self.modify_name_cancel_button.setEnabled(False)
        self.modify_new_name_combobox.setEnabled(False)
        
        self.modify_name_layout.addWidget(self.modify_name_label)
        self.modify_name_layout.addWidget(self.modify_name_combobox)
        self.modify_name_layout.addWidget(self.modify_name_cancel_button)
        self.modify_name_layout.addWidget(self.modify_new_name_label)
        self.modify_name_layout.addWidget(self.modify_new_name_combobox)
        self.modify_name_groupbox.setLayout(self.modify_name_layout)
        
        self.modify_value_groupbox = QGroupBox()
        self.modify_value_layout = QVBoxLayout()
        self.modify_value_attribute_label = QLabel("Global Attribute Name")
        self.modify_value_attribute_combobox = QComboBox()
        self.modify_value_attribute_cancel_button = QPushButton("Cancel")
        self.modify_new_value_label = QLabel("New Global Attribute Value")
        self.modify_new_value_combobox = QComboBox()
        
        self.modify_value_attribute_combobox.setEditable(True)
        self.modify_new_value_combobox.setEditable(True)
        
        self.modify_value_attribute_combobox.setEnabled(True)
        self.modify_value_attribute_cancel_button.setEnabled(False)
        self.modify_new_value_combobox.setEnabled(False)
        
        self.modify_value_layout.addWidget(self.modify_value_attribute_label)
        self.modify_value_layout.addWidget(self.modify_value_attribute_combobox)
        self.modify_value_layout.addWidget(self.modify_value_attribute_cancel_button)
        self.modify_value_layout.addWidget(self.modify_new_value_label)
        self.modify_value_layout.addWidget(self.modify_new_value_combobox)
        self.modify_value_groupbox.setLayout(self.modify_value_layout)
        
        self.modify_tabwidget.addTab(self.modify_name_groupbox, "Name")
        self.modify_tabwidget.addTab(self.modify_value_groupbox, "Value")
        
        return self.modify_tabwidget
    
    
    def delete_attribute(self):
        
        self.delete_tabwidget = QTabWidget()
        
        self.delete_name_groupbox = QGroupBox()
        self.delete_name_layout = QVBoxLayout()
        self.delete_name_label = QLabel("Global Attribute Name")
        self.delete_name_combobox = QComboBox()
        
        self.delete_name_combobox.setEditable(True)
        
        self.delete_name_layout.addWidget(self.delete_name_label)
        self.delete_name_layout.addWidget(self.delete_name_combobox)
        self.delete_name_groupbox.setLayout(self.delete_name_layout)
        
        self.delete_value_groupbox = QGroupBox()
        self.delete_value_layout = QVBoxLayout()
        self.delete_value_attribute_label = QLabel("Global Attribute Name")
        self.delete_value_attribute_combobox = QComboBox()
        
        self.delete_value_attribute_combobox.setEditable(True)
        
        self.delete_value_layout.addWidget(self.delete_value_attribute_label)
        self.delete_value_layout.addWidget(self.delete_value_attribute_combobox)
        self.delete_value_groupbox.setLayout(self.delete_value_layout)
        
        self.delete_tabwidget.addTab(self.delete_name_groupbox, "Name")
        self.delete_tabwidget.addTab(self.delete_value_groupbox, "Value")
        
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
        self.button = QPushButton("Create Specific Catalog With File")
        self.tabwidget = QTabWidget()
        self.dimension_tabwidget = DimensionTabWidget()
        self.variable_tabwidget = VariableTabWidget()
        self.attribute_tabwidget = AttributeTabWidget()

        self.tabwidget.addTab(self.dimension_tabwidget, "Dimension")
        self.tabwidget.addTab(self.variable_tabwidget, "Variable")
        self.tabwidget.addTab(self.attribute_tabwidget, "Global Attribute")

        self.groupbox_layout.addWidget(self.button)
        self.groupbox_layout.addWidget(self.tabwidget)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.vuecatalogsettings_layout.addWidget(self.groupbox)
    
    
    def connect_signals(self):
        
        self.button.clicked.connect(self.controleurcatalogsettings.fill_catalog)
        
        self.dimension_tabwidget.add_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_name_add)
        self.dimension_tabwidget.add_value_dimension_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_value_add_confirm)
        self.dimension_tabwidget.add_value_dimension_cancel_button.clicked.connect(self.controleurcatalogsettings.dimension_value_add_cancel)
        self.dimension_tabwidget.add_value_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_value_add)
        
        self.dimension_tabwidget.modify_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_name_modify_confirm)
        self.dimension_tabwidget.modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.dimension_name_modify_cancel)
        self.dimension_tabwidget.modify_new_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_name_modify)
        self.dimension_tabwidget.modify_value_dimension_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_value_modify_confirm)
        self.dimension_tabwidget.modify_value_dimension_cancel_button.clicked.connect(self.controleurcatalogsettings.dimension_value_modify_cancel)
        self.dimension_tabwidget.modify_new_value_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_value_modify)
        
        self.dimension_tabwidget.delete_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_name_delete)
        self.dimension_tabwidget.delete_value_dimension_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.dimension_value_delete)
        
        self.variable_tabwidget.add_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_name_add_confirm)
        self.variable_tabwidget.add_name_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_name_add_cancel)
        self.variable_tabwidget.add_dimension_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_name_add)
        self.variable_tabwidget.add_attribute_variable_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_variable_add_confirm)
        self.variable_tabwidget.add_attribute_variable_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_variable_add_cancel)
        self.variable_tabwidget.add_attribute_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_add_confirm)
        self.variable_tabwidget.add_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_add_cancel)
        self.variable_tabwidget.add_attribute_value_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_add)
        
        self.variable_tabwidget.modify_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_name_modify_confirm)
        self.variable_tabwidget.modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_name_modify_cancel)
        self.variable_tabwidget.modify_new_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_new_name_modify_confirm)
        self.variable_tabwidget.modify_new_name_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_new_name_modify_cancel)
        self.variable_tabwidget.modify_dimension_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_name_modify)
        
        self.variable_tabwidget.modify_attribute_variable_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_variable_modify_confirm)
        self.variable_tabwidget.modify_attribute_variable_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_variable_modify_cancel)
        self.variable_tabwidget.modify_attribute_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_modify_confirm)
        self.variable_tabwidget.modify_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_modify_cancel)
        self.variable_tabwidget.modify_new_attribute_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_new_attribute_modify_confirm)
        self.variable_tabwidget.modify_new_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_new_attribute_modify_cancel)
        self.variable_tabwidget.modify_new_attribute_value_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_modify)
        
        self.variable_tabwidget.delete_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_name_delete)
        self.variable_tabwidget.delete_attribute_variable_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_delete_confirm)
        self.variable_tabwidget.delete_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.variable_attribute_delete_cancel)
        self.variable_tabwidget.delete_attribute_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.variable_attribute_delete)
        
        self.attribute_tabwidget.add_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_name_add)
        self.attribute_tabwidget.add_value_attribute_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_value_add_confirm)
        self.attribute_tabwidget.add_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_add_cancel)
        self.attribute_tabwidget.add_value_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_value_add)
        
        self.attribute_tabwidget.modify_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_name_modify_confirm)
        self.attribute_tabwidget.modify_name_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_name_modify_cancel)
        self.attribute_tabwidget.modify_new_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_name_modify)
        self.attribute_tabwidget.modify_value_attribute_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_value_modify_confirm)
        self.attribute_tabwidget.modify_value_attribute_cancel_button.clicked.connect(self.controleurcatalogsettings.global_attribute_value_modify_cancel)
        self.attribute_tabwidget.modify_new_value_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_value_modify)
        
        self.attribute_tabwidget.delete_name_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_name_delete)
        self.attribute_tabwidget.delete_value_attribute_combobox.lineEdit().returnPressed.connect(self.controleurcatalogsettings.global_attribute_value_delete)




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
