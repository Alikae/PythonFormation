# On peut parfois "transformer" un type en un autre avec ce qu'on appelle un "cast".

var = float("3.6")
print(f"{var} est de type {type(var)}")

var = int(var)
print(f"{var} est de type {type(var)}")

var = str(var)
print(f"{var} est de type {type(var)}")

var = list(var)
var.append(42)
print(f"{var} est de type {type(var)}")
