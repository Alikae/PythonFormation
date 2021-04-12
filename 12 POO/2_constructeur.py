# Une méthode __init__ sert de constructeur a la classe.
# Lorsqu'on instanciera cette classe, c'est cette fonction qui sera appelée.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self, punctuation="."):
        print(f"Hello, my name is {self.first_name} {self.last_name}{punctuation}")

ryan = User("Ryan", "Smith")

ryan.say_hello("!")

abdel = User("Abdel", "Messaoudi")

abdel.say_hello("!")
