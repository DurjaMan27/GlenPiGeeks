from tkinter import *
import tkinter.font

##GUI Definitions
win = Tk()
win.title("Glen Pi Geeks GUI")
myFont = tkinter.font.Font(family = 'Calibri', size = 12, weight = "bold")

###Event Functions
def colorToggler():
    hwButton["text"]= "Hello from GPG!"

#widgets
hwButton = Button(win, text = "Welcome", font = myFont, command = colorToggler, bg = 'bisque2', height=1, width =24)
hwButton.grid(row=0, column=1)
