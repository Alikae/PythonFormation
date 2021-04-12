# La fonction dir sans argument permet de lister des noms dans l'espace de nommage local.
print(dir())

# En lui donnant un objet en argument, elle permet de lister des informations sur lui.
ages = [33, 35, 22, 17]

def func():
    pass

print(dir(ages))
ages.append(42)
