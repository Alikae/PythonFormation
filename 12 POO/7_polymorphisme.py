# En programmation orientée objet, on créé parfois des classes dîtes "abstraites".
# Ce sont des classes qui ne seront jamais instanciées, mais permettent de définir une interface commune entre les classes qui en hériteront.
# On parle de polymorphisme lorsque plusieurs classes différentes peuvent être acceptées dans un contexte donné.

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}!")

class Customer(User):

    def say_hello(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}. I am a customer!")


class Vendor(User):
    
    def say_hello(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}. I am a vendor!")


def inscription(user: User):
    user.say_hello()

abdel = Customer("Abdel", "Messaoudi")
michelle = Vendor("Michelle", "Lezalle")

inscription(abdel)
inscription(michelle)
