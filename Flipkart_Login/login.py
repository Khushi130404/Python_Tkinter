from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk


def handle_login():
    e = email_input.get()
    p = pass_input.get()

    if e=="abc@gmail.com" and p=="abc":
        messagebox.showinfo("Success","Login Successful")
    else:
        messagebox.showerror("Error","Login Failed")

root = Tk()
root.title("Flipkart")
root.iconbitmap('logo.svg')
root.geometry('350x500')
root.config(background='#0096DC')

text_label = Label(root,text='Flipkart Login',fg='white',bg='#0096DC')
text_label.pack(pady=(30,10))
text_label.config(font=('Verdana',22))

img = Image.open('flipkart.png')
img = img.resize((90,90))
img = ImageTk.PhotoImage(img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

email_label = Label(root,text="Enter Email",fg='#f4f4f4',bg='#0096DC')
email_label.pack(pady=(15,10))
email_label.config(font=('Verdana',12))

email_input = Entry(root,width=40)
email_input.pack(ipady=6,pady=(1,5))

pass_label = Label(root,text="Enter Password",fg='#f4f4f4',bg='#0096DC')
pass_label.pack(pady=(15,10))
pass_label.config(font=('Verdana',12))

pass_input = Entry(root,width=40)
pass_input.pack(ipady=6,pady=(1,5))

login_button = Button(root,text='Login',bg='#f4f4f4',fg='black',width=20,height=2,command=handle_login)
login_button.pack(pady=(40,20))
login_button.config(font=('verdana',10))

root.mainloop()