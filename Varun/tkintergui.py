from tkinter import *
import tkinter.font

##GUI Definitions
win = Tk()
win.title("Python GUI")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

###Event Functions
def colorToggler():
    hwButton["text"]= "Hello World!"

#Widgets
hwButton = Button(win, text = "Hello World", font = myFont, command = colorToggler, bg = 'bisque2', height=1, width=24)
hwButton.grid(row=0, column=1)
