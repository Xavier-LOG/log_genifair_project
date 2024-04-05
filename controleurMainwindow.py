# Définition de la classe controleurMainwindow




class controleurMainwindow:
    
    
    # Constructeur par défaut
    
    
    def __init__(self, vueMainwindow):
        
        self.vueMainwindow = vueMainwindow
    
    
    # Définition des méthodes
    
    
    def load_logs(self, logs):
        
        self.vueMainwindow.mainwindow_logs_textarea.setPlainText("")
        for log in logs:
            self.vueMainwindow.mainwindow_logs_textarea.appendPlainText(str(log))
