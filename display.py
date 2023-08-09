'''

Fichier display: Classe 'Window' constituant la gestion graphique du jeu
Créé par J.Lisée et H.Salmon

'''

from tkinter import Canvas ,Tk ,Button ,Label


class Window(): #Classe gérant l'interface graphique

    def __init__(self, w, h): #Initialisation de l'interface graphique avec le module tkinter
        self.mainWindow = Tk()
        self.mainWindow.title('Tavern Invaders')
        self.mainWindow.geometry(f"{w}x{h}")
        self.Canvas = Canvas(self.mainWindow, width = 1280, height = 720, background = "#000144")

    
    def mainMenu(self): #Fenêtre du menu principal
        newgame = Button(self.mainWindow ,text = "New Game" ,command = self.newGame)
        quit = Button(self.mainWindow ,text = "Quit" ,command = self.mainWindow.destroy)
        lives = Label(self.mainWindow ,text = "remaining lives : " + str(self.lives))     #n'est pas dynamique avec le nombre de vies
        self.title = self.Canvas.create_text(640,360, fill = '#FF822C' ,text = 'Tavern Invaders' ,font = ("arial", 30))

        quit.pack(side = 'top' , padx = 0 , pady = 0)
        newgame.pack(side = 'top' , padx = 0 , pady = 0)
        lives.pack(side = 'top' ,padx = 0 ,pady = 0)
        self.Canvas.pack(padx = 5,pady = 5)
    
    def winMenu(self): #Fonction qui affiche le menu de victoire
        replay = Button(self.mainWindow, text="Replay ?", command=self.replay)
        self.winText = self.Canvas.create_text(640,360, fill = '#FF822C' ,text = 'Well played !' ,font = ("arial", 30))

        replay.pack(side = 'bottom', padx = 0, pady = 0)
        self.Canvas.pack(padx = 5, pady = 5)

    def loseMenu(self): #fonction qui affiche le menu de défaite
        replay = Button(self.mainWindow, text="Replay ?", command=self.replay)
        self.winText = self.Canvas.create_text(640,360, fill = '#FF822C' ,text = 'Better luck next time :(' ,font = ("arial", 30))

        replay.pack(side = 'bottom', padx = 0, pady = 0)
        self.Canvas.pack(padx = 5, pady = 5)
    

    def playerDisplay(self, x, y, w, h): #Fonction qui gère l'affichage du joueur
        self.playerSprite = self.Canvas.create_rectangle(x, y, x + w, y + h, outline = "#ff0000", fill = "#ff0000")
        return self.playerSprite

    def invaderDisplay(self, x, y, w, h): #Affichage d'un alien sur le Canvas
        self.invaderSprite = self.Canvas.create_rectangle(x, y, x + w, y + h, outline = "#fb0", fill = "#fb0")
        return self.invaderSprite

    def projectileDisplay(self, x, y, w, h): #Fonction qui affiche le projectile
        self.projectileSprite = self.Canvas.create_rectangle(x, y, x + w, y + h, outline = "#fb0", fill = "#fb0")
        return self.projectileSprite 

    def functionLink(self, newGame,replay): #Méthode qui fait le lien entre le jeu et l'interface graphique
        self.newGame = newGame
        self.replay = replay
    
    def attributeLink(self,lives):
        self.lives = lives
