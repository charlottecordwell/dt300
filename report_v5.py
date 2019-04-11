#------------------------------------------
# Authour: Charlotte Cordwell
#
# Name: Report Generator
# File Name: report_v5
#
# Purpose: Generates a report for year 13 students
# Version : #5
#
# Changes 
# -  Added PEP 8 comapliance
# - Added validation for fn, ln
# - 
# - 
# Creation Date: 8/4/19
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
      def __init__(self, fn, ln, student_no, background_c, \
                   constructive_c, classwork_c, paragraph):
            
            self.fn = fn.capitalize()
            self.ln = ln.capitalize()
            self.student_no = student_no
            self.background_c = background_c
            self.constructive_c = constructive_c
            self.classwork_c = classwork_c
            self.paragraph = paragraph
            
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
      
      def get_paragraph(self):
            return self.paragraph

def validate ():
      #validation for duplicate student number, this does not check against csv file
      try:
            number = int(student_no.get())
      except ValueError:
            tkinter.messagebox.showwarning("Warning!",\
                                           "Please enter numeric student number.")

      no_duplicate = True #validates for duplicate student numbers
      for i in range(0, len(student_nos)):
            if int(student_no.get()) == student_nos[i]:
                  no_duplicate = False
       # input error messages           
      if len(fn.get()) < 1 or len(ln.get()) < 1: 
            tkinter.messagebox.showwarning("Warning!",\
                                           "Please enter a value for all fields")
      elif not (fn.get().isalpha()) or not (ln.get().isalpha()):
            tkinter.messagebox.showwarning("Warning!",\
                                           "Please enter a name with no symbols, spaces or numbers.")
            #this will do the same for hyphenated names and names with apostrophes, unfortunately.
      elif len(student_no.get()) > 5 or len(student_no.get()) <5:
            tkinter.messagebox.showwarning("Warning!",\
                                           "Please put in a student number that is 5 digits.")
      elif len(fn.get()) > 30 or len(ln.get()) > 30:
            tkinter.messagebox.showwarning("Warning!",\
                                           "Please put in a first or last name with less than 30 characters.")
      elif no_duplicate == False:
            tkinter.messagebox.showwarning("Warning","Duplicate Student number")      

      else:
            processdata() #runs if all of the validation above is passed.
            

def processdata():             
      #putting validated variables into other ones to append to csv
      ufn = fn.get().capitalize()
      uln = ln.get().capitalize()
      ustudent_no = int(student_no.get())
      uback = background_c.get()
      uconstructive = constructive_c.get()
      uclasswork = classwork_c.get()
      
      paragraph = ("%s is %s Some thing to work on is that %s %s %s")\
                  %(ufn, uback, uconstructive, ufn, uclasswork)
      print(paragraph) # testing
      
      student_nos.append(ustudent_no)
      print(student_nos)
      tkinter.messagebox.showinfo("Notice","Submission Sucessful")
      #testing purposes only

      """
      print(ufn)
      print(uln)
      print(ustudent_no)
      print(uback)
      print(uconstructive)
      print(uclasswork)
      """
      #put the values into students list, this then gets added to csv
      students.append(Report(ufn, uln, ustudent_no, uback,\
                             uconstructive, uclasswork, paragraph))
      print(students)#testing

      #clearing entry fields to inidcate that values have been submitted
      fnEntry.delete(0,END)
      fnEntry.insert(20,"noname")
      lnEntry.delete(0,END)
      lnEntry.insert(20,"noname")
      student_noEntry.delete(0,END)
      student_noEntry.insert(10, "#####")
          

def writetocsv():
      import csv
      file_name = "student_report.csv"
      ofile = open(file_name, "w") #'w' for testing purposes
      writer = csv.writer(ofile, delimiter=',',lineterminator='\n')
      #cycles through list of records
      for i in range (0, len (students)):
            #the following code is used for debugging purposes
            """
            print(students[i].fn)
            print(students[i].ln)
            print(students[i].student_no)
            print(students[i].background_c)
            print(students[i].constructive_c)
            print(students[i].classwork_c)
            """
            writer.writerow([students[i].fn, students[i].ln, students[i].student_no,\
                             students[i].background_c, students[i].constructive_c,\
                             students[i].classwork_c, students[i].paragraph])
            tkinter.messagebox.showinfo("Notice","Write to CSV sucessful.")
      ofile.close()
      
def Quit():
    mExit = tkinter.messagebox.askokcancel(title = "Quit",\
                                           message = "Are you sure?")
    print(mExit)
    if mExit > 0: #1 is True 0 is False
        mGui.destroy()
    return

#### GUI
student_nos = []
mGui = Tk()
students = [] #this is where objects of students will be.

#variable types that are used by tkinter
fn = StringVar()
ln = StringVar()
student_no = StringVar()

BACKGROUND = ["an excellent student.", " a good student.",\
              " a struggling student."]
