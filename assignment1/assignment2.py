#Assignment 2:

#student_list = ["Anil", "Mayur", "Priyanka", "Hardik", "Maulik", "Sunil"]

student_list = ["Anil", "Mayur", "Priyanka", "Hardik", "Maulik", "Sunil"]

#1. Print a list of all students
print "print all student list :-",student_list

#2. How many students are there in list?
print "total no of student in list :-",len(student_list)

#3. Add a new student "Jatin" in end of the list
student_list.append( 'Jatin' );
print "Updated List : ", student_list

#4. Get list of all students between "Mayur" and "Maulik" in list
print "student list between Mayur and Maulik :-",student_list[1:5]

#5. Replace student "Hardik" to "Sameer" in list
student_list[3] = "Sameer"
print "after replace... student List is :-",student_list