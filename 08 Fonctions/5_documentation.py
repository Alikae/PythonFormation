# Docstring
print("\n---Docstrings:")
# Les premières lignes d'une fonction peuvent être une string littérale, ici appelée une docstring,
# qui peut ensuite être parsée et formatée par des outils externes pour générer automatiquement de la documentation.
# Les docstrings sont conventionnellement formatées comme tel: La première ligne explicite de facon courte ce que fait la fonction.
# Si une description plus complète est nécéssaire, on la séparera de la première ligne par une ligne vide.
def add_1(n):
    """ Add one to the argument and return it.

    Doesn't do anything else.
    """
    return n + 1

print(add_1.__doc__)
#print(dir.__doc__)
print(list.append.__doc__)


# Annotations
print("\n---Annotations:")
# On peut spécifier le type attendu pour les arguments d'une fonction, ainsi que le type renvoyé, en suivant cette syntaxe:
def mult_to_string(a: int, b: int)-> str:
    return str(a * b)
# Cela n'empêche pas l'utilisateur de la fonction de rentrer n'importe quel type en argument!
# On peut accéder a ces informations en utilisant __annotations__.
print(mult_to_string.__annotations__)
