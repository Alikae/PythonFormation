# On peut récupérer les arguments donnés au script grâce au module sys
# et plus précisément "sys.argv".
import sys

print(sys.argv)
print(type(sys.argv))

for arg in sys.argv:
    print(arg)
