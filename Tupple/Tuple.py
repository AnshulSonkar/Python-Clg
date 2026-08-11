# t = (10, 20, 30)

# print(t)


# t = tuple([1,2,3])
# print(t)


# t = (10)

# print(type(t))


# Empty Tuple
# t = ()

# print(type(t))


# Single element
# t = (10)

# print(type(t))


# 
# t = (10,)
# print(type(t))


# 
# t = (10,)

# print(type(t))


# 
# t = (5,10,15,20)

# print(t[0])
# print(t[2])


# Acessing Elements
# t = (5,10,15,20)

# print(t[-1])
# print(t[-2])


# Negative Indexing
# t = (5,10,15,20)

# print(t[-1])
# print(t[-2])


# Slicing
# t = (1,2,3,4,5,6)

# print(t[1:5])
# print(t[:4])
# print(t[3:])
# print(t[::-1])


# Tuple Functions
# 1. len()
# t = (10,20,30,40)

# print(len(t))


# 2. max()
# t = (15,80,22,9)

# print(max(t))


# 3. min()
# t = (15,80,22,9)

# print(min(t))


# 4. sum()
# t = (1,2,3,4)

# print(sum(t))


# 5. Count()
# t = (10,20,10,30,10,10)

# print(t.count(10))


# 6. Index()
# t = (5,8,2,9)

# print(t.index(2))


# 7. Tuple
# lst = [1,2,3]

# t = tuple(lst)

# print(t)


# 8. Sorted
# t = (8,3,5,1)

# print(sorted(t))


# 9. Any()
# t = (0,0,5)

# print(any(t))


# 10. all()
# t = (1,2,3)

# print(all(t))


# Tuple Packing
# student = ("Anshul",20,"Bhopal")

# print(student)


# Tuple unpacking
# name, age, city = ("Anshul",20,"Bhopal")

# print(name)
# print(age)
# print(city) 


# Swapping variables
# a = 10
# b = 20

# a,b = b,a

# print(a,b)


# Membership
# t = (10,20,30)

# print(20 in t)
# print(50 in t)


# Looping
# t = (1,2,3,4)

# for i in t:
#     print(i)


# Nested Loop
# t = ((1,2),(3,4),(5,6))

# print(t[1])
# print(t[2][1])


# Concatenation
# t1 = (1,2)

# t2 = (3,4)

# t3 = (5,6)

# print(t1+t2+t3)


# Repetition
# t = (1,2)

# print(t*3)


# Convert tuple to list
# t = (1,2,3)

# lst = list(t)

# print(lst)


# Convert list to tuple
# lst = [10,20,30]

# t = tuple(lst)

# print(t)


# Tuple are immutable 
# t = (1,2,3)

# lst = list(t)

# lst[1]=100

# t = tuple(lst)

# print(t)


# Print All Elements
# t=(10,20,30)

# for i in t:
#     print(i)


# Find Maximum
# t=(3,7,2,9)

# print(max(t))
# 
# 
# Find minimum
# t=(3,7,2,9)

# print(min(t))
# 
# 
# Find Sum
# t=(1,2,3,4)

# print(sum(t))
# 
# 
# Reverse tuple 
# t=(1,2,3,4)

# print(t[::-1])
# 
# 
# Count Occurence
# t=(1,2,1,1,3)

# print(t.count(1))
# 
# 
# Find Index 
# t=(8,4,7)

# print(t.index(4))
# 
# 
# Check member 
# t=(10,20,30)

# print(40 in t)
# 
# 
# Tuple length
# t=(1,2,3)

# print(len(t))
# 
# 
# Multiply Tuple
# t=(5,)

# print(t*5)
# 
# 
# Join tuples
# t1=(1,2)

# t2=(3,4)

# print(t1+t2)
# 
# 
# Unpacking 
# a,b,c=(5,10,15)

# print(a,b,c)
# 
# 
# Swap Values
# a,b=100,200

# a,b=b,a

# print(a,b)
# 
# 
# Convert list
# lst=[1,2,3]

# print(tuple(lst))
# 
# 
# Convert Tuple
# t=(1,2,3)

# print(list(t))
# 
# 
# Sort tuple
# t=(8,2,9)

# print(sorted(t))
# 
# 
# Nested Tuple
# t=((1,2),(3,4))

# print(t[0][1])
# 
# 
# Largest using loop
# t=((1,2),(3,4))

# print(t[0][1])
# 
# 
# Smallest using Loop
# t=(2,8,4,10)

# smallest=t[0]

# for i in t:
#     if i<smallest:
#         smallest=i

# print(smallest)
# 
# 
# Average
# t=(10,20,30,40)

# print(sum(t)/len(t))
# 
# 
# Quick quiz
# a = (100)
# b = (100,)
# c = 100,
# d = ()

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# 
# 
# Pyhton map()
# 1. What is map()?
# map() is used to apply a function to every element of an iterable such as a list, tuple, etc.
# without map()
# lst = [1, 2, 3, 4, 5]

# result = []

# for x in lst:
#     result.append(x * x)

# print(result)
# 
# 
# Using map()
# lst = [1, 2, 3, 4, 5]

# result = map(lambda x: x * x, lst)

# print(list(result))
# 
# 
# 3.
# map() with normal function
# def square(x):
#     return x * x

# lst = [1, 2, 3, 4, 5]

# result = map(square, lst)

# print(list(result))
# 
# 
# 4.
# map() with lambda
# lst = [10, 20, 30, 40]

# result = map(lambda x: x + 5, lst)

# print(list(result))
# 
# 
# 5.
# Double every number
# lst = [1, 2, 3, 4, 5]

# result = map(lambda x: x * 2, lst)

# print(list(result))
# 
# 
# 6.
# Triple every number
# lst = [1, 2, 3, 4]

# result = map(lambda x: x * 3, lst)

# print(list(result))
# 
# 
# 7.
# Add 10 to every number
# lst = [5, 10, 15, 20]

# result = map(lambda x: x + 10, lst)

# print(list(result))
# 
# 
# 8.
# Subtract 5
# lst = [10, 20, 30, 40]

# result = map(lambda x: x - 5, lst)

# print(list(result))
# 
# 
# 9.
# Convert number to string
# lst = [10, 20, 30, 40]

# result = map(str, lst)

# print(list(result))






