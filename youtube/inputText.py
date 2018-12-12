from tkinter import*
from tkinter import ttk
import os

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('Menő Beviteli Mező')
        self.minsize(800, 450)
        self.wm_iconbitmap(os.environ['USERPROFILE']+'/Documents/GitHub/Python/youtube/RetroBlock.ico')
        self.initUI()

    def btnClick(self):
        self.label.configure(text = "Hello " + self.name.get())


    def initUI(self):

        self.name = StringVar()

        self.label = ttk.Label(self, text = "Hogy hívják a nevedet?")    
        self.label.grid(column = 0, row = 0)   

        self.textbox = ttk.Entry(self, width = 20, textvariable = self.name)
        self.textbox.grid(column = 0, row = 1)

        self.button = ttk.Button(self, text = "Send", command = self.btnClick)
        self.button.grid(column = 0, row = 2)

root = Root()
root.mainloop()          