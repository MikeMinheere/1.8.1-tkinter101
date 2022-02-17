def updateWindow():
    button.configure(command=buttonAction)

def buttonAction():
    print('kaas')

grabbelton = ['appel','vis','jojo','hotwheel','pizza','bowlingbal','pils','lamp','bank','stoel','geit','barbie pop','papier','laptop','Xbox']

import tkinter
import random

root = tkinter.Tk()
root.config(bg='light green')
root.geometry('200x200')
root.title('grabbelton')

button=tkinter.Button(root)
button.configure(text='pak iets uit de grabbelton', command=updateWindow)
button.pack(padx=20,pady=20)

root.mainloop()