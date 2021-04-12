# Un point sur la mémoire: Références
# TODO
def add_3(n):
    n += 3

def add_4(t):
    t.append(4)

x = 6
add_3(x)
print(x)

tab = [1, 3]
add_4(tab)
print(tab)


array1 = [1, 2]
array2 = array1
array1.append(3)
print(array2)


# Les arguments par défaut sont interprétés a la lecture de la définition de la fonction.
# Les objets "cachés derrière une référence" seront donc toujours le même objet, d'un appel sur l'autre.
def accumulate(value, array=[]):
    array.append(value)
    return array

print(accumulate(1))
print(accumulate("lala"))

# Pour éviter ce comportement:
def dont_accumulate(value, array=None):
    if array == None:
        array = []
    array.append(value)
    return array

print(dont_accumulate(1))
print(dont_accumulate("lala"))
