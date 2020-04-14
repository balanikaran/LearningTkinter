import tkinter as tk
import tkinter.ttk as ttk

from textEditor.textarea import TextArea


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.textArea = TextArea(self, bg="white", fg="black", undo=True)

        self.scrollBar = tk.Scrollbar(orient="vertical", command=self.scroll_text)

        self.textArea.configure(yscrollcommand=self.scrollBar.set)

        self.scrollBar.pack(side=tk.LEFT, fill=tk.Y)
        self.textArea.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def scroll_text(self, *args):
        self.textArea.yview_moveto(args[1])


if __name__ == "__main__":
    mainWindow = MainWindow()
    mainWindow.mainloop()
