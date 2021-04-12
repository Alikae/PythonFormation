print(f"Module '{__name__}': Ce code sera exécuté une seule fois si ce module est importé au moins une fois.")
print("Ce code permet la plupart du temps d'initialiser le module.")

if __name__ == "__main__":
    print("Ce code n'est interprété que si ce module est lancé en tant que tel, pas si il est importé.")
    print("Ca peut être utilisé pour tester le module sans parasiter les programmes qui l'importeront.")
