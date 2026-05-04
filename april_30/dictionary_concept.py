#DICTIONARY

student={
    "name":"tanuja",
    "age":18,
    "course":"python"
}

print(student)

print(student["name"])
print(student["course"])

#Add new key value pair

student["city"]="vijayawada"
print(student)

#update the data
student["age"]=21
print(student)

del student["city"]
print(student)

#keys iteration
for key in student.keys():
    print(key)

#values iteration
for value in student.values():
    print(value)

#loop through key value pairs
for key,value in student.items():
    print(key,value)