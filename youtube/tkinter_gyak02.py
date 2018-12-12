from tkinter import*
import os

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('Menő Elemző Mező')
        self.minsize(800, 450)
        self.wm_iconbitmap(os.environ['USERPROFILE']+'/Documents/GitHub/Python/youtube/RetroBlock.ico')
        self.configure(background = '#4D4D4D')

root = Root()
root.mainloop()        