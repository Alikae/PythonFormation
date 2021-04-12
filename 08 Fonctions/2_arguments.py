# Arguments
# Il existe plusieurs moyen de définir des arguments en fonction de ce que l'on veut faire.
# Ceux que l'on connait déja s'appellent les "positional parameters".


# Arguments par défaut:
def say_hello(name, greetings="Hello", punctuation="!"):
    print(f"{greetings} {name}{punctuation}")
    
# On peut alors appeler la fonction de plusieurs facon différentes.
say_hello("Bob")
say_hello("Alice", "Bienvenue")
say_hello("Alice", punctuation=".")


# Arguments variadiques (dont le nombre peut varier) non-nommés:
def sum_all_arguments(do_print, *numbers):
    sum = 0
    for n in numbers:
        sum += n
    if do_print:
        print(sum)
    return sum

sum_all_arguments(True, 2, 3, 5, 7, 11)
sum_all_arguments(True)


# Arguments variadiques nommés (keyword arguments / kwargs):
def print_all_arguments(**args_dictionary):
    for key in args_dictionary:
        print(f"{key}: {args_dictionary[key]}")

print_all_arguments(name="Etienne", passions=["music", "code"])


# On peut utiliser les trois types d'arguments au sein de la même fonction.
def example(positional1, *variadics, kw1=42, **kwargs):
    print(f"argument positionel: {positional1}")
    print("arguments variadiques:")
    for v  in variadics:
        print(v)
    print(f"keyword argument: {kw1}")
    print("kwargs:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example("position", "vari1", "vari2", kw1=17, other="lala", other2=42)


# Notion avancée: Unpacking
# On peut "unpack" un itérable dans des arguments variadiques grâce a la syntaxe "*iterable".
sum_all_arguments(True, *range(10))
