import tkinter as tk

class MyMenu(tk.Menu):
    def __init__(self, master: tk.Tk):
        super().__init__(master=master)

        fileMenu = tk.Menu(master=self)

        fileMenu.add_command(label="Label 1")
        fileMenu.add_command(label="Label 2")

        self.add_cascade(label="File", menu=fileMenu)

root = tk.Tk()
root.minsize(300,300)
root.config(menu=MyMenu(root))
root.mainloop()