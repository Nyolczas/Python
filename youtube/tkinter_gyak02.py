from tkinter import*
import os

bgClr = '#4D4D4D' 
txtClr = '#CCCCCC'

# ablak osztály
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('Menő Elemző Mező')
        self.minsize(800, 450)
        self.wm_iconbitmap(os.environ['USERPROFILE']+'/Documents/GitHub/Python/youtube/RetroBlock.ico')
        self.configure(background = bgClr)
        self.createWidget()

    # label  
    def createWidget(self):     
        label = Label(self, text = 'Ez az analizálandó téma neve')
        label.grid(column = 0, row = 0)
        label.configure(foreground = txtClr, background = bgClr)
      

root = Root()
root.mainloop()        