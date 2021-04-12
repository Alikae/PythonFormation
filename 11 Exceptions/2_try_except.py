# On peut utiliser la syntaxe "try/except" pour gérer certaines exceptions.
# Si une exception est rencontrée dans un bloc try, le bloc courant va stopper son exécution et on va directement passer dans le except correspondant.
# Si aucun except ne gère l'exception rencontrée, le programme va s'arrêter avec une erreur.

array = [1, 2, 3]
#array[6] = 4

def bad_function():
#    bad_file = open("inexistant")
#    1e10**1e20
#    array[6] = 4
    pass

try:
    bad_function()
except IndexError as error:
    print(f"oups. [{error}] has been encountered.")
except FileNotFoundError:
    print("Ce fichier n'existe pas!")

print("Le programme peut se terminer.")

# Une clause except sans nom d'exception va "attraper" toutes les exceptions.
# C'est une mauvaise pratique, car cela peut masquer de véritables erreurs de logique dans le code.
#except:

# TODO
# Il existe aussi finally
