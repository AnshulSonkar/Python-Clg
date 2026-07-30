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
# 
# 
# print(students["101"]["name"])
# 
# 
# Merge Dictionaries
# d1 = {"a":1}
# d2 = {"b":2}

# d3 = d1 | d2

# print(d3)
# 
# 
# Practise 
# 1 . Create Dictionary
# d = {"name":"Anshul","age":20}
# print(d)
# 
# 
# Access Values 
# d = {"name":"Anshul"}
# print(d["name"])
# 
# 
# Using get()
# d = {"age":20}
# print(d.get("age"))
# 
# 
# Add key
# d = {}
# d["city"] = "Bhopal"
# print(d)
# 
# 
# 5.Update value
# d = {"age":20}
# d["age"] = 21
# print(d)
# 
# 
# 6.Delete using pop()
# d = {"a":1,"b":2}
# d.pop("a")
# print(d)
# 
# 
# 7. Delete using del
# d = {"a":1,"b":2}
# del d["b"]
# print(d)
# 
# 
# 8. clear Dictionary
# d = {"a":1}
# d.clear()
# print(d)
# 
# 
# copy
# d = {"a":1}
# x = d.copy()
# print(x)
# 
# 
# length
# d = {"a":1,"b":2}
# print(len(d))