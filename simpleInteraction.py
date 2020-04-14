import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Interaction")

        self.labelText = tk.StringVar()
        self.labelText.set("Choose One!")

        self.label = tk.Label(self, textvariable = self.labelText)
        self.label.pack(fill = tk.BOTH, expand = 1, padx = 100, pady = 50)

        self.helloButton = tk.Button(self, text = "Say Hello!", command = self.sayHello)
        self.helloButton.pack(side = tk.LEFT, padx = (20, 0), pady = (0, 20))

        self.goodByeButton = tk.Button(self, text = "Good Bye!", command = self.goodBye)
        self.goodByeButton.pack(side = tk.RIGHT, padx = (0, 20), pady = (0, 20))

    def sayHello(self):
        self.labelText.set("Hello! Ssup?")
        # self.label.config(text = self.labelText.get())

    def goodBye(self):
        self.labelText.set("Bye! Closing in 2 seconds...")
        # self.label.config(text = self.labelText.get())
        self.after(2000, self.destroy)

if __name__ == "__main__":
    window = Window()
    window.mainloop()