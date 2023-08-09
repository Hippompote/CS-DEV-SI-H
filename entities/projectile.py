'''

Fichier Projectile: Classe 'Projectile' constituant les principales fonctions du jeu et sa gestion
Créé par J.Lisée et H.Salmon

'''

class Projectile():
    def __init__(self, x, y, w, h, origine = False):
        self.x = x
        self.y = y
        self.w = w #constante
        self.h = h #constante
        self.origine = origine #false pour provenance ennemi, true pour provenance player 

    
    def getCoords(self): #retourne les coordonnées du projectile
        return  self.x, self.y 

        
