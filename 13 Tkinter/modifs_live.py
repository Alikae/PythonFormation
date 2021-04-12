import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self, text="Change Color!",
                                command=self.change_color,
                                bg="red")
        self.button.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def change_color(self):
        # On peut lire les attributs actuels comme dans un dictionnaire:
        if self.button["bg"] != "blue":
            self.button["bg"] = "blue"
        else:
            # config() permet de modifier plusieurs attributs a la fois.
            self.button.config(bg="red", command=self.change_color)
            

root = tk.Tk()
app = Application(master=root)
app.mainloop()