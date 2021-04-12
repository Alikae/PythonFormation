# Il existe plusieurs moyens pour lire le contenu d'un fichier.

# Lire n caractères avec read() (ou tout le fichier si on omet l'argument):
mon_fichier = open("09 Fichiers/test", "r", encoding="utf-8")
text = mon_fichier.read(10)
print(text)
text = mon_fichier.read()
print(text)
mon_fichier.close()

# Lire ligne par ligne avec une boucle for:
mon_fichier = open("09 Fichiers/test", "r", encoding="utf-8")
for line in mon_fichier:
    # La ligne contient alors le retour ligne final, encodé "\n".
    print(line + " EOL")
mon_fichier.close()


# Lire ligne par ligne avec readline():
mon_fichier = open("09 Fichiers/test", "r", encoding="utf-8")
print(mon_fichier.readline() * 2)
mon_fichier.close()


# Lire le restant du fichier avec readlines():
mon_fichier = open("09 Fichiers/test", "r", encoding="utf-8")
first_line = mon_fichier.readline()
# Le résultat est stocké dans un tableau de lignes.
print(mon_fichier.readlines())
mon_fichier.close()


# Ecrire dans le fichier avec write:
mon_fichier = open("09 Fichiers/test", "w", encoding="utf-8")
mon_fichier.write("Data:\nfirst line\n")
mon_fichier.write("second line\n")
mon_fichier.close()


# Ecrire dans le fichier avec print:
mon_fichier = open("09 Fichiers/test", "w", encoding="utf-8")
print("Data:\nfirst", file=mon_fichier)
print("second", file=mon_fichier)
mon_fichier.close()


# On peut également se déplacer dans le fichier, sans avoir besoin de le lire avec seek().

# Un autre moyen utile pour parser le fichier avec la syntaxe "with":
# Cette syntaxe permet de fermer automatiquement le fichier, et fonctionne même en cas d'exception levée.
# On appelle ca le context manager.
with open("etudiants.txt", encoding = 'utf-8') as f:
    print("Mostafa", file=f)
