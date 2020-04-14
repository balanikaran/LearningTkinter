import tkinter as tk

class TextArea(tk.Text):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        
        self.master = master
        self.config(wrap = tk.WORD)