# Tkinter est codée en python, C, CTL, et utilise la Xlib comme librairie graphique.
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Le packer (empaqueteur) est l'assembleur graphique,
        # On l'appelle avec la méthode pack().
        # Il est parfois nommé "Gestionnaire de géométrie".
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # On créé un attribut pour stocker un élément graphique.
        # On l'instancie depuis une classe Tkinter existante.
        self.hi_there = tk.Button(self)
        # On peut ensuite associer des attributs et des comportements a cet élément.
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        # On l'ajoute enfin au packer.
        self.hi_there.pack(side="top")

        # On peut aussi directement initialiser ces attributs/comportement a l'instanciation de l'élément.
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy) # master.destroy termine l'application.
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

# On initialise Tkinter
root = tk.Tk()
# On créé l'application en lui fournissant le contexte Tkinter
app = Application(master=root)
# Et on lance le main loop
app.mainloop()