# Les slices sont un moyen de séléctionner un sous-set d'un itérable (collection).
# Elles sont très utiles pour manipuler les chaînes de caractère.

s = "0123456789"
print(f"s: {s}")

# Accès classique:
print(f"s[1]: {s[1]}")

# La slice: [debut:fin:pas]
# La fin est non-incluse.

# Copie de liste:
print(f"s[:]: {s[:]}")

# Slice depuis le 2ème element :
print(f"s[1:]: {s[1:]}")

# Slice jusqu'au deuxieme element non inclus:
print(f"s[:2]: {s[:2]}")

# Du 2eme au 4eme caractère:
print(f"s[1:4]: {s[1:4]}")

# Avec un pas de 2:
print(f"s[::2]: {s[::2]}")

# Tout a la fois:
print(f"s[1:4:2]: {s[1:4:2]}")

# Avec un pas négatif:
print(f"s[::-1]: {s[::-1]}")

print(f"{(1, 2, 3, 4)[1::2]}")
