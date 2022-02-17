import tkinter
import random
import time

a = 50
b = 6
colors =['yellow','green','orange','pink','red','blue','purple']
explosiveWindow =tkinter.Tk()
explosiveWindow.title('Explosive window')
time.sleep(2)
def loop():
    global colors,a,b
    explosiveWindow.configure(bg=random.choice(colors))
    if b >= 1:
        print(b)
        b-=1
        explosiveWindow.geometry(str(a)+'x'+str(a))
        a+=50
        explosiveWindow.after(2000,loop)
    elif b == 0:
        print("BOOM!!!")
        explosiveWindow.destroy()
loop()
explosiveWindow.mainloop()