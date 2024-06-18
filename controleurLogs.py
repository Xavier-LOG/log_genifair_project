# Importation des bibliothèques




from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor




# Définition de la classe controleurLogs




class controleurLogs:
    
    
    # Constructeur par défaut
    
    
    def __init__(self, vuelogs):
        
        self.vuelogs = vuelogs
        self.logs = []
        
    # Définition des méthodes


    def add_log(self, log):
        
        """_summary_
        Réinitialisation du contenu de la zone de texte toutes les 10 lignes et ajout dans la liste
        """
        
        if len(self.logs) % 10 == 0:
            # Réinitialisation du contenu de la zone de texte toutes les 10 lignes
            self.vuelogs.groupbox_textarea.setPlainText("")
        # Ajout dans la liste
        self.logs.append(log)

    
    def add_colored_log(self, log, color):
        
        """_summary_
        Coloration
        """
        
        format = QTextCharFormat()
        if color == "red":
            format.setForeground(QColor("red"))
        elif color == "orange":
            format.setForeground(QColor("orange"))
        else:
            format.setForeground(QColor("green"))
        cursor = self.vuelogs.groupbox_textarea.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(log, format)
