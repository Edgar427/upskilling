student = {"name" : "John", "age": 25, "courses": ["Math", "CompSci"] }

#print(student["courses"]) # to get value of 1 key
#print(student.get("phone", "Not found")) #to get value but also to not give an error when the key does not exist
#print(student.get("name")) to get value 


#Adding key and value
#student["phone"] = "555-5555"
#student["phone"] = "555-676767" if key already exists will update value
#print(student.get("phone", "Not found"))

#Updating dict
#student.update({"name":"Jane", "age": 26 , "phone" : "5555-1212" }) both updates and add new keys
#print(student)

#deleting keys
#del student["age"] will delete age
#age = student.pop("age") #will return age when print
#print(age)
#print(student)

#dict methods
#print(len(student)) will return number of keys
#print(student.keys()) will give all the keys of the dict
#print(student.values()) will give all of the values of the dict
#print(student.items()) will see both key and value pair

#Looping
#for key, value in student.items():
#    print(key, value)