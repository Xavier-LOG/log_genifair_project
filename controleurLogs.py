# Importation des bibliothèques




from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor




# Définition de la classe controleurLogs




class controleurLogs:
    
    
    # Constructeur par défaut
    
    
    def __init__(self, vueLogs):
        
        self.vueLogs = vueLogs
        self.logs = []
    
    
    # Définition des méthodes


    def log(self, message):
        
        if len(self.logs) % 10 == 0:
            self.vueLogs.groupbox_textarea.setPlainText("")
        self.logs.append(message)

    
    def addColoredText(self, text, color):
        
        format = QTextCharFormat()
        if color == "red":
            format.setForeground(QColor("red"))
        elif color == "orange":
            format.setForeground(QColor("orange"))
        else:
            format.setForeground(QColor("green"))

        cursor = self.vueLogs.groupbox_textarea.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(text, format)
