# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:30:18 2016

@author: Domagoj
"""

import Tkinter as tk
from Tkinter import *


master = tk.Tk()
master.geometry('800x500')



def projectwindow():
    global lab1
    lab1=Label(master, text="Add Project details")
    lab1.grid(row=4, column=0)
    lab2=Label(master, text="Add Project details")
    lab2.grid(row=5, column=0)
    global b9    
    b9 = Button(master,text="Add Users", command=destroywin)
    b9.grid(row=9, column=0)
    master.update()

    
def destroywin():
    global b9,lab1
    b9.grid_forget()
    lab1.grid_forget()
    master.update()
    
    
#text = tk.Text(root, background='white', foreground='black', font=('Arial', 16))
#text.pack()

"""
master = Tk()
Label(master, text="Enter Username:").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
b = Button(master, text="Enter", width=15) #, command=username_set
b.grid(row=2, column=1)

#text=tk.Text(root)
#text.pack()
#text.insert(END, 'Projects')

listbox = Listbox(root)
listbox.grid(row=0,column=0)
listbox.pack(side=LEFT,padx=10)
listbox.insert(END, "a list entry")
for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

#text.insert('end', '\n\n\n\n\n')
#text.tag_config("a", justify='center')
#text.insert('end', 'Welcome to Keyboard!\n',("a"))
#text.insert('end', 'Load keyboard mapping\n',("a"))
#text.insert('end', 'Begin typing random phrase\n',("a"))  
"""


Label(master, text="Projects").grid(row=0, column=0)
Label(master, text="Groups").grid(row=0, column=1)
Label(master, text="Users").grid(row=0, column=2)
Label(master, text="Instances").grid(row=0, column=3)
Label(master, text="Networks").grid(row=0, column=4)
Label(master, text="Stacks").grid(row=0, column=5)

listbox1 = Listbox(master)
listbox1.grid(row=1,column=0)
for item in ["one", "two", "three", "four"]:
    listbox1.insert(END, item)
    
listbox2 = Listbox(master)
listbox2.grid(row=1,column=1)
for item in ["one", "two", "three", "four"]:
    listbox2.insert(END, item)
    
listbox3 = Listbox(master)
listbox3.grid(row=1,column=2)
for item in ["one", "two", "three", "four"]:
    listbox3.insert(END, item)
    
listbox4 = Listbox(master)
listbox4.grid(row=1,column=3)
for item in ["one", "two", "three", "four"]:
    listbox4.insert(END, item)
    
listbox5 = Listbox(master)
listbox5.grid(row=1,column=4)
for item in ["one", "two", "three", "four"]:
    listbox5.insert(END, item)
    
listbox6 = Listbox(master)
listbox6.grid(row=1,column=5)
for item in ["one", "two", "three", "four"]:
    listbox6.insert(END, item)
    
  
    
b1 = Button(master,text="Add Project").grid(row=2, column=0)
b2 = Button(master,text="Add Group").grid(row=2, column=1)
b3 = Button(master,text="Add Users", command=projectwindow).grid(row=2, column=2)





while True:
    #
    master.update()
    
    
    
    
    
    