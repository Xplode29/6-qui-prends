import random

class Carte:
    def __init__(self, numero: int, valeur: int):
        self.numero = numero
        self.valeur = valeur

class Rangee:
    def __init__(self, premiere_carte):
        self.cartes = [premiere_carte]

class Jeu:
    def __init__(self, joueurs: list):
        self.joueurs = joueurs
        
        self.rangees = []
        self.pile = []
        self.a_placer = []
    
    def distribuer(self):
        # Créer la pile
        for i in range(1, 105):
            tdb = 1
            if i % 10 == 0: tdb = 3
            elif i % 5 == 0: tdb = 2
            if i % 11 == 0: tdb = 5
            if i == 55: tdb = 7
            self.pile.append(Carte(i, tdb))
        
        random.shuffle(self.pile)
        
        for joueur in self.joueurs:
            for i in range(10):
                index = random.randint(0, len(self.pile) - 1)
                joueur.cartes_main.append(self.pile[index])
                self.pile.pop(index)
            joueur.cartes_main = sorted(joueur.cartes_main, key=lambda carte: carte.numero)
        
        #print("Pile:", [str(carte.numero) + " / " + str(carte.valeur) for carte in self.pile])
        for i in range(4):
            self.rangees.append(Rangee(self.pile[0]))
            self.pile.pop(0)
        #print("Pile:", [str(carte.numero) + " / " + str(carte.valeur) for carte in self.pile])

    def verifCartes(self): # Trop long, a simplifier
        for carteP in self.pile:
            for joueur in self.joueurs:
                for carteJ in joueur.cartes_main:
                    if carteJ.numero == carteP.numero:
                        print("Il y a deux meme cartes de valeur", carteP.numero)
    
    def afficherCartes(self):
        print("----- Rangee: ")
        [print("Rangee" + ":", [str(carte.numero) + " / " + str(carte.valeur) for carte in rangee.cartes]) for rangee in self.rangees]
        print("----- Cartes a placer: ")
        [print(self.joueurs[couple[0]].pseudo + ":", str(couple[1].numero) + " / " + str(couple[1].valeur)) for couple in self.a_placer]
        print("----- Cartes en main: ")
        [print(joueur.pseudo + ":", [str(carte.numero) + " / " + str(carte.valeur) for carte in joueur.cartes_main]) for joueur in self.joueurs]

    def tour(self):
        self.a_placer = []
        # Chacun choisi une carte (random pour les autres joueurs)
        print("-----------------------------------------------")
        for j, joueur in enumerate(self.joueurs):
            print("\n----- Tour de", joueur.pseudo)
            
            print("----- Rangee: ")
            [print("Rangee" + ":", [str(carte.numero) + " / " + str(carte.valeur) for carte in rangee.cartes]) for rangee in self.rangees]
            print("----- Cartes en main: ")
            print(joueur.pseudo + ":", [str(carte.numero) + " / " + str(carte.valeur) for carte in joueur.cartes_main])
            
            carte_num = 0
            while carte_num not in [carte.numero for carte in joueur.cartes_main]: #la carte est bien presente
                carte_num = input("Numero de la carte a poser: ")
                if carte_num.isdigit():
                    carte_num = int(carte_num)
            for i in range(len(joueur.cartes_main)):
                if joueur.cartes_main[i].numero == carte_num:
                    self.a_placer.append((j, joueur.cartes_main[i]))
                    joueur.cartes_main.pop(i)
                    break
        self.a_placer = sorted(self.a_placer, key=lambda couple: couple[1].numero)
        
        # On place les cartes
        print("-----------------------------------------------")
        
        print("\n----- Cartes a placer: ")
        [print(self.joueurs[couple[0]].pseudo + ":", str(couple[1].numero) + " / " + str(couple[1].valeur)) for couple in self.a_placer]
        #self.afficherCartes()
        
        # On joue le jeu
        for couple in self.a_placer:
            rangeeToGo = None
            for rangee in self.rangees:
                if couple[1].numero > rangee.cartes[-1].numero:
                    if rangeeToGo == None or rangee.cartes[-1].numero > rangeeToGo.cartes[-1].numero:
                        rangeeToGo = rangee
            
            if rangeeToGo == None:
                print("\n----- Tour de", self.joueurs[couple[0]].pseudo)
                print("----- Rangee: ")
                [print("Rangee" + ":", [str(carte.numero) + " / " + str(carte.valeur) for carte in rangee.cartes]) for rangee in self.rangees]
                print(joueur.pseudo + ":", [str(carte.numero) + " / " + str(carte.valeur) for carte in joueur.cartes_main])
                print("Votre numero (" + str(couple[1].numero) + " / " + str(couple[1].valeur) + ") est plus petit que ceux sur les rangees")
                
                #selection de la rangee a prendre
                rangee_num = 0
                while rangee_num not in range(1, 5):
                    rangee_num = input("Numero de la rangee a prendre: ")
                    if rangee_num.isdigit():
                        rangee_num = int(rangee_num)
                
                #prends la rangee
                self.joueurs[couple[0]].cartes_main.extend(self.rangees[rangee_num - 1].cartes)
                self.rangees[rangee_num - 1].cartes = [couple[1]]
                self.joueurs[couple[0]].cartes_main = sorted(self.joueurs[couple[0]].cartes_main, key=lambda carte: carte.numero)
            else:
                #On verifie si 6 qui prends
                if len(rangeeToGo.cartes) >= 5:
                    #prends la rangee
                    self.joueurs[couple[0]].cartes_main.extend(rangeeToGo.cartes)
                    rangeeToGo.cartes = []
                    self.joueurs[couple[0]].cartes_main = sorted(self.joueurs[couple[0]].cartes_main, key=lambda carte: carte.numero)
                
                rangeeToGo.cartes.append(couple[1])
        
        #self.afficherCartes()
                
class Joueur:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.cartes_main = []

joueurs = [
    Joueur("Joueur 1"),
    Joueur("Joueur 2"),
    Joueur("Joueur 3")
]

jeu = Jeu(joueurs)
jeu.distribuer()
#jeu.afficherCartes()
jeu.verifCartes()

while True:
    jeu.tour()