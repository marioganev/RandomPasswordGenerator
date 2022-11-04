from tkinter import *
from tkinter.ttk import Combobox
import random

screen = Tk()
screen.title("Password Generator")
screen.geometry('700x400')
screen.configure(background ="RoyalBlue1")


def gen():
    global sc1
    sc1.set("")
    passw=""
    length=int(c1.get())
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'+lowercase
    mixs='0123456789'+lowercase+uppercase+'@#$%&*'

    if c2.get()=='Low Strength':
        for i in range(0,length):
            passw=passw+random.choice(lowercase)
        sc1.set(passw)
    elif c2.get()=='Medium Strength':
        for i in range(0,length):
            passw=passw+random.choice(uppercase)
        sc1.set(passw)
    elif c2.get()=='High Strength':
        for i in range(0,length):
            passw=passw+random.choice(mixs)
        sc1.set(passw)

sc1=StringVar('')
t1=Label(screen,text='Random Password Generator',font=('monaco',25),fg='seashell',background ="RoyalBlue1")
t1.place(x=30,y=8)
t2=Label(screen,text='Password:',font=('Arial',14),background ="RoyalBlue1")
t2.place(x=117,y=90)

il=Entry(screen,font=('Arial',14),textvariable=sc1)
il.place(x=230,y=90)
t3=Label(screen,text='Length: ',font=('Arial',14),background ="RoyalBlue1")
t3.place(x=145,y=136)

t4=Label(screen,text='Strength:',font=('Arial',14),background ="RoyalBlue1")
t4.place(x=130,y=185)

c1=Entry(screen,font=('Arial',14),width=10)
c1.place(x=230,y=136)

c2=Combobox(screen,font=('Arial',14),width=15)
c2['values']=('Low Strength','Medium Strength','High Strength')
c2.current(1)
c2.place(x=231,y=185)

b=Button(screen,text='Generate',font=('M+',14),fg='black',background ="yellow2",command=gen)
b.place(x=270,y=290)


screen.mainloop()
