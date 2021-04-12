# On peut créer ses propres exceptions et les générer avec "raise".

try:
    print("Entrez un mot commencant par a.")
    mot = input()
    if mot[0] != "a":
        raise NameError("BadFirstLetter")
    print(f"Votre mot est {mot}!")
except NameError:
    print("Une exeption a été levée.")
