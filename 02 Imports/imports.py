# En suivant PEP8, on mets toujours les imports en haut.
# Il existe plusieurs facon d'importer:

# import classique:
import mon_module
# import nommé:
import mon_module2 as mod2
# import spécifique:
from math import pi, sqrt
# Mauvaise pratique!
#from math import *

mon_module.say_hello("Etienne")
root_pi = sqrt(pi)
print(mod2.add_three(root_pi))

