from importlib.metadata import files
from itertools import count
from tkinter import *
from PIL import ImageTk,Image
import os

counter = 1

def rotate():
    global counter
    img_label.config(image=img_arr[counter%len(img_arr)])
    counter += 1

root = Tk()
root.title("Wallpapers")
root.geometry('310x380')
root.config(background="black")

files = os.listdir('Image_2')
img_arr = []

for i in files:
    img = Image.open(os.path.join('Image_2',i))
    img = img.resize((250,250))
    img_arr.append(ImageTk.PhotoImage(img))

img_label = Label(root,image=img_arr[0])
img_label.pack(pady=(30,30))

next_button = Button(root,text="Next",bg='#f4f4f4',fg='black', width=25, height=1, command=rotate)
next_button.pack()
next_button.config(font=('Verdana',12))


root.mainloop()