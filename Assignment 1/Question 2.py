
dog={'name':'puppy','color':'black','breed':'suzu','legs':4,'age':5}
print(dog)
student={'first_name':'Pavan', 'last_name':'Naga Sai', 'gender':'male', 'age':23,
         'martial status':'single', 'Skills':['Python','Leadership','Time Management'],
         'country':'India', 'city':'Vijayawada', 'address':'AGS TOWERS'}
print(len(student)) # len is used to print the length of the list
print("the student skills are" , student['Skills'])
print("The Data type of the Skills in student dictionary is ",type(student['Skills']))
# type is the function which is used to find the datatype of the list
student['Skills'].extend(['Java','C programming'])
# extend is the function which is used to add the multiple  values to the keys
print('the updated skills are' , student['Skills'])
keyList=list(student.keys())
print(keyList)
valueList=list(student.values()) # list is a function which is used to get the values as a list
print(valueList)
