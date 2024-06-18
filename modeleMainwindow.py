# Définition de la classe modeleMainwindow




class modeleMainwindow:
    
    
    # Constructeur par défaut
    
    
    def __init__(self):
        
        self.screen_width = 0
        self.screen_height = 0
    
    
    # Définition des méthodes


    def set_screen_resolution(self, width, height):
        
        """_summary_
        Gestion de la résolution de l'écran
        """
        
        if width <= self.screen_width:
            self.screen_width = width
        if height <= self.screen_height:
            self.screen_height = height
