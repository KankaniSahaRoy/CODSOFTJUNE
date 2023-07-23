from tkinter import *
import random,string

root=Tk()
root.geometry("450x400")
root.title("password generator")
title=StringVar()
label=Label(root,textvariable=title,font=('times new roman',20,'bold')).pack()
title.set("The Strength Of The Password")


def select():
  select=choice.get()
choice=IntVar()
Font=('arial',13,'bold')
r1=Radiobutton(root,text="POOR",variable=choice,value=1,command=select,font=Font).pack(anchor=CENTER)
r1=Radiobutton(root,text="AVERAGE",variable=choice,value=2,command=select,font=Font).pack(anchor=CENTER)
r1=Radiobutton(root,text="BEST",variable=choice,value=3,command=select,font=Font).pack(anchor=CENTER)
labelchoice=Label(root)
labelchoice.pack()

lengthlabel=StringVar()
lengthlabel.set("Password Length")
lengthtitle=Label(root, textvariable=lengthlabel,font=('times new roman',20,'bold')).pack()

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_char=string.punctuation
    all=small_alphabets+capital_alphabets+numbers+special_char
    password_length=int(length_box.get())

    if choice.get()==1:
       passwordFied.insert(0,random.sample(small_alphabets,password_length))
    
    if choice.get()==2:
       passwordFied.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    
    if choice.get()==3:
       passwordFied.insert(0,random.sample(all,password_length))

    
length_box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_box.pack(pady=10)

generetorbutton=Button(root,text="generate",font=(('arial',15,'bold')),command=generator).pack(pady=10)
passwordFied=Entry(root,width=20,bd=2,font=('arial',20,'bold'))
passwordFied.pack(pady=10)


root.mainloop()