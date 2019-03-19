#----------
# Char


#load tkinter library
from tkinter import *
import tkinter.messagebox  #need to import this

def processdata():
#process data, note access to tkinter variables
    print(bookName.get())
    uname=bookName.get().upper()
    print(uname)
    bookNameEntry.delete(0,END)
##    magelabel = Label(mGui, text=age.get())
##    magelabel.pack()
    print(copies.get())
    print(genre.get())



def Quit():
    mExit = tkinter.messagebox.askokcancel(title="Quit", message="Are you sure")
    print(mExit)
    if mExit >0: #1 is True 0 is False
        mGui.destroy()
    return

mGui=Tk()


#variable types that are used by tkinter
bookName=StringVar()
copies=IntVar()
genre=StringVar()

#primary window
mGui.geometry('450x450+50+30') #+50 +30 give starting postion on screen
mGui.title('Book Inventory')
mGui.configure(background = '#dbf2cb')

#Simple label used for header
mlabel = Label(mGui,text='Book Inventory',fg='#509621',bg='white', font =('Roboto', 18))
mlabel.pack(pady=5)

#data entry label and Entry field for text and integer. Includes insertion of default values
#note the text variables as name and gae as declared above
bookNameEntryl = Label(mGui,text='Book Name',fg='red',bg='white')
bookNameEntryl.pack(pady =5, anchor=W)
bookNameEntry = Entry(mGui,textvariable=bookName)
bookNameEntry.insert(10,"book name")
bookNameEntry.pack(pady =5, anchor=W)

copiesEntryl = Label(mGui,text='Number of Copies',fg='red',bg='white')
copiesEntryl.pack()
copiesEntry = Entry(mGui, textvariable=copies)
copiesEntry.insert(10,1)
copiesEntry.pack(pady =5)

#obtain data from a pull down list
genreEntry1 = Label(mGui, text='Genre',fg="red", bg="black")
genreEntry1.pack(pady =5)
genreEntry=OptionMenu(mGui, genre, "Science Fiction", "Sport", "Biography", "Political Thriller")
genreEntry.pack(pady =5)

#OK button ie event used to initiatiate a command ie processdata
mbutton = Button(mGui,text="Add Book",command=processdata, fg='red')
mbutton.pack(pady =5)

#QUIT button ie event to quit
qbutton = Button(mGui,text="DIVISION BY ZERO DETECTED THE UNIVERSE HAS ENDED!",command=Quit, fg='red')
qbutton.pack(pady =5)

mGui.mainloop()
