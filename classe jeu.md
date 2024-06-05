    >>> from exercice import *


Exercice
========

La classe Jeu contient un jeu de cartes complet. Les cartes sont
mélangées. On pourra utiliser la fonction `shuffle()` du module
`random`.

,------------------------------------------------------------------.
|Jeu                                                               |
|------------------------------------------------------------------|
|+ cartes : la liste mélangée d'objets de type Carte.              |
|                                                                  |
|+ __init__(self) : le constructeur de la classe.                  |
|+ piocher(self) : qui renvoie la carte sur le haut de la pile.    |
|                Si la pile est vide, une AssertionError est levée.|
|+__len(self)__: renvoie le nombre de cartes restant dans le jeu,  |
|               c'est-à-dire le nombre de cartes de la pioche.     |
`------------------------------------------------------------------'


1.  On vérifie que le jeu contient le bon nombre de cartes.


    >>> j = Jeu()
    >>> len(j.cartes)
    104


2.  On vérifie que le jeu ne contient que des cartes.


    >>> def contient_cartes(l):
    ...     for c in l.cartes:
    ...         if not isinstance(c, Carte):
    ...             return False
    ...     return True
    >>> contient_cartes(j)
    True


3.  On vérifie que le jeu est mélangé.


    >>> def est_trie(l):
    ...     for i in range(len(l.cartes)-1):
    ...         if l.cartes[i] > l.cartes[i-1]:
    ...             return False
    ...     return True
    >>> est_trie(j)
    False


4.  En implémentant la méthode `__len(self)__`, on peut écrire
    simplement `len(j)` au lieu de `len(j.cartes)`.


    >>> len(j)
    104


5.  On vérifie que, si on pioche une carte, le nombre de cartes diminue
    de 1 et que l'on obtient bien une carte.


    >>> c1 = j.piocher()
    >>> len(j)
    103
    >>> isinstance(c1, Carte)
    True
    >>> c2 = j.piocher()
    >>> c3 = j.piocher()
    >>> len(j)
    101
    >>> isinstance(c3, Carte)
    True

