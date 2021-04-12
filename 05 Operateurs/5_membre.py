# "in" permet de vérifier si un élement est présent dans une séquence.
tableau = [3, 17, "lala"]
print(3 in tableau)
print(4 in tableau)
print("-" * 30)
print("lae" in "the lazy dog")

# Dans le cas d'un dictionnaire, "in" permet de vérifier la présence de clés,
# mais pas de valeurs.
dictionnaire = {
    "nametiu": "Jean",
    "age": 33,
    123: "Anne"
}
print(33 in dictionnaire)
print("age" in dictionnaire)
print(123 in dictionnaire)

print("name" in dictionnaire.keys())
if "name" in dictionnaire.keys():
    print(dictionnaire["name"])