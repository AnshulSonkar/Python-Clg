# Creating a Dictionary
# Method 1
# student = {
#     "name": "Anshul",
#     "age": 20,
#     "course": "Python"
# }

# print(student)
# 
# 
# Method 2
# student = dict(name="Anshul", age=20, city="Bhopal")

# print(student)
# 
# 
# Empty Dictionary
# d = {}

# print(type(d))
# 
# 
# Accessing Values 
# Using keys
# student = {
#     "name":"Anshul",
#     "age":20
# }

# print(student["name"])
# print(student["age"])
# 
# 
# Using get()
# student = {
#     "name":"Anshul",
#     "age":20
# }

# print(student.get("name"))
# 
# 
# Adding new key 
# student = {
#     "name":"Anshul"
# }

# student["age"] = 20

# print(student)
# 
# 
# Updating value
# student = {
#     "age":20
# }

# student["age"] = 21

# print(student)
# 
# 
# Deleting item 
# pop()
# student = {
#     "name":"Anshul",
#     "age":20
# }

# student.pop("age")

# print(student)
# 
# 
# Popitem()
# student = {
#     "a":1,
#     "b":2,
#     "c":3
# }

# student.popitem()

# print(student)
# 
# 
# del
# student = {
#     "name":"Anshul",
#     "age":20
# }

# del student["age"]

# print(student)
# 
# 
# clear()
# student = {
#     "a":1,
#     "b":2
# }

# student.clear()

# print(student)
# 
# 
# copy()
# student = {
#     "name":"Anshul",
#     "age":20
# }

# new_student = student.copy()

# print(new_student)
# 
# 
# len()
# student = {
#     "a":1,
#     "b":2,
#     "c":3
# }

# print(len(student))
# 
# 
# keys()
# student = {
#     "name":"Anshul",
#     "age":20
# }

# print(student.keys())
# 
# 
# values()
# student = {
#     "name":"Anshul",
#     "age":20
# }

# print(student.values())
# 
# 
# Items()
# student = {
#     "name":"Anshul",
#     "age":20
# }

# print(student.items())
# 
# 
# update()
# student = {
#     "name":"Anshul"
# }

# student.update({"age":20})

# print(student)
# 
# 
# formkeys()
# keys = ("a","b","c")

# d = dict.fromkeys(keys,0)

# print(d)
# 
# 
# setdefault()
# student = {
#     "name":"Anshul"
# }

# student.setdefault("age",20)

# print(student)
# 
# 
# loop through dictionary
# keys()
# 
# 
# values
# for value in student.values():
#     print(value)
# 
# 
# keys and values
# for key,value in student.items():
#     print(key,value)
# 
# 
# Membership
# student = {
#     "name":"Anshul",
#     "age":20
# }

# print("name" in student)
# print("marks" in student)
# 
# 
# Nested Dictionary
# students = {
#     "101":{
#         "name":"Rahul",
#         "age":20
#     },
#     "102":{
#         "name":"Amit",
#         "age":21
#     }
# }

# print(students["101"]["name"])
# 
# 
