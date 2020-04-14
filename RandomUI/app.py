from RandomUI.screens import splashScreen
import tkinter as tk
from RandomUI.init import InitializeApp


class App(tk.Tk):
    # initialise the app here
    # also show the splash screen
    def __init__(self):
        super().__init__()
        self.withdraw()

        # show splash screen
        splash = splashScreen.SplashScreen(self)

        # simulate initialization
        self.initStatus = InitializeApp.start()
        print(self.initStatus)

        splash.destroy()

        self.deiconify()


if __name__ == '__main__':
    app = App()
    app.mainloop()
