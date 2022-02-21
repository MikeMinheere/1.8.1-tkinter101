from distutils.command.clean import clean
from turtle import Screen, clear


def buttonAction():
    random.shuffle(grabbelton)
    displayItem = tkinter.Label(
        root,
        bg = 'light green',
        text= 'Gefeliciteerd! je hebt een \n'+grabbelton[0]+' gegrabbelt!\n\n er zijn '+str(len(grabbelton))+' items in de grabbelton' 
    )
    displayItem.place(relx=0.5, rely=0.51, anchor=CENTER)
    displayItem.config(font=("Courier", 14),fg='black')
    del grabbelton[0]

import tkinter
from tkinter import CENTER
import random
import time

grabbelton = ['appel','vis','jojo','hotwheel','pizza','bowlingbal','pils','lamp','bank','stoel','geit','barbie pop','papier','laptop','Xbox']

root = tkinter.Tk()
root.config(bg='light green')
root.geometry('390x300')
root.title('grabbelton')

button=tkinter.Button(root)
button.configure(text='pak iets uit de grabbelton', command=buttonAction)
button.pack(padx=20,pady=20)

root.mainloop()