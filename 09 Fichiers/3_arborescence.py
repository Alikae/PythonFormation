import os
import shutil

print(__file__)

working_path = "."
# Le sous-module os.path permet de manipuler des paths aisément.
working_path = os.path.dirname(__file__)

# Os
for root, dirs, files in os.walk(working_path):
    for name in files:
        if name[-3:] == ".py":
            print(name)
            # shutil est un module copiant des utilitaires shell.
            shutil.copy(f"{working_path}/{name}", f"{working_path}/{name[:-3]}.backup")


# shutil.copy -> 

# zlib -> module de compression de données très utilisé.
