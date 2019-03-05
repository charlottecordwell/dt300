#-----------------------------------ui
#Authour : Charlotte Cordwell
#Name: school_class
#Purpose: Oragize and use data for
#        schools to produce an input

class School:
    
    def __init__(self, school_name, roll_size, num_classrooms):
        
        self.school_name= school_name
        self.roll_size= roll_size
        self.num_classrooms =num_classrooms
        
    def get_average(self):
        average = round(self.roll_size/self.num_classrooms,1)
        return average
    
    def show_info(self):
        print("School:",self.school_name,"Average students per class:",self.get_average())
        

 #gets a number for anything with validation
def get_num(prompt,error,border):
    choice = border
    while choice <= border:
        try:
            choice = int(input(prompt))
        except ValueError:
            print(error)
    return choice

#gets the data for the school
def get_values():
    
    global school_name
    global roll_size
    global num_classrooms
    
    school_name = input("What is the school's name?")
    
    roll_size = get_num("How many students are there?","Please put in a number greater than -1", -1)
    
    num_classrooms = get_num("How many classrooms are there?","Please put in a number greater than 0",0)
    

#main
                                
get_values()
school1= School(school_name,roll_size, num_classrooms)

school1.show_info()
        
        
        
        
