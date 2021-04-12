# "while" permet d'executer le même code en boucle tant qu'une condition est respectée.
print("Boucle while")
n = 0
while (n < 5):
    print(n)
    n += 1

# "for" permet d'itérer sur un itérable (une collection) (liste, tuple...)
print("\nBoucle for")
users = ["Jean", "Lynn", "Franck"]
for name in users:
    print(name)

user = {
    "name": "Jean",
    "age": 33,
    "is_admin": False
}

for key in user:
    print(f"{key}: {user[key]}")

# Itérer avec la méthode "items" et le "tuple unpacking"
for key, value in user.items():
    print(f"{key}: {value}")

# La fonction "range", utile avec les boucles for.
# On doit lui donner une valeur d'arrêt, et optionnellement une valeur de début et un pas.
tableau = []
for n in range(3):
    tableau.append(n)
print(tableau)

tableau = []
for n in range(3, 10):
    tableau.append(n)
print(tableau)

tableau = []
for n in range(3, 10, 2):
    tableau.append(n)
print(tableau)

# break et continue
# break permet de sortir de la boucle en cours.
# continue va passer a la prochaine itération, terminant l'itération en cours.
tableau = []
n = 0
while (True):
    n += 1
    if n % 2 == 1:
        continue
    if n > 10:
        break
    tableau.append(n)
print(tableau)
