# Le "if" permet d'executer un code différent en fonction d'une condition.
print("Entrez un nombre entier.")
x = input()
if len(x) == 0:
    print("Il faut écrire quelque-chose...")
    exit()
x = int(x)

# Un if peut être suivi de n'importe quel nombre de "elif", puis d'un "else" optionnel.
if (x < 0):
    print("C'est négatif.")
elif (x == 0):
    print("Il n'y a rien.")
elif (x < 42):
    print("Ce n'est pas beaucoup.")
elif (x == 42):
    print("C'est la quantité parfaite!")
else:
    print("C'est beaucoup!")
