#------------------------------------------
# Authour: Charlotte Cordwell
#
# Name: Report Generator
# File Name: report_v4
#
# Purpose: Generates a report for year 13 students
# Version : #4
#
# Changes :
# - remove get_values()
# - added writetocsv() + GUI button
# - 
# - 
# - 
# Creation Date: 3/4/19
#-----------------------------------------

def main():
      pass
if __name__== "__main__":
      main()
      
# getting GUI library
from tkinter import *
#need to espcially import this
import tkinter.messagebox

class Report:
      def __init__(self, fn, ln, student_no, background_c, constructive_c, classwork_c):
            self.fn = fn.capitalize()
            self.ln = ln.capitalize()
            self.student_no = student_no
            self.background_c = background_c
            self.constructive_c = constructive_c
            self.classwork_c = classwork_c
            
      def get_fn(self):
            return self.fn

      def get_ln(self):
            return self.ln
      
      def get_student_no(self):
            return self.student_no
      
      def get_background_c(self):
            return self.background_c

      def get_constructive_c(self):
            return self.constructive_c
      
      def get_classwork_c(self):
            return self.classwork_c


def processdata():
      
      ufn = fn.get().capitalize()
      #print(ufn)
      fnEntry.delete(0,END)
      fnEntry.insert(20,"noname")
      
      uln = ln.get().capitalize()
      lnEntry.delete(0,END)
      lnEntry.insert(20,"noname")
      #print(uln)

      ustudent_no = student_no.get()
      #print(ustudent_no)

      uback = background_c.get()
      #print(uback)
      
      uconstructive = constructive_c.get()
      #print(uconstructive)

      uclasswork = classwork_c.get()
      #print(uclasswork)
      
      students.append(Report(ufn, uln, ustudent_no, uback, uconstructive, uclasswork))
      print(students)
      
def writetocsv():
      import csv
      file_name = "student_report.csv"
      ofile = open(file_name, "w") #'w' for testing purposes
      writer = csv.writer(ofile, delimiter=',',lineterminator='\n')
      #cycles through list of records
      for i in range (0, len (students)):
            #the following code is used for debugging purposes
            print(students[i].fn)
            print(students[i].ln)
            print(students[i].student_no)
            print(students[i].background_c)
            print(students[i].constructive_c)
            print(students[i].classwork_c)

            writer.writerow([students[i].fn, students[i].ln, students[i].student_no, students[i].background_c, students[i].constructive_c, students[i].classwork_c,])
      ofile.close()
      
def Quit():
    mExit = tkinter.messagebox.askokcancel(title="Quit", message="Are you sure")
    print(mExit)
    if mExit >0: #1 is True 0 is False
        mGui.destroy()
    return

    
mGui = Tk()      
#variable types that are used by tkinter
fn = StringVar()
ln = StringVar()
student_no = IntVar()

BACKGROUND = ["Excellent Student", "Good Student", "Strugggling Student"]
background_c = StringVar()
background_c.set(BACKGROUND[0]) #makes the drop down all entrys in the BACKGROUND list 

CONSTRUCTIVE = ["As work load increases she needs to manage her time", "Needs to be more attetive in calss", "Needs to come to class"]
constructive_c = StringVar()
constructive_c.set(CONSTRUCTIVE[0])

CLASS_WORK = ["Completes work to a high standard", "Completes Work","Does not do assgined work"]
classwork_c = StringVar()
classwork_c.set(CLASS_WORK[0])

#primary window
mGui.geometry('600x500')
mGui.title('Report Generator')
mGui.configure(background = '#fcedd1')

#Simple label used for header
mlabel = Label(mGui,text='Year 13 Report Generator',fg ='#383123',bg ='#fcedd1', font =("Courier",24))
mlabel.grid(row = 0, columnspan = 2)

#data entry label and Entry field for text and integer. Includes insertion of default values
#note the text variables as name and gae as declared above
fnEntryl = Label(mGui,text='First Name:',fg='#383123',bg='#fcedd1',font =("Courier",12,"bold"))
fnEntryl.grid(row = 1, column = 0, sticky = W, padx = 5,pady = 5)
fnEntry = Entry(mGui,textvariable=fn)
fnEntry.insert(10,"FirstName")
fnEntry.grid(row=1, column = 1,sticky =EW,pady=5)

#last name field
lnEntryl = Label(mGui,text='Last Name:',fg='#383123',bg='#fcedd1',font =("Courier",12,"bold"))
lnEntryl.grid(row = 2, column = 0,sticky = W, padx = 5,pady = 5)
lnEntry = Entry(mGui, textvariable=ln)
lnEntry.insert(50, "LastName")
lnEntry.grid(row=2, column = 1,sticky = EW, pady = 5)

#student number field
student_noEntryl = Label(mGui,text='Student Number:',fg='#383123',bg='#fcedd1',font =("Courier",12,"bold"))
student_noEntryl.grid(row = 3, column = 0,sticky = W,padx = 5, pady = 5)
student_noEntry = Entry(mGui, textvariable=student_no)
student_noEntry.insert(10,1)
student_noEntry.grid(row = 3, column = 1, sticky = EW, pady =5 )

#comments lable
mlabel = Label(mGui,text='Please choose commentS.',fg='#383123',bg='#fcedd1', font =("Courier",18))
mlabel.grid(row=4, columnspan=2)

#background comment field
background_cEntry1 = Label(mGui, text='Background Comment:', fg = '#383123' ,bg = '#fcedd1', font = ("Courier",12,"bold"))
background_cEntry1.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)
background_cEntry= OptionMenu(mGui, background_c, *BACKGROUND)
background_cEntry.config(width=50) #makes this whole column 1 stay at 50 px wide.
background_cEntry.grid(row = 5, column = 1, sticky= EW, pady = 5)

# constructive comment field
constructive_cEntry1 = Label(mGui, text='Constructive Comment:', fg = '#383123' ,bg = '#fcedd1', font = ("Courier",12,"bold"))
constructive_cEntry1.grid(row = 6, column = 0, sticky = W, padx = 5,pady = 5)
constructive_cEntry= OptionMenu(mGui, constructive_c, *CONSTRUCTIVE)
constructive_cEntry.grid(row=6, column = 1,sticky = EW, pady = 5)

#class wokr comment field
classwork_cEntry1 = Label(mGui, text='Class Work Comment:', fg = '#383123' ,bg = '#fcedd1', font = ("Courier",12,"bold"))
classwork_cEntry1.grid(row=7, column = 0,sticky =W,padx=5,pady=5)
classwork_cEntry= OptionMenu(mGui, classwork_c,  *CLASS_WORK)
classwork_cEntry.grid(row = 7, column = 1,sticky= EW,pady = 5 )      

#Submit data
mbutton = Button(mGui,text="Submit",command=processdata, fg='black')
mbutton.grid(row = 8, column = 1, pady = 5)

#write to csv
qbutton = Button(mGui,text="Write to CSV",command= writetocsv, fg='red',bg="#a4a8a5",font =("Courier",10))
qbutton.grid(row = 9,columnspan = 2,pady = 5, padx = 11)

#QUIT button ie event to quit
qbutton = Button(mGui,text="Finish!",command=Quit, fg='red',bg="#a4a8a5",font =("Courier",10))
qbutton.grid(row = 10, columnspan = 2,pady = 5, padx = 11)

students = []

mGui.mainloop()

                                                  
