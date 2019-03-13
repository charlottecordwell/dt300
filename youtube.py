

import sys
from tkinter import *
import tkinter.messagebox

mGui = Tk()


def Quit():
    mExit = tkinter.messagebox.askokcancel(title="Quit", message="Are you sure")
    print(mExit)
    if mExit >0: #1 is True 0 is False
        mGui.destroy()
    return

def processdata():
    #process data, note access to tkinter variables
    uname=name.get()
    print(uname)
    nameEntry.delete(0,END)

    
#gui box size and desgin    
mGui.geometry('450x450+200+200')
mGui.title('My Youtube tkinter')
mGui.configure(background = 'gray')

name=StringVar()

#order of lables/buttons

#testing gui
mlabel = Label(mGui,text='Testing a GUI is a challenge', fg='red',bg='white')
mlabel.pack()

#name lable
nameEntryl = Label(mGui,text='Name',fg='red',bg='white')
nameEntryl.pack()

#name entry box
nameEntry = Entry(mGui,textvariable=name)
nameEntry.insert(10,"Shrek")
nameEntry.pack()

#ok button
mbutton = Button(mGui,text="OK",command=processdata, fg='red')
mbutton.pack()

#quit button
qbutton = Button(mGui,text="Quit",command=Quit, fg='red')
qbutton.pack()

mGui.mainloop()
