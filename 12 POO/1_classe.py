# Une classe est un type d'objet pouvant contenir des attributs (variables) et méthodes (fonctions).
# Elle sert a définir le comportement d'un ensemble d'objets, qui seront des instances de cette classe.
# Une classe est comme le "patron" ou "blueprint" de tout les objets qui seront instanciés a partir de celle ci.

class User:

    # Le premier argument d'une méthode d'instance est toujours "self" et représente l'instance qui appelle cette méthode.
    def say_hello(self, punctuation="."):
        print(f"Hello, my name is {self.first_name} {self.last_name}{punctuation}")

ryan = User()
ryan.first_name = "Ryan"
ryan.last_name = "Smith"

ryan.say_hello("!")

abdel = User()
abdel.first_name = "Abdel"
abdel.last_name = "Messaoudi"

abdel.say_hello()
ryan.say_hello()
