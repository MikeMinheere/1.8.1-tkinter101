from tkinter import *
from tkinter.ttk import *
 
# import strftime functie
# krijg systeem tijd
from time import strftime
 
# maak tkinter window
root = Tk()
root.title('Clock')
 
#dit is om de tijd te displayen
def time():
    string = strftime('%H:%M:%S') 
    lbl.config(text = string)
    lbl.after(1000, time)
 
#styling
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'light green',
            foreground = 'black')
 
#klok centreren
lbl.pack(anchor = CENTER)
time()
 
mainloop()