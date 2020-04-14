import tkinter as tk


class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("This is splash screen")
        self.w = 500
        self.h = 500
        self.minsize(self.w, self.h)
        self.resizable(False, False)
        self.splash()

    def splash(self):
        self.update()
