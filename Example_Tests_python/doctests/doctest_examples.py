# Exemple 1

def ajouter(a=None, b=None):
    """ Additionne deux elements.

        Parameters:
            a : entier, flottant, liste ou str, default = None
                Premier élément à additionner
            b : entier, flottant, liste ou str, default = None
                Deuxième élément à additionner

        Returns: entier, flottant ou liste
            somme de a et b


        Exemple :

            >>> # on peut mettre des commentaires ici
            >>> ajouter(1, 2) # ou là
            3
            >>> ajouter(2., 2) # fonctionne sur tous les types de nombre
            4.0

        La fonction fonctionne en duck typing, et accepte donc tout objet
        qui possède la méthode magique __add__ :

            >>> ajouter('a', 'b')
            'ab'
            >>> ajouter([1], [2])
            [1, 2]
    """
    return a + b


def get(data, index, default=None):
    """ Implémente l'équivalent de dict.get() pour les indexables.

        Example :

            >>> simple_comme_bonjour = ('pomme', 'banane')
            >>> get(simple_comme_bonjour, 0)
            'pomme'
            >>> get(simple_comme_bonjour, 1000, 'Je laisse la main')
            'Je laisse la main'
    """
    try:
        return data[index]
    except IndexError:
        return default


#if __name__ == "__main__":
# Si on utilise python pour les doctests
# Soit on inclut ces lignes de codes
     #import doctest
     #doctest.testmod()
# Soit on fait tourner les doctests avec
