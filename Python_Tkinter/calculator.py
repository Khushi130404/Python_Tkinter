from tkinter import *

from bokeh.layouts import column
from click import command

first_number=second_number=operator=None

def write_digit(digit):
    text = result_label['text']
    text+=digit
    result_label.config(text=text)

def clear():
    result_label.config(text="")


root = Tk()
root.title("Calculator")
root.geometry("280x380")
root.resizable(0,0)
root.configure(background='black')

result_label = Label(root,text="",bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=5,sticky="w",pady=(50,25))
result_label.config(font=('verdana',30,'bold'))

text_arr = [["7","8","9","+"],["4","5","6","-"],["1","2","3","*"],["0","c","=","/"]]
btn_arr = []
for i in range(4):
    b_arr = []
    for j in range(4):
        btn = Button(root, text=text_arr[i][j], bg='#00a65a', fg='white', width=5, height=2)
        if i<3 and j<3 or text_arr[i][j]=="0":
            btn.config(command=lambda text=text_arr[i][j]: write_digit(text))
        elif i==3 and j==1:
            btn.config(command=clear)
        btn.grid(row=i+1,column=j+1)
        btn.config(font=('verdana',14))
        b_arr.append(btn)
    btn_arr.append(b_arr)

root.mainloop()