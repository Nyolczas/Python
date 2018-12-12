import os
from tkinter import ttk
from tkinter import*

bgClr = '#4D4D4D' 
txtClr = '#CCCCCC'
hiClr = 'orange'

# ablak osztály
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('Menő Elemző Mező')
        self.minsize(800, 450)
        self.wm_iconbitmap(os.environ['USERPROFILE']+'/Documents/GitHub/Python/youtube/RetroBlock.ico')
        self.configure(background = bgClr)
        self.createWidget()

         # button
        self.button = ttk.Button(self, text ="Click me!", command = self.btnClick)    
        self.button.grid(column = 0, row = 1)  
    
        #button label
        self.btnLabel = ttk.Label(self, text = "Hello Tkinter")
        self.btnLabel.grid(column = 1, row = 1)
        self.btnLabel.configure(foreground = txtClr, background = bgClr)

    # label  
    def createWidget(self):     
        label = Label(self, text = 'Ez az analizálandó téma címe') #  , font="Roboto 12 bold"
        label.grid(column = 0, row = 0)
        label.configure(foreground = txtClr, background = bgClr)

    def btnClick(self):
        self.btnLabel.configure(text = "most ideklikkoltál és megváltoztattad a szöveget")
        self.btnLabel.configure(foreground = hiClr)

      

root = Root()
root.mainloop()        