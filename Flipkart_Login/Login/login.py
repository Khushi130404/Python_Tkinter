from tkinter import *

root = Tk()
root.title("Flipkart")
root.iconbitmap('logo.png')
root.geometry('350x500')
root.config(background='#0096DC')

text_label = Label(root,text='Flipkart Login',fg='white',bg='#0096DC')
text_label.pack(pady=(50,10))
text_label.config(font=('Verdana',22))

email_label = Label(root,text="Enter Email",fg='#f4f4f4',bg='#0096DC')
email_label.pack(pady=(25,15))
email_label.config(font=('Verdana',12))

email_input = Entry(root,width=40)
email_input.pack(ipady=6,pady=(1,5))

pass_label = Label(root,text="Enter Password",fg='#f4f4f4',bg='#0096DC')
pass_label.pack(pady=(25,15))
pass_label.config(font=('Verdana',12))

pass_input = Entry(root,width=40)
pass_input.pack(ipady=6,pady=(1,5))


root.mainloop()