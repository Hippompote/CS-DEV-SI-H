'''

Fichier Game: Classe 'Game' constituant les principales fonctions du jeu et sa gestion
Créé par J.Lisée et H.Salmon

'''


from random import randint
from display import Window
from entities.invader import Invader
from entities.player import Player
from entities.projectile import Projectile
from random import randint

class Game(Window): #Classe Jeu héritée de la classe Fenêtre (gestion de l'interface)
    
    def GameLaunch(self): #Fonction Initialisant le jeu

        #en entrée : vide
        #en sortie : vide 

        self.lives = 3
        Window.attributeLink(Game,self.lives)
        Window.functionLink(Game,self.startGame,self.replay)
        self.mainMenu()
        self.mainWindow.mainloop()
    

    def startGame(self): #Fonction qui met en place le lancement d'une partie et gère la boucle principale

        #en entrée : vide
        #en sortie : vide 

        self.Canvas.delete('all')
        self.level = 0
        self.score = 0
        self.lstPlayer = []
        self.lstShot =[]
        self.lstInvaderShot = []
        self.gameLoop(3, 0)


    def gameLoop(self, life, level): #Boucle principale du jeu

        #en entrée : le nombre de vies restantes, le niveau de difficulté (pas implémenté)
        # en sortie : vide

        self.level = level
        self.life = life
        self.spawnInvaders()
        self.invaderBehavior()
        self.spawnPlayer()
        self.keybindPlayer()
        self.playerMove()
        self.playerDestroyOrWin()



#------------------Gestion des Aliens-------------------------

    def spawnInvaders(self): #Fonction qui gère l'apparition des ennemis

        #en entrée : vide
        #en sortie : la liste des invaders

        self.lstInv = []
        for i in range(10):
            Inv = Invader(i*100, 50,50)
            Disp = self.invaderDisplay(Inv.x,Invader.y, Inv.w,Inv.h)
            self.lstInv.append([Inv, Disp])
        return self.lstInv


    def invaderShoot(self): #fonction de la boucle behavior qui fait tirer un invader aléatoire

        #en entrée : vide
        #en sortie : vide 

        randInvader = randint(0, len(self.lstInv) - 1)
        x, y = self.lstInv[randInvader][0].getCoords()
        x += self.lstInv[randInvader][0].w / 2 #centre le tir
        y += 10
        shot = Projectile(x, y, 3, 10)
        invShotDisp = self.projectileDisplay(shot.x, shot.y, shot.w, shot.h)
        self.lstInvaderShot.append([shot, invShotDisp])
        self.projectileMove(self.lstInvaderShot, 3)
        return


    def invaderBehavior(self): #Comportement des ennemis et leur affichage

        #en entrée : vide
        #en sortie : vide 

        if Invader.speed > 0:
            for Inv,Disp in reversed(self.lstInv): #on parcourt la liste dans le sens inverse si la vitesse est positive
                Inv.invaderMove(1280)
                self.Canvas.coords(Disp, Inv.x, Invader.y, Inv.x + Inv.w, Invader.y + Inv.h)
        else:
            for Inv,Disp in self.lstInv:
                Inv.invaderMove(1280)
                self.Canvas.coords(Disp, Inv.x, Invader.y, Inv.x + Inv.w, Invader.y + Inv.h)
        if randint(0,20) == 1 :     #à chaque tic de mouvement, il y a une chance sur 30 qu'un alien aleatoire tir (le nombre 30 est subjectif à la difficulté)
            self.invaderShoot()
        self.invaderDestroy()
        self.Canvas.after(100, self.invaderBehavior)

    
    def invaderDestroy(self): #Fonction qui gère la destruction des aliens

        #en entrée : vide
        #en sortie : vide

        for Inv, Disp in self.lstInv:
            if self.shotCollision(self.lstShot, Inv) == True:
                self.Canvas.delete(Disp)
                self.lstInv.remove([Inv, Disp])
                self.score += 100


