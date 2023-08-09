'''

Fichier player: Classe 'player' constituant les principales fonctions relatives au vaisseau commandé
Créé par J.Lisée et H.Salmon

'''

from entities.projectile import Projectile

class Player():
    def __init__(self, x, y, w, h, life):
        self.x = x
        self.y = y #constante
        self.w = w #constante
        self.h = h #constante
        self.life = life

    def getCoords(self):
        return  self.x, self.y 
    
    def moveLeft(self, event):
        if self.x > 0:
            self.x -= 12

    def moveRight(self, event):
        if self.x < 1220:
            self.x += 12
    
    def playerWin(self, Lst): #si la liste des invaders est vide 
        if Lst == []:
            return True
    
    def playerLose(self):
        if self.life == 0:
            return True
