from tkinter import *
from tkinter.ttk import Combobox
import random
import customtkinter

screen = Tk()
screen.title("Password Generator")
screen.geometry('600x400')

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"


def gen():
    global sc1
    sc1.set("")
    passw = ""
    length = int(c1.get())
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + lowercase
    mixs = '0123456789' + lowercase + uppercase + '@#$%&*'

    if c2.get() == 'Low Strength':
        for i in range(0, length):
            passw = passw + random.choice(lowercase)
        sc1.set(passw)
    elif c2.get() == 'Medium Strength':
        for i in range(0, length):
            passw = passw + random.choice(uppercase)
        sc1.set(passw)
    elif c2.get() == 'High Strength':
        for i in range(0, length):
            passw = passw + random.choice(mixs)
        sc1.set(passw)


sc1 = StringVar()
t1 = Label(screen, text='Random Password Generator', font=('monaco', 25), fg='#0be1ff', )
t1.place(x=52, y=8)
t2 = customtkinter.CTkLabel(screen, text='Password:', text_color='black', text_font=('arial', 14))
t2.place(x=100, y=90)

il = customtkinter.CTkEntry(screen, textvariable=sc1)
il.place(x=230, y=90)
t3 = customtkinter.CTkLabel(screen, text='Length: ', text_color='black', text_font=('arial', 14))
t3.place(x=100, y=136)

t4 = customtkinter.CTkLabel(screen, text='Strength: ', text_color='black', text_font=('arial', 14))
t4.place(x=100, y=185)

c1 = customtkinter.CTkEntry(screen, width=20, )
c1.place(x=230, y=136)

c2 = customtkinter.CTkOptionMenu(screen, width=15,
                                 values=["Low Strength", "Medium Strength", "High Strength"])
c2.place(x=231, y=185)

b = customtkinter.CTkButton(screen, text='Generate', command=gen)
b.place(x=200, y=290)

screen.mainloop()
