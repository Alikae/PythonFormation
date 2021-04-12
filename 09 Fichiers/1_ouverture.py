# Ouverture
# On appelle l'objet qui représente un fichier "descripteur".
# On l'obtient grâce a la fonction open().
# open() prend en argument le "path" du fichier, ainsi qu'un mode dont les plus courants sont:
# "r" pour lire (read)
# "w" pour écrire (write) en ayant au préalable effacé le contenu du fichier
# "a" pour écrire a partir de la fin du fichier (append)

# "w+" pour lire ET créer 

print(open.__doc__)
mon_fichier = open("09 Fichiers/test", "r", encoding="utf-8")
print(mon_fichier)

# Lorsqu'on a plus besoin du fichier, il est préférable de spécifier au système de libérer les ressources qui lui sont liées avec la méthode close().
mon_fichier.close()
