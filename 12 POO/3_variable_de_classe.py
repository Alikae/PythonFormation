# Une classe peut également avoir des variables dîtes "de classe".
# Elles sont accessibles directement via la classe (ClassName.variable) ou via l'instance (instance_name.variable).
# En suivant la même logique, on peut également avoir des méthodes de classe.

class User:

    user_count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        User.user_count += 1

    def say_hello(self, punctuation="."):
        print(f"Hello, my name is {self.first_name} {self.last_name}{punctuation}")

    # On utilise un décorateur pour spécifier qu'une méthode est une méthode de classe.
    @classmethod
    def show_user_count(cls):
        print(f"{cls.user_count} users has been instanciated.")


ryan = User("Ryan", "Smith")

ryan.say_hello("!")

abdel = User("Abdel", "Messaoudi")

abdel.say_hello("!")

print(User.user_count)
print(abdel.user_count)

User.show_user_count()
ryan.show_user_count()