#-------------------------------Gestion du vaisseau-------------------------------------


    def spawnPlayer(self): #Fonction qui gère l'apparition du joueur

        #en entrée : vide
        #en sortie : l'objet de classe player contrôlé par le joueur

        self.player = Player(600, 600, 50, 50, self.life)
        self.playerDisp = self.playerDisplay(self.player.x, self.player.y, self.player.w, self.player.h)
        self.lstPlayer.append([self.player, self.playerDisp])
        return self.player

    
    def playerMove(self): #Fonction qui gère le déplacement du joueur

        #en entrée : vide
        #en sortie : vide

        self.Canvas.coords(self.playerSprite, self.player.x, self.player.y, self.player.x + self.player.w, self.player.y + self.player.h)
        self.Canvas.after(5, self.playerMove)


    def playerDestroyOrWin(self): #gère les conditions de destruction du joueur par contact avec un invader ou un projectile (ne marche pas bien) et vérifie si il a gagné

        #en entrée : vide
        #en sortie : vide

        if  self.shotCollision(self.lstInvaderShot, self.player) == True or self.lstInv[0][0].y >= self.player.y: #vérifie si le joueur est touché par un projectile invader ou si un invader se retrouve sur sa rangée
            self.player.life -= 1
            self.Canvas.delete(self.playerSprite)   
            self.lstPlayer.remove([self.player, self.playerDisp])
            print(self.player.life)
            if self.player.playerLose():
                self.loseDisplay()          #vérifie si le joueur a perdu (ne marche pas)
        elif self.player.playerWin(self.lstInv):   #vérifie si tous les ennemis sont morts et donc que le joueur a gagné (ne marche pas)
            self.winDisplay()
        self.Canvas.after(5, self.playerDestroyOrWin)

#----------------------------Gestion des projectiles--------------------------

    def projectileMove(self, shotList, speed): #Fonction qui gère le mouvement des projectiles

        #en entrée : liste des projectiles, vitesse des projectiles 
        #en sortie : vide

        for shot, shotDisp in shotList:
            shot.y += speed
            self.Canvas.coords(shotDisp, shot.x, shot.y, shot.x + shot.w, shot.y + shot.h)
            if shot.y > 0 and shot.y < 1280:
                self.Canvas.after(5, lambda:self.projectileMove(shotList, speed))
            else :
                self.Canvas.delete(shotDisp)
                shotList.remove([shot, shotDisp])


    def shootStart(self, event): #initialise le tir du joueur

        #en entrée : condition d'activation "event" due à un keypress
        #en sortie : la liste des projectiles
        
        x, y = self.player.getCoords() #recupere les coordonnées du joueur pour définir le départ du tir
        x += self.player.w / 2 #centre le tir 
        y -= 10 #spawn le tir hors du player
        shot = Projectile(x ,y ,3, 10)
        shotDisp = self.projectileDisplay(shot.x, shot.y, shot.w, shot.h)
        self.lstShot.append([shot, shotDisp])
        self.projectileMove(self.lstShot, -3) #lance une fonction qui boucle l'avancée du tir
        return self.lstShot

#-------------------------------Autres---------------------------------------------

    def shotCollision(self, shotList, Entity): #Fonction qui renvoie True si un projectile entre en contact avec le vasseau ou un alien

        #en entrée : la liste des projectiles, un objet qui subit un contact avec un projectile
        #en sortie : la condition collision True ou False

        Collision = False
        for shot, shotDisp in shotList:
            if shot.x in range(Entity.x, Entity.x + Entity.w) and shot.y in range(Entity.y, Entity.y + Entity.h):
                Collision = True
        return Collision
        

    def keybindPlayer(self): #Fonction qui gère la liaison entre les touches du clavier et le déplacement du vaisseau

        #en entrée : vide
        #en sortie : vide

        self.mainWindow.bind('<Left>', self.player.moveLeft)
        self.mainWindow.bind('<Right>', self.player.moveRight)
        self.mainWindow.bind('<space>', self.shootStart)

    def winDisplay(self): #affichage du menu de victoire (ne marche pas)
        self.Canvas.delete('All')
        self.winMenu()
    
    def loseDisplay(self): #affichage du menu défaite (ne marche pas)
        self.Canvas.delete('All')
        self.loseMenu()

    def replay(self): #Gestion du bouton "replay" en cas de victoire
        self.level += 1
        self.gameLoop(self.life, self.level)

Jeu = Game(1280, 720)
Jeu.GameLaunch()