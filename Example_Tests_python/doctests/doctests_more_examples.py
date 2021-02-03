#Fichier de scripts avec des exemples additionnels de doctests

def greet(msg):
    """
    Début de la doctest

    Attention au formattage
    Exemples:
        # Échoue
        >>> greet("Coucou c'est moi") # doctest: +SKIP
        "Coucou c'est moi"

        # Échoue
        >>> greet("Coucou c'est encore moi!!!") # doctest: +SKIP
        'Coucou c'est moi'

        # Réussi
        >>> greet("Coucou")
        Coucou

    """

    print(msg)


#Gérer les valeurs non prédictables
class MyClass:
    pass

def unpredictable_failed(obj):
    """Returns a new list containing obj.

    >>> unpredictable_failed(MyClass()) # doctest: +SKIP
    [<doctests_more_examples.MyClass object at 0x7f13af17bf60>]
    """
    return [obj]

def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctests_more_examples.MyClass object at 0x...>]
    """
    return [obj]

# Remarque: ce genre de questions ne se posent plus à partir de Python 3.7
# Voir: https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6

# Exemple: gérer les erreurs

# Doctest avec du code inutile!!

def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    File "/home/stoll/anaconda3/lib/python3.7/runpy.py", line 193, in _run_module_as_main
        "__main__", mod_spec)
    File "/home/stoll/anaconda3/lib/python3.7/runpy.py", line 85, in _run_code
        exec(code, run_globals)
    File "/home/stoll/anaconda3/lib/python3.7/doctest.py", line 2794, in <module>
        sys.exit(_test())
    File "/home/stoll/anaconda3/lib/python3.7/doctest.py", line 2782, in _test
        m = __import__(filename[:-3])
    File "doctests/doctests_more_examples.py", line 104, in <module>
        this_raises()
    File "doctests/doctests_more_examples.py", line 102, in this_raises
        raise RuntimeError('here is the error')
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')

# Invocation de la fonction
# this_raises()

# Solution
# Doctest ignore tout ce qu'il y a entre "Traceback (most recent call last)" et l'erreur soulevée

def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')


# Exemple: gérer les espaces blancs

# Cette doctest échoue....
def double_space_failed(lines):
    """Prints a list of lines double-spaced.

    >>> double_space_failed(['Line one.', 'Line two.']) # doctest: +SKIP
    Line one.

    Line two.

    """
    for l in lines:
        print(l)
        print()
    return

# Solution: ajouter <BLANKLINE>
def double_space(lines):
    """Prints a list of lines double-spaced.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    """
    for l in lines:
        print(l)
        print()
    return

# FACULTATIF

# Exemple: gérer les dictionnaires
# # L'ordre d'affichage dans la console des élément d'un dictionnaire n'est pas garantit

# keys = [ 'a', 'aa', 'aaa' ]

# d1 = dict( (k,len(k)) for k in keys )
# d2 = dict( (k,len(k)) for k in reversed(keys) )

# print()
# print('d1:', d1)
# print('d2:', d2)
# print('d1 == d2:', d1 == d2)

# s1 = set(keys)
# s2 = set(reversed(keys))

# print()
# print('s1:', s1)
# print('s2:', s2)
# print('s1 == s2:', s1 == s2)

# # Doctest
# La doctest doit être reproductible et ne pas dépendre de l'ordre d'affichage des éléments du dict
# def group_by_length(words):
#     """Returns a dictionary grouping words into sets by length.

#     >>> grouped = group_by_length([ 'python', 'module', 'of', 'the', 'week' ])
#     >>> grouped == { 2:set(['of']),
#     ...              3:set(['the']),
#     ...              4:set(['week']),
#     ...              6:set(['python', 'module']),
#     ...              }
#     True

#     """
#     d = {}
#     for word in words:
#         s = d.setdefault(len(word), set())
#         s.add(word)
#     return d