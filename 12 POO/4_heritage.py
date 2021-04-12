# On peut faire hériter une classe d'une autre: cela signifie que la classe enfant possèdera tout les attributs et méthodes de la classe parent.
# On peut lui ajouter de nouveaux éléments, et redéfinir les éléments existants.

class User:

    user_count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        User.user_count += 1

    def say_hello(self, punctuation="."):
        print(f"Hello, my name is {self.first_name} {self.last_name}{punctuation}")


class Admin(User):
    # On redéfinie la méthode say_hello:
    def say_hello(self, punctuation="."):
        print(f"Hello, my name is {self.first_name} {self.last_name}{punctuation} I am administrator.")

    def connect_to_database(self, key):
        pass

bill = Admin("Bill", "Parker")
bill.say_hello()
bill.connect_to_database(1234)

peter = User("Peter", "Gates")
peter.say_hello()
#peter.connect_to_database()


# On peut également faire hériter une classe de plusieurs autres (héritage multiple) -> MAUVAISE PRATIQUE.
