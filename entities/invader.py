'''

Fichier Invader: Classe 'Invader' constituant les principales fonctions relatives aux aliens.
Créé par J.Lisée et H.Salmon

'''

class Invader(): #Classe groupant les attibuts et méthodes de base d'un ennemi

    speed = 10 #Variable statique de la vitesse
    y = 50
    def __init__(self, x, w, h):
        self.x = x
        self.w = w 
        self.h = h
        

    def getCoords(self): #Méthode pour récuperer les coordonnées
        return  self.x, self.y

    def invaderMove(self,w): #Méthode gérant le changement de coordonnées d'un ennemi

        #entrée: w la largeur de la fenêtre

        if self.x + Invader.speed < 0 or self.x + self.w + Invader.speed > w:
            Invader.speed = -Invader.speed
            Invader.y += 50
        self.x += Invader.speed
    

