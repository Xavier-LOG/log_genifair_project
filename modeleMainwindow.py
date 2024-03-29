# Définition de la classe modeleErrorLogs




class modeleMainwindow:
    
    
    logs: list = []
    screen_width: int = 0
    screen_height: int = 0
    
    
    # Définition des méthodes statiques
    
    
    @staticmethod
    def log(message):
        
        modeleMainwindow.logs.append(message)


    @staticmethod
    def set_screen_resolution(width: int, height: int):
        if width <= modeleMainwindow.screen_width:
            modeleMainwindow.screen_width = width
        if height <= modeleMainwindow.screen_height:
            modeleMainwindow.screen_height = height
