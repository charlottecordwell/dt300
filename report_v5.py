# ------------------------------------------
# Authour: Charlotte Cordwell
#
# Name: Report Generator
# File Name: report_v5
#
# Purpose: Generates a report for year 13 students
# Version : #5
#
# Changes
# -  Added PEP 8 compliance
# - Added constants for validation
# - Removed  all print() that was for testing purposes
# - Added more comments for clarification
# Creation Date: 8/4/19
# -----------------------------------------


# getting GUI library
from tkinter import *
# need to espcially import this
import tkinter.messagebox


def main():
    pass
if __name__ == "__main__":
    main()


class Report:  # class for creating report objects
    def __init__(self, fn, ln, student_no, background_c,
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


def validate():
    # runs when validate/submit button is clicked
    STUDENTNO_LEN = 5
    NAMEMAX = 30
    NAMEMIN = 1
    true_int = True
    no_duplicate = True
    # validates for non-numeric student number
    try:
        istudent_no = int(student_no.get())
    except ValueError:
        true_int = False
    # validates for duplicate student numbers
    # this does not check against csv file
    for i in range(0, len(student_nos)):
        if int(istudent_no) == student_nos[i]:
            no_duplicate = False

    # input error messages
    if len(fn.get()) < NAMEMIN or len(ln.get()) < NAMEMIN:
        tkinter.messagebox.showwarning("Warning!",
        "Please enter a value for all fields")
    elif len(fn.get()) > NAMEMAX or len(ln.get()) > NAMEMAX:
        tkinter.messagebox.showwarning("Warning!",
        "Please put in a first or last name with less than 30 characters.")
    elif true_int is False or len(str(istudent_no)) > STUDENTNO_LEN \
         or len(str(istudent_no)) < STUDENTNO_LEN or istudent_no < 0:
            tkinter.messagebox.showwarning("Warning!",
            "Please enter a valid, numeric student number that is 5 digits.")
    elif no_duplicate is False:
        tkinter.messagebox.showwarning("Warning", "Duplicate student number")
    else:
        processdata()  # runs if all of the validation above is passed.
# there is no validation for symbols and numbers because names may:
# be hyphenated, have apostrophes, macrons and in some special cases, numbers.


def processdata():
    # This runs when all of the validation in processdata() is passed
    # putting validated variables into other ones to append to csv
    ufn = fn.get().capitalize()  # makes the first letter a cap
    uln = ln.get().capitalize()
    ustudent_no = int(student_no.get())
    uback = background_c.get()
    uconstructive = constructive_c.get()
    uclasswork = classwork_c.get()
    paragraph = ("%s is %s Something to work on is that %s %s %s")\
                % (ufn, uback, uconstructive, ufn, uclasswork)
    # paragraph for final rport putting together sentences
    student_nos.append(ustudent_no)
    # this is then used in validate() to check for duplicates
    tkinter.messagebox.showinfo("Notice", "Submission Sucessful")

    # put the values into students list, this then gets added to csv
    students.append(Report(ufn, uln, ustudent_no, uback,
                           uconstructive, uclasswork, paragraph))

    # clearing entry fields to inidcate that values have been submitted
    fnEntry.delete(0, END)
    fnEntry.insert(20, "noname")
    lnEntry.delete(0, END)
    lnEntry.insert(20, "noname")
    student_noEntry.delete(0, END)
    student_noEntry.insert(10, "#####")


def writetocsv():
    import csv
    file_name = "student_report.csv"
    ofile = open(file_name, "a")  # 'a' for persistence
    writer = csv.writer(ofile, delimiter=',', lineterminator='\n')
    # cycles through list of records in studentd list
    for i in range(0, len(students)):
        writer.writerow([students[i].fn, students[i].ln,
            students[i].student_no, students[i].background_c,
            students[i].constructive_c, students[i].classwork_c,
            students[i].paragraph])
    tkinter.messagebox.showinfo("Notice", "Write to CSV sucessful.")
    ofile.close()


def Quit():
    mExit = tkinter.messagebox.askokcancel(title="Quit",
                                           message="Are you sure?")
    print(mExit)
    if mExit > 0:  # 1 is Yes 0 is No
        mGui.destroy()
    return

# GUI
student_nos = []  # list to check duplicates
students = []  # this is where objects of students will be.
mGui = Tk()

# variable types that are used by tkinter
fn = StringVar()
ln = StringVar()
student_no = StringVar()

BACKGROUND = ["an excellent student.", "a good student.",
              "a struggling student."]
# there are no capitals ^ as these will be put into a sentence,
# this is the same with the other lists.
background_c = StringVar()
background_c.set(BACKGROUND[0])
# makes the drop down list all entrys in the BACKGROUND list

CONSTRUCTIVE = ["when work load increases she needs to manage her time.",
                "she needs to be more attentive in class.",
                "she needs to come to class."]
constructive_c = StringVar()
constructive_c.set(CONSTRUCTIVE[0])

CLASS_WORK = ["completes work to a high standard.",
              "completes work.", "does not do assgined work."]
classwork_c = StringVar()
classwork_c.set(CLASS_WORK[0])

# primary window
mGui.geometry("600x500")
mGui.title("Report Generator")
mGui.configure(background="#fcedd1")

# Simple label used for header
mlabel = Label(mGui, text="Year 13 Report Generator",
               fg="#383123", bg="#fcedd1", font=("Courier", 24))
mlabel.grid(row=0, columnspan=2)

# data entry label and Entry field for text and integer.
# note the text variables as name and gae as declared above
fnEntryl = Label(mGui, text="First Name:",
                 fg="#383123", bg="#fcedd1", font=("Courier", 12, "bold"))
fnEntryl.grid(row=1, column=0, sticky=W, padx=5, pady=5)
fnEntry = Entry(mGui, textvariable=fn)
fnEntry.insert(10, "FirstName")
fnEntry.grid(row=1, column=1, sticky=EW, pady=5)

# last name field
lnEntryl = Label(mGui, text="Last Name:",
                 fg="#383123", bg="#fcedd1", font=("Courier", 12, "bold"))
lnEntryl.grid(row=2, column=0, sticky=W, padx=5, pady=5)
lnEntry = Entry(mGui, textvariable=ln)
lnEntry.insert(50, "LastName")
lnEntry.grid(row=2, column=1, sticky=EW, pady=5)

# student number field
student_noEntryl = Label(mGui, text='Student Number:',
                fg="#383123", bg="#fcedd1", font=("Courier", 12, "bold"))
student_noEntryl.grid(row=3, column=0, sticky=W, padx=5, pady=5)
student_noEntry = Entry(mGui, textvariable=student_no)
student_noEntry.insert(10, "#####")
student_noEntry.grid(row=3, column=1, sticky=EW, pady=5)

# comments header
mlabel = Label(mGui, text="Please choose comments.",
               fg="#383123", bg="#fcedd1", font=("Courier", 18))
mlabel.grid(row=4, columnspan=2)

# background comment field
background_cEntry1 = Label(mGui, text="Background Comment:",
                    fg="#383123", bg="#fcedd1", font=("Courier", 12, "bold"))
background_cEntry1.grid(row=5, column=0, sticky=W, padx=5, pady=5)
background_cEntry = OptionMenu(mGui, background_c, *BACKGROUND)
background_cEntry.config(width=50)
# ^ makes this whole column 1 stay at 50 px wide.
background_cEntry.grid(row=5, column=1, sticky=EW, pady=5)

# constructive comment field
constructive_cEntry1 = Label(mGui, text="Constructive Comment:",
                    fg="#383123", bg="#fcedd1", font=("Courier", 12, "bold"))
constructive_cEntry1.grid(row=6, column=0, sticky=W, padx=5, pady=5)
constructive_cEntry = OptionMenu(mGui, constructive_c, *CONSTRUCTIVE)
constructive_cEntry.grid(row=6, column=1, sticky=EW, pady=5)

# class work comment field
classwork_cEntry1 = Label(mGui, text="Class Work Comment:",
                    fg="#383123", bg="#fcedd1", font=("Courier", 12, "bold"))
classwork_cEntry1.grid(row=7, column=0, sticky=W, padx=5, pady=5)
classwork_cEntry = OptionMenu(mGui, classwork_c,  *CLASS_WORK)
classwork_cEntry.grid(row=7, column=1, sticky=EW, pady=5)

# Validate and submit data button
mbutton = Button(mGui, text="Validate and Submit Entries",
                 command=validate, fg="black")
mbutton.grid(row=8, column=1, pady=5)

# Write to csv button
qbutton = Button(mGui, text="Write to CSV",
                 command=writetocsv, fg="black", font=("Courier", 10))
qbutton.grid(row=9, columnspan=2, pady=10, padx=11, ipadx=10)

# Quit button
qbutton = Button(mGui, text="Quit",
                command=Quit, fg="red", font=("Courier", 15))
qbutton.grid(row=10, columnspan=2, pady=5, padx=11, ipadx=30)

mGui.mainloop()  # waits for an event
