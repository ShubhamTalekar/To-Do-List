import tkinter as tk
from tkinter import *
import tkinter
from tkinter import messagebox
import pickle


r = tk.Tk()
r.title("To-Do List")
r.geometry("300x400")

listbox_task = tk.Listbox(r, height = 15, width = 50)
listbox_task.pack()

def add():
    task = e.get()
    if task != "":
        listbox_task.insert(tkinter.END,task)
        e.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message = "Cant insert empty task")

def update():
    for item in listbox_task.curselection():
      listbox_task.delete(item)
      listbox_task.insert("end", e.get())
      e.delete(0,tkinter.END)

def delete():
    for item in listbox_task.curselection():
      listbox_task.delete(item)

def save():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("tasks.txt", "wb"))

def load():
    try:
        tasks = pickle.load(open("tasks.txt", "rb"))
        listbox_task.delete(0, tkinter.END)
        for task in tasks:
            listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.") 

L = Label(r, text="Enter Task", width = 9, height = 1)
L.place(x = 15, y = 245)
e = tk.Entry(r, font=('calibre',10,'normal'), width = 19)
e.place(x = 90,y = 245)
b = Button(r, text = "Add", width = 8, command=add)
b.place(x = 230, y = 245)

b = Button(r, text = "Update Task", width = 10, command=update)
b.place(x = 110, y = 268)

b = Button(r, text = "Delete Task", width = 10, command=delete)
b.place(x = 110, y = 298)

b = Button(r, text = "Save List", width = 10, command=save)
b.place(x = 110, y = 325)

b = Button(r, text = "Load List", width = 10, command=load)
b.place(x = 110, y = 355)


r.mainloop()