# Importation des fichiers




from vueMainwindow import vueMainwindow




# Importation des bibliothèques




import sys
from PyQt6.QtWidgets import QApplication




# Programme principal




if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    vuemainwindow = vueMainwindow()
    vuemainwindow.show()
    sys.exit(app.exec())
