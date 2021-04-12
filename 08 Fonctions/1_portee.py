# Une fonction est un bloc de code nommé, pouvant prendre des arguments et souvent destinée a être executée plusieurs fois.
# Elle est de la forme: "def name(arguments):" suivie d'un bloc indenté contenant son code.


# SCOPE (portée)
# Une variable n'est accessible que dans son propre bloc.
# On peut également y accéder depuis tout les scopes imbriqués contenus dans celui-ci, grâce au mot-clé "nonlocal".

def a():
    x = 42
    print(x)
    def b(): # La fonction b n'est accessible qu'au sein de la fonction a car c'est dans ce scope qu'elle a été déclarée.
        print(x) # Scope imbriqué, on peut accéder a x ici.

    def c():
        nonlocal x
        x += 2 # Pour avoir le droit de modifier x, on doit utiliser le mot-clé "nonlocal".
        print(x)
    b()
    c()
    print(x)

a()

# Essayer d'accéder a x ici déclenchera une erreur, car nous sommes sortis du scope dans lequel il a été déclaré.
#print(x)


#En définissant une variable dans le scope global, on peut y accéder de n'importe ou dans le fichier grâce au mot-clé "global".
glob = 33

def add_to_glob(n):
    global glob
    glob += n


print(glob)
add_to_glob(3)
print(glob)
