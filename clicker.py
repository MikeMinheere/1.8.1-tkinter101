from textwrap import fill
import tkinter
from tkinter import CENTER,N,S

number = 0

def numUp():
    global number
    number += 1
    if number == 0:
        root.config(bg='grey')
    elif number > 0:
        root.config(bg='green')
    elif number < 0:
        root.config(bg='red')
    displayNumber.config(text=number)

def numDown():
    global number
    number -= 1
    if number == 0:
        root.config(bg='grey')
    elif number > 0:
        root.config(bg='green')
    elif number < 0:
        root.config(bg='red')
    displayNumber.config(text=number)

root = tkinter.Tk()
root.config(bg='grey')
root.geometry('400x350')
root.title('Clicker')

buttonUp=tkinter.Button(root)
buttonUp.configure(text='Up',font=("Courier", 14),anchor=N, command=numUp)
buttonUp.pack(fill='x',padx=40,pady=60)

displayNumber = tkinter.Label(
    root,
    bg='white',
    text=number,
    font=("Courier", 14),
)
displayNumber.pack(fill='x',padx=40)

buttonDown=tkinter.Button(root)
buttonDown.configure(text='Down',font=("Courier", 14),anchor=S, command=numDown)
buttonDown.pack(fill='x',padx=40,pady=60)

root.mainloop()