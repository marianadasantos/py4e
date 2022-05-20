#create data types, create a class for it. define your own data type

#model a real world object, it will be a student for example
#define attributes about the thing, student
#strings, int and bool about students 
#initialize fuction: map attributes a student should have
#attributes after self 

#a class is an overview of what a student data is

class stud:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


#the values in the other file are passing through the __init__ function
#so self.name = name (so the object's name is equal to name). self.name is an attribute of student
#assign the parameters to the actual attributes. so the anme of the student's object (self.name) will be equal to the name passed on the parameter (name)