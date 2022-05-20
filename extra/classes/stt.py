from classes_obj import stud

numb = input('How many students are? ')

quest = [
    'Name: \n',
    '\nMajor: \n',
    '\nGPA: \n',
    '\nIs on probation: \n',
]

student = [
    stud(quest[0],quest[1],quest[2],quest[3])
]

try:
    numb = int(numb)
    print('floatok')
    for stu in range(numb):
        name = input(student.name)
        major = input(student.major)
        gpa = input(student.gpa)
        gpa = float(gpa)
        is_on_probation = input(student.is_on_probation)
    print()





except:
    print('Invalid')
    quit()