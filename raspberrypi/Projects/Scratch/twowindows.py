from tkinter import *
import random
import math
from PIL import ImageTk
from PIL import Image

root = Tk()
canvas = Canvas(root)
background_image=PhotoImage(file="/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.png")
canvas.pack(fill=BOTH, expand=1) # Stretch canvas to root window size.
image = canvas.create_image(0, 0, anchor=NW, image=background_image)
root.wm_geometry("794x370")
root.title('Map')

def toplevel():
    top = Toplevel()
    top.title('Optimized Map')
    top.wm_geometry("794x370")
    #img = Image.open("/home/pi/GlenPiGeeks/PiPhotoBoothPictures/image.jpg")
    img = Image.open("image.png")
    #photoimg = ImageTk.PhotoImage(img)
    #background_image=PhotoImage(file="image.png")
    optimized_canvas = Canvas(top)
    optimized_canvas.pack(fill=BOTH, expand=1)
    optimized_image = optimized_canvas.create_image(0, 0, anchor=NW, image=background_image)

toplevel()

root.mainloop()
