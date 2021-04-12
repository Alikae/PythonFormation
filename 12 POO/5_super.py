# Lors de la redéfinition d'une méthode, on peut utiliser la syntaxe super().parent_method qui va executer la fonction parent correspondante.

class User:

    user_count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        User.user_count += 1

    def say_hello(self, punctuation="."):
        print(f"Hello, my name is {self.first_name} {self.last_name}{punctuation}")


class Admin(User):

    def __init__(self, first_name, last_name, key):
        super().__init__(first_name, last_name)
        self.key = key

    def say_hello(self, punctuation="."):
        super().say_hello()
        print(f"I am administrator.")


bill = Admin("Bill", "Parker", 1234)
bill.say_hello()

print(bill.key)