#there are no capitals ^ as these will be put into a sentence,
#this is the same ith the other lists.
background_c = StringVar()
background_c.set(BACKGROUND[0])
#makes the drop down list all entrys in the BACKGROUND list 

CONSTRUCTIVE = ["when work load increases she needs to manage her time.",\
                "she needs to be more attentive in class.",\
                "she needs to come to class."]
constructive_c = StringVar()
constructive_c.set(CONSTRUCTIVE[0])

CLASS_WORK = ["completes work to a high standard.",\
              "completes Work.", "does not do assgined work."]
classwork_c = StringVar()
classwork_c.set(CLASS_WORK[0])

#primary window
mGui.geometry("600x500")
mGui.title("Report Generator")
mGui.configure(background = "#fcedd1")

#Simple label used for header
mlabel = Label(mGui, text = "Year 13 Report Generator",\
               fg ="#383123",bg ="#fcedd1", font =("Courier",24))
mlabel.grid(row = 0, columnspan = 2)

#data entry label and Entry field for text and integer. 
#note the text variables as name and gae as declared above
fnEntryl = Label(mGui, text = "First Name:",\
                 fg = "#383123", bg = "#fcedd1", font = ("Courier",12,"bold"))
fnEntryl.grid(row = 1, column = 0, sticky = W, padx = 5,pady = 5)
fnEntry = Entry(mGui, textvariable = fn)
fnEntry.insert(10, "FirstName")
fnEntry.grid(row = 1, column = 1, sticky = EW, pady = 5)

#last name field
lnEntryl = Label(mGui, text = "Last Name:",\
                 fg = "#383123", bg = "#fcedd1", font = ("Courier",12,"bold"))
lnEntryl.grid(row = 2, column = 0,sticky = W, padx = 5,pady = 5)
lnEntry = Entry(mGui, textvariable = ln)
lnEntry.insert(50, "LastName")
lnEntry.grid(row=2, column = 1, sticky = EW, pady = 5)

#student number field
student_noEntryl = Label(mGui, text='Student Number:',\
                         fg='#383123',bg='#fcedd1',font =("Courier",12,"bold"))
student_noEntryl.grid(row = 3, column = 0,sticky = W, padx = 5, pady = 5)
student_noEntry = Entry(mGui, textvariable = student_no)
student_noEntry.insert(10, "#####")
student_noEntry.grid(row = 3, column = 1, sticky = EW, pady = 5)

#comments label
mlabel = Label(mGui, text = "Please choose comments.",\
               fg = "#383123", bg = "#fcedd1", font =("Courier",18))
mlabel.grid(row = 4, columnspan = 2)

#background comment field
background_cEntry1 = Label(mGui, text = "Background Comment:",\
                           fg = "#383123", bg = "#fcedd1", font = ("Courier",12,"bold"))
background_cEntry1.grid(row = 5, column = 0, sticky = W, padx = 5, pady = 5)
background_cEntry= OptionMenu(mGui, background_c, *BACKGROUND)
background_cEntry.config(width = 50)
#^ makes this whole column 1 stay at 50 px wide.
background_cEntry.grid(row = 5, column = 1, sticky = EW, pady = 5)

# constructive comment field
constructive_cEntry1 = Label(mGui, text = "Constructive Comment:",\
                             fg = "#383123", bg = "#fcedd1", font = ("Courier",12,"bold"))
constructive_cEntry1.grid(row = 6, column = 0, sticky = W, padx = 5,pady = 5)
constructive_cEntry= OptionMenu(mGui, constructive_c, *CONSTRUCTIVE)
constructive_cEntry.grid(row = 6, column = 1, sticky = EW, pady = 5)

#class work comment field
classwork_cEntry1 = Label(mGui, text = "Class Work Comment:",\
                          fg = "#383123", bg = "#fcedd1", font = ("Courier",12,"bold"))
classwork_cEntry1.grid(row = 7, column = 0, sticky = W, padx = 5, pady = 5)
classwork_cEntry= OptionMenu(mGui, classwork_c,  *CLASS_WORK)
classwork_cEntry.grid(row = 7, column = 1, sticky = EW, pady = 5 )      

#Submit data
mbutton = Button(mGui, text = "Validate and Submit Entries",\
                 command = validate, fg = "black")
mbutton.grid(row = 8, column = 1, pady = 5)

#write to csv
qbutton = Button(mGui, text = "Write to CSV",\
                 command = writetocsv, fg = "black", font =("Courier",10))
qbutton.grid(row = 9, columnspan = 2, pady = 10, padx = 11, ipadx = 10)

#QUIT button ie event to quit
qbutton = Button(mGui, text = "Quit",\
                 command = Quit, fg = "red", font =("Courier",15))
qbutton.grid(row = 10, columnspan = 2, pady = 5, padx = 11, ipadx = 30)

mGui.mainloop()

                                                  
