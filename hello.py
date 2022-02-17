import tkinter as tk
from tkinter import CENTER, ttk
from tkinter import font

root = tk.Tk()
root.title('hello')
root.geometry("250x200")
root.configure(bg='green')

middle = tk.Label(  
    root,
    bg = 'blue',
    text= 'Hello \n World!',
) 
middle.place(relx=0.5, rely=0.5, anchor=CENTER)
middle.config(font=("Fixedsys", 35),fg='red')
root.mainloop()