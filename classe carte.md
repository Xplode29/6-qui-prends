``` {.python}
>>> from exercice import *
```

Exercice
========

Le jeu est composé de 104 cartes numérotées de 1 à 104. Chaque porte
également un certain nombre de têtes de bœuf. Ce nombre dépend de la
valeur de la carte et son mode de calcul sera développé ultérieurement.

,-------------------------------------------------------------------------.
| Carte                                                                   |
|-------------------------------------------------------------------------|
| + int numero : le numéro de la carte                                    |
| + int penalites : le nombre de têtes de bœuf.                           |
|                                                                         |
| + __init__(self, n) : le constructeur de la classe                      |
| + get_numero(self) :  renvoie le numero de la carte                     |
| + get_nombre_tdb(self): renvoie le nombre de têtes de bœuf              |
|                         que la carte contient.                          |
|+ __str__() : renvoie le numéro de la carte au format au format string.  |
|+ __repr__() : renvoie une chaine de caractère avec la numéro de la carte|
|               et les nombres de pénalités que cela représente.          |
|              Par exemple, « Carte 1 - 1 TdB ».                          |
|+ __lt__(self, autre) : implémente la comparaison < de 2 cartes.         |
|+ __gt__(self, autre) : implémente la comparaison > de 2 cartes.         |
|- __get_penalites(self) : méthode privée qui calcule le nombre de        |
|                        têtes de bœufs de la carte. Cette méthode        |
|                       sera appelée une seule fois à la création         |
|                       de la carte par la fonction __init__().           |
`-------------------------------------------------------------------------'

Les valeurs de la cartes
------------------------

Le jeu est composé de 104 cartes numérotées de 1 à 104. Le numéro est
passé en argument de la méthode `__init__()`. Les valeurs en dehors de
cet intervalle doivent provoquer une `AssertionError`.

``` {.python}
>>> cartes = [0]
>>> for i in range(1, 105):
...    m = Carte(i)
...    cartes.append(m)
...    assert m.numero == i
```

``` {.python}
>>> m0 = Carte(0)
Traceback (most recent call last):
...
AssertionError

>>> m1 = Carte(105)
Traceback (most recent call last):
...
AssertionError

>>> m3 = Carte(100.0)
Traceback (most recent call last):
...
AssertionError
```

L'accès au numéro
-----------------

``` {.python}
>>> m4 = Carte(32)
>>> m4.get_numero()
32
>>> m4 = Carte(55)
>>> m4.get_numero()
55
```

Les pénalités des cartes
------------------------

``` {.python}
>>> cartes_pas_simples = []
```

Les cartes : - en 5 (5, 15, 25, etc.) ont 2 têtes de boeuf,

``` {.python}
    >>> for i in range(5, 105, 10):
    ...     if i != 55:
    ...         assert cartes[i].get_nombre_tdb() == 2
    ...         cartes_pas_simples.append(i)
```

-   en 0 (10, 20, 30, etc.) 3 têtes,

``` {.python}
    >>> for i in range(10, 105, 10):
    ...     if i != 55:
    ...         assert cartes[i].get_nombre_tdb() == 3
    ...         cartes_pas_simples.append(i)
```

-   avec un doublet (11, 22, 33, etc.) 5 têtes

``` {.python}
    >>> for i in range(11, 105, 11):
    ...     cartes_pas_simples.append(i)
    ...     if i == 55:
    ...         assert cartes[i].get_nombre_tdb() == 7
    ...     else:
    ...         assert cartes[i].get_nombre_tdb() == 5
```

Le nombre "55" est à la fois un doublet et un nombre en 5, c'est
pourquoi cette carte compte 7 têtes de boeuf.

Toutes les autres cartes ont 1 seule tête de bœufs.

``` {.python}
    >>> for i in range(1, 105):
    ...     if not i in cartes_pas_simples:
    ...         assert cartes[i].get_nombre_tdb() == 1
```

Les comparaisons
----------------

On doit pouvoir comparer les cartes entre elles.

``` {.python}
>>> m10 = Carte(16)
>>> m20 = Carte(13)
>>> m30 = Carte(100)
```

``` {.python}
>>> m10 < m20
False
>>> m30 < m20
False
>>> m10 < m30
True
```

``` {.python}
>>> m10 > m20
True
>>> m30 > m20
True
>>> m10 > m30
False
```
