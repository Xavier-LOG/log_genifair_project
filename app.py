# Importation des fichiers




from vueMainwindow import vueMainwindow




# Importation des bibliothèques




import sys
from PyQt6.QtWidgets import QApplication




# Programme principal




if __name__ == "__main__":
    
    # Initialisation de l'application
    app = QApplication(sys.argv)
    vuemainwindow = vueMainwindow()
    vuemainwindow.show()
    # Lancement
    sys.exit(app.exec())
