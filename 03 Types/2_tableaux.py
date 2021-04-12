# Un tableau est une collection d'objets ordonnée.
users = ["Jo", "Phil", "Kate"]
users.append("Lynn")
print(users)
print(type(users))
# Comme les "tableaux" sont des listes, on peut y stocker différents types au sein du même tableau.
users.append(33)
print(users)

print(users[4])
