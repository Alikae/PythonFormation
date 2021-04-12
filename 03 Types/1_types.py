# Python a ce qu'on appelle un typage "faible".
# Cela signifie que le type d'une variable peut changer au cours de l'execution.
var = 3
print(var)
var = "lala"
print(var)

# Variables textuelles
name = "lulu"
third_char = name[2]
print(f"name: {name}")
print(f"third char: {third_char}")

# Variables numériques
points = 3
ratio = 0.1
ratio = 10 / 5
complex_number = 3 + 2j
print(f"points: {points}")
print(f"ratio: {ratio}")
print(f"complex_number: {complex_number}")

# Variables booléennes
is_adult = True
is_greater_than_five = points > 5
print(is_adult)
print(is_greater_than_five)

print(type(is_adult))
print(type(ratio))
