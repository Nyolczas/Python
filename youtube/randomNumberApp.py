import tkinter
import random

window = tkinter.Tk()

def RandomNumber():
    myRandom = random.uniform(-6.9, 10.5)
    joslat.configure(text = "A legközelebbi tréded lehet, hogy "
                        + str(round(myRandom,1)) + " % -ot fog hozni.")
    myButton.configure(text="Jósolj Még!")                        

myTitle = tkinter.Label(window, text = "Tréder Varázsgömb", font = "Roboto 16")   
myTitle.pack()

joslat = tkinter.Label(window, font="Roboto 8 bold")
joslat.pack()

myButton = tkinter.Button(window,text="Jósolj!", command=RandomNumber)
myButton.pack()


window.mainloop()