import math

# Lambdas
# Une lambda est une fonction définie "on the fly".
inverse_sqrt = lambda x: 1 / math.sqrt(x)
print(inverse_sqrt(3))
# Lambda a 2 arguments:
lambda x, y: x + y

def map_array(array, func):
    i = 0
    while i < len(array):
        array[i] = func(array[i])
        i += 1
    return array

notes = [12, 16, 19, 13, 3, 20]
print(map_array(notes, lambda x: x + 2 if x < 18 else 20))

# Une fonction étant un objet, on peut la stocker dans une variable.

my_lambda = lambda x: x + 2 if x < 18 else 20
print(map_array(notes, my_lambda))
