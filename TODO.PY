import tkinter
from tkinter import *
from tkinter import ttk

class TODO:
    def __init__(self,root):
        self.root=root
        self.root.title('to-do-list')
        self.root.geometry("700x510+400+150")
        self.label=Label(self.root,text='TO-DO-LIST',font='ariel, 25 bold',width=10,bd=5,bg='pink',fg='black')
        self.label.pack(side='top',fill=BOTH)
        self.label2=Label(self.root,text='ADD-INFO',font='ariel, 25 bold',width=10,bd=5,bg='pink',fg='black')
        self.label2.place(x=40,y=54)
        self.label3=Label(self.root,text='TASKS',font='ariel, 25 bold',width=10,bd=5,bg='pink',fg='black')
        self.label3.place(x=320,y=54)
        self.main_txt=Listbox(self.root,height=12,width=23,bd=5,font="ariel, 15 italic bold")
        self.main_txt.place(x=300,y=120)
        self.txt= Text(self.root,height=2,width=30,bd=5,font='ariel, 10 bold')
        self.txt.place(x=30,y=120)
        def add():
         content = self.txt.get(1.0,END)
         self.main_txt.insert(END,content)
         with open('data.txt','a')as file:
            file.write(content)
            file.seek(0)
            file.close()
         self.txt.delete(1.0,END)
        def delete():
         delete_=self.main_txt.curselection()
         look=self.main_txt.get(delete_)
         with open('data.txt','r+') as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                item=str(look)
                if item not in line:
                    f.write(line)
            f.truncate()
         self.main_txt.delete(delete_)
        
        with open('data.txt','r') as file:
            read=file.readlines()
            for i in read:
             ready=i.split()
             self.main_txt.insert(END,ready)
            file.close()
        self.button=Button(self.root,text="add",font='sarif, 20 bold italic',
                           width=10,bd=5,bg='orange',fg='black',command=add)
        self.button.place(x=30,y=200) 
        self.button2=Button(self.root,text="delete",font='sarif, 20 bold italic',
                           width=10,bd=5,bg='orange',fg='black',command=delete)
        self.button2.place(x=30,y=300)
                         

root=Tk()
ui=TODO(root)
root.mainloop()

