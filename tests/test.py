# Importation des fichiers



from outilsArrangement import outilsArrangement
from outilsProcessing import outilsProcessing




# Importation des bibliothèques




import unittest
import os
import pandas as pd
import xarray as xr




# Définition de la classe test




class test(unittest.TestCase):
    
    def test(self):
        
        catalog = outilsArrangement.read_json(os.path.normpath(os.path.abspath("test_catalog.json")).replace('\\', '/'))
        dataframe = pd.read_excel(os.path.normpath(os.path.abspath("test.xlsx")).replace('\\', '/'))
        xarray_dataset = outilsProcessing(None, dataframe, xr.Dataset(), os.path.normpath(os.path.abspath("test_catalog.json")).replace('\\', '/'))
        
        self.assertTrue(outilsArrangement.read_json(os.path.normpath(os.path.abspath("test_catalog.json")).replace('\\', '/')))
        self.assertTrue(outilsArrangement.dimension_name_add(catalog, "Dimension_add"))
        self.assertTrue(outilsArrangement.dimension_value_add(catalog, "dimension_add", "100, 200"))
        self.assertTrue(outilsArrangement.dimension_value_modify(catalog, "dimension_add", "200, 300", 2))
        self.assertTrue(outilsArrangement.dimension_value_delete(catalog, "dimension_add"))
        self.assertTrue(outilsArrangement.dimension_name_modify(catalog, "Dimension_add", "Dimension_modify"))
        self.assertTrue(outilsArrangement.variable_name_add(catalog, "variable_add", ["Dimension_modify"], ["date", "time"]))
        self.assertTrue(outilsArrangement.variable_name_modify(catalog, "variable_add", "variable_modify", ["Dimension_modify"]))
        self.assertTrue(outilsArrangement.variable_attribute_add(catalog, "variable_modify", "attribute_add", "value_add"))
        self.assertTrue(outilsArrangement.variable_attribute_modify(catalog, "variable_modify", "attribute_add", "attribute_modify", "value_modify"))
        self.assertTrue(outilsArrangement.variable_attribute_delete(catalog, "variable_modify", "attribute_modify"))
        self.assertTrue(outilsArrangement.fill_catalog(catalog, "Dimension_modify", dataframe, ["date", "time"]))
        self.assertTrue(outilsArrangement.dimension_name_delete(catalog, "Dimension_modify", ["dimension_modify", "variable_modify"]))
        self.assertTrue(outilsArrangement.global_attribute_name_add(catalog, "comment"))
        self.assertTrue(outilsArrangement.global_attribute_value_add(catalog, "comment", "test"))
        self.assertTrue(outilsArrangement.global_attribute_value_modify(catalog, "comment", "new"))
        self.assertTrue(outilsArrangement.global_attribute_value_delete(catalog, "comment"))
        self.assertTrue(outilsArrangement.global_attribute_name_modify(catalog, "comment", "comment_bis"))
        self.assertTrue(outilsArrangement.global_attribute_name_delete(catalog, "comment_bis"))
        
        self.assertTrue(xarray_dataset.create_xarray_dataset())




# Programme principal




if __name__ == '__main__':
    
    unittest.main()
