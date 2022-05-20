#an objetc is an actual student
#so student 1 is a student object
from classes_obj import student


student1 = student('Jim', 'Business', 3.1, False)
student2 = student('Jane', 'Arts', 2.0, True)



#will print out the student's name
print(student1.name)
#will print out the student's gps
print(student1.gpa)