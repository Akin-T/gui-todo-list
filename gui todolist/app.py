import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("ToDo List")
app.geometry("600x700")
app.config(bg='#09112e')

font1 = ("Arial",30,"bold")
font2 = ("Arial",18,"bold")
font3 = ("Arial",10,"bold")


def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror('Hata', 'Bir not giriniz.')


def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Hata', 'Silmek için bir not seçiniz.')

def save_tasks():
    with open("tasks.txt","w") as f:
        tasks = tasks_list.get(0,END)
        for task in tasks:
            f.write(task+ "\n")


def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            tasks = f.readline()
            for task in tasks:
               tasks_list.insert(0,task.strip())
    except FileNotFoundError:
        messagebox.showerror('Hata', 'Görevler yüklenemiyor')

title_label =customtkinter.CTkLabel(app,font=font1,text='ToDo List',text_color='#fff', bg_color='#09112e')
title_label.place(x=100,y=20)

add_button = customtkinter.CTkButton(app,command=add_task , font=font2,text_color='#fff',text="Ekle",corner_radius=5,width=120)
add_button.place(x=40,y=80)


remove_button = customtkinter.CTkButton(app,command=remove_task,font=font2,text_color='#fff',text="Sil")
remove_button.place(x=180,y=80)

task_entry = customtkinter.CTkEntry(app,font=font2,text_color='#000' ,width=280)
task_entry.place(x=40,y=120)

tasks_list = Listbox(app,width=39,height=15,font=font3)
tasks_list.place(x=40,y=180)



app.mainloop()
