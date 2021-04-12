# La méthode __del__ est le destructeur de la classe: elle sera appelée lorsque le ramasse-miette (garbage collector) de python supprimera la classe,
# ou quand on le fera nous même avec "del mon_instance".

class User:

    user_count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        User.user_count += 1

    def say_hello(self, punctuation="."):
        print(f"Hello, my name is {self.first_name} {self.last_name}{punctuation}")

    def __del__(self):
        # Par exemple, supprimer l'utilisateur de la database.
        print(f"L'utilisateur {self.first_name} {self.last_name} a été supprimé.")

def manipulate_user():
    alban = User("Alban", "Bwat")
    alban.say_hello()

manipulate_user()

louis = User("Louis", "Levelle")
louis.say_hello()

del louis

print("Fin du programme.")