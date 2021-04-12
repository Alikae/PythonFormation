# LISTES
# Les listes sont ordonnées et modifiables.
print("LISTS:")
my_list = [3, 44, "Jean"]
print(my_list)
my_list[1] = "George"
print(my_list)

# TUPLES
# Les tuples ressemblent aux listes, mais sont immuables.
# On ne peut ni modifier les elements existants, ni en ajouter de nouveaux.
# Les tuples sont utiles par exemple en retour de fonctions.
print("\nTuples:")
my_tuple = (3, 44, "Jean")
print(my_tuple)

def get_user():
    return ("Jean", 33, True)

user = get_user()

print(user)
print(f"L'utilisateur s'appelle {user[0]}")
# On peut également utiliser le "tuple unpacking":
name, age, isAdmin = get_user()
print(f"Son age est {age}")

# SETS
# Les Sets sont non-ordonnés et ne peuvent contenir de doublons.
print("\nSets:")
my_set = {1, 33, "lala", 33.0, 17, "17"}
print(my_set)
print("les elements de mon set sont:")
for element in my_set:
    print(f"{element} ({type(element)})")

tab = [3, 17, 3, 2]
print(tab)
tab = set(tab)
tab = list(tab)
tab = list(set(tab))
print(tab)

# Dictionnaires
# Les Dictionnaires permettent de stocker des paires "clé-valeur".
print("\nDictionnaires:")
user = {
    "name": "Lynn",
    "age": 33,
    "is_admin": True,
    33: "you can do this"
}
print(f"{user['name']} est admin: {user['is_admin']}")
user["is_admin"] = False
print(f"{user['name']} est admin: {user['is_admin']}")
user['new_key'] = 10
print(user)
