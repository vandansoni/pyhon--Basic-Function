#2) Take a student's percentage dictionary, say for example this one:
Student_Marks = {"pragnesh": 90, "jayesh": 80, "sohel": 79, "Hardik": 81, "Rajan":100}
print "Students Marks is",Student_Marks
Grades={}
for key,value in Student_Marks.items():
    if value>90:
        Grades.update({key : 'A'})
    elif value>80 and value<=90:
        Grades.update({key : 'B'})
    elif value>70 and value<=80:
        Grades.update({key : 'C'})
    else:
        Grades.update({key : 'D'})
print "Grades : ",Grades
