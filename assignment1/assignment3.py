#Assignment 3:

#student_detail_dict = {'Name': 'Rajan', 'Age': 8, 'Class': 'First'}
student_detail_dict = {'Name': 'Rajan', 'Age': 8, 'Class': 'First'}

print student_detail_dict

#1. Get a value of key 'Age'
print "student Detail Dictionary :-",student_detail_dict['Age']

#2. Add a new key value pair "City": "Gandhinagar"
student_detail_dict["city"] = "Gandhinagar"
print "after adding new key value pair :-",student_detail_dict

#3. Update value of key 'Age' : 10
student_detail_dict["Age"] = 10
print "after updating the value of key 'Age' : 10 :-",student_detail_dict

#4. Get list of all keys from dictionary
print "print all the value of keys :-",student_detail_dict.keys()

#5. Get list of all values from dictionary
print "print all the keys of values :-",student_detail_dict.values()

#6. remove entry with key 'Class'
del student_detail_dict['Class'];
print "After remove the key 'class' dictionary is :- ",student_detail_dict

