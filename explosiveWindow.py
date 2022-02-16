import tkinter
import random
import time

a=6
colors =['yellow','green','orange','pink','red','blue','purple']
explosiveWindow =tkinter.Tk()
explosiveWindow.geometry('50x100')
time.sleep(2)
def loop():
    global colors,a
    explosiveWindow.configure(bg=random.choice(colors))
    explosiveWindow.after(2000,loop)
loop()
explosiveWindow.mainloop()
