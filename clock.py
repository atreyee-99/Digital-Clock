from tkinter import *
import sys
import time

def times():
    cur_time=time.strftime('%H:%M:%S')
    clock.config(text=cur_time)
    clock.after(200,times)


root=Tk()
root.geometry('500x250')
root.title('Clock')

clock=Label(root,font=('times',50,'bold'),bg='white')
clock.grid(row=2,column=2,pady=25,padx=100)
times()

dig=Label(root,text="Digital Clock",font=('times',24,'bold'))
dig.grid(row=0,column=2)

desc=Label(root,text="HOURS    MINUTES   SECONDS",font=('times',15,'bold'))
desc.grid(row=3,column=2)

root.mainloop()