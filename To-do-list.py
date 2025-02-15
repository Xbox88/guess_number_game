import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("To-DO-List")
root.geometry("350x450")
root.configure(bg="#FF8200")

custom_font = font.Font(family="Arial", size=12)

entry = tk.Entry()
entry.pack()
entry.configure(bg="#B284BE")

listbox = tk.Listbox()
listbox.pack()
listbox.configure(bg="#00FFBF")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)

add_button = tk.Button(root,text="Add",command=add_task,bg="#F4C430",fg="White")
add_button.pack()

def delete_task():
    task = listbox.curselection()
    if task:
        listbox.delete(task[0])

delete_button = tk.Button(root,text="Delete",command=delete_task,bg="#FFD700",fg="White")
delete_button.pack()

def delete_all_task():
    task = listbox
    if task:
        listbox.delete(0,tk.END)

clear_button = tk.Button(root, text="Clear",command=delete_all_task,bg="#FFBF00",fg="White")
clear_button.pack()

root.mainloop()
