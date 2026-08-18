# De
# What is a Function?
# A function is a block of reusable code that performs a specific task.
# Instead of writing the same code again and again, you write it once and call it whenever needed.
# 
# 
# Syntax
# def function_name():
# EXample simple Function
# def greet():
#     print("Hello Everyone!")

# greet()
# 
# 
# Example 2
# def welcome():
#     print("Welcome to Python")

# welcome()
# welcome()
# welcome()
# 
# 
# Example 3 
# def greet(name):
#     print("Hello", name)

# greet("Anshul")
# greet("Rahul")
# 
# 
# Example 4 : function with 2 parameter
# def add(a, b):
#     print(a + b)

# add(10, 20)
# add(50, 30)
# 
# 
# Exapmle 5
# def add(a, b):
#     return a + b

# x = add(10, 20)

# print(x)
# 
# 
# Ex. 6 Square of numbers 
# def square(n):
#     return n * n

# print(square(5))
# 
#
# Ex. 7 
# Even or odd 
# def evenOdd(n):
#     if n % 2 == 0:
#         return "Even"
#     return "Odd"

# print(evenOdd(12))
# 
# 
# Ex. Largest number 
# def largest(a, b):
#     if a > b:
#         return a
#     return b

# print(largest(100, 50))
# 
# 
# Ex. 9
# Factorial
# def factorial(n):
#     fact = 1

#     for i in range(1, n + 1):
#         fact *= i

#     return fact

# print(factorial(5))
# 
# 
# Ex. 10
# Reverse String
# def reverse(text):
#     return text[::-1]

# print(reverse("Python"))
# 
# 
# Ex. 11
# Check Palindrome
# def palindrome(text):
#     return text == text[::-1]

# print(palindrome("madam"))
# 
# 
# Ex. 12 
# Count vowels 
# def vowels(text):
#     count = 0

#     for ch in text.lower():
#         if ch in "aeiou":
#             count += 1

#     return count

# print(vowels("Programming"))
# 
# 
# Types of Arguments
# 1.
# Positional Argumensts
# def student(name, age):
#     print(name, age)

# student("Anshul", 20)
# 
# 
# 2.
# keyword Arguments
# def student(name, age):
#     print(name, age)

# student(age=20, name="Anshul")
# 
# 
# 3.
# def greet(name="Guest"):
#     print("Hello", name)

# greet()
# greet("Rahul")
# 
# 
# 4.
#  Variable Length Arguments
# def total(*numbers):
#     print(sum(numbers))

# total(1,2,3)
# total(10,20,30,40)
# 
# 
# 5.
# Keyword Variable Argument
# def student(**data):
#     print(data)

# student(name="Anshul", age=20)
# 
# 
# Loacal Variable 
# def fun():
#     x = 10
#     print(x)

# fun()
# 
# 
# Global variable
# x = 100

# def fun():
#     print(x)

# fun()
# 
# 
# Using global 
# x = 10

# def change():
#     global x
#     x = 50

# change()

# print(x)
# 
# 
# Nested Function
# def outer():

#     def inner():
#         print("Inner Function")

#     inner()

# outer()
# 
# 
# Recursive Function
# def fact(n):

#     if n == 1:
#         return 1

#     return n * fact(n-1)

# print(fact(5))
# 
# 
# Lambda Functions
# square = lambda x: x*x

# print(square(5))
# 
# 
# Practise codes
# 1.
# def hello():
#     print("Hello")

# hello()
# 
# 
# 
# 
# 2.
# Add
# def add(a,b):
#     return a+b

# print(add(5,10))
# 
# 
# 3.
# Subtract
# def sub(a,b):
#     return a-b

# print(sub(10,5))
# 
# 
# 4.
# def mul(a,b):
#     return a*b

# print(mul(4,6))
# 
# 
# 5.
# Divide
# def div(a,b):
#     return a/b

# print(div(20,4))
# 
# 
# 6.
# Square
# def square(x):
#     return x*x

# print(square(8))
# 
# 
# 7.
# Cube
# def cube(x):
#     return x*x*x

# print(cube(3))
# 
# 
# 8.
# Maximum
# def maximum(a,b):
#     return max(a,b)

# print(maximum(10,50))
# 
# 
# 9.
# Minimum
# def minimum(a,b):
#     return min(a,b)

# print(minimum(10,50))
# 
# 
# 10.
# def length
# def length(text):
#     return len(text)

# print(length("Python"))
# 
# 
# 11.
# Even Check
# def even(n):
#     return n%2==0

# print(even(20))
# 
# 
# 12.
# Odd check
# def odd(n):
#     return n%2!=0
# 
# print(odd(15))
# 
# 
# 13.
# Reverse text
# def reverse(text):
#     return text[::-1]

# print(reverse("Hello"))
# 
# 
# 14.
# def Palindrome
# def palindrome(text):
#     return text==text[::-1]

# print(palindrome("madam"))
# 
# 
# 15.
# def power
# def power(a,b):
#     return a**b

# print(power(2,5))
# 
# 
# 16.
# def average
# def average(a,b,c):
#     return (a+b+c)/3

# print(average(10,20,30))
# 
# 
# 17.
# def factorial
# def factorial(n):

#     f=1

#     for i in range(1,n+1):
#         f*=i

#     return f

# print(factorial(6))
# 
# 
# 18.
# def vowelCount(text):

#     count=0

#     for ch in text.lower():
#         if ch in "aeiou":
#             count+=1

#     return count

# print(vowelCount("Education"))
# 
# 
# 19.
# VowelCount
# def vowelCount(text):

#     count=0

#     for ch in text.lower():
#         if ch in "aeiou":
#             count+=1

#     return count

# print(vowelCount("Education"))
# 
# 
# 20.
# Largest
# def largest(lst):
#     return max(lst)

# print(largest([5,8,10,1]))
# 
# 
# 21.
# Smallest
# def smallest(lst):
#     return min(lst)

# print(smallest([5,8,10,1]))
# 
# 
# 22.
# def total
# def total(lst):
#     return sum(lst)

# print(total([1,2,3,4]))
# 
# 
# 23.
# def unique
# def unique(lst):
#     return list(set(lst))

# print(unique([1,2,2,3,4]))
# 
# 
# 24.
# Student info
# def student(name,age):
#     print(name,age)

# student("Anshul",20)
# 
# 
# 25.
# def greet
# def greet(name="Guest"):
#     print("Hello",name)

# greet()
# 
# 
# 26.
# def args
# 
# 
# Next Topic
# Lambda Functions 
# 🐍 Python Lambda Functions — Complete Guide
# 1. What is a Lambda Function?
# A lambda function is a small anonymous function written in one line.
# 
# 
# Lambda equivalent
# square = lambda x: x * x

# print(square(5))
# 
# 
# 2.
# Lambda with one argument
# square = lambda x: x * x

# print(square(6))
# 
# 
# 3.
# Lambda with two argument 
# add = lambda a, b: a + b

# print(add(10, 20))
# 
# 
# 4.
# Lambda with 3 argument
# multiply = lambda a, b, c: a * b * c

# print(multiply(2, 3, 4))
# 
# 
# 5.
# Lambda for even/odd
# even = lambda x: x % 2 == 0

# print(even(10))
# print(even(7))
# 
# 
# 6.
# Lmabda for positive/negative
# positive = lambda x: x > 0

# print(positive(10))
# print(positive(-5))
# 
# 
# 7.
# Lambda with conditional Expression 
# check = lambda x: "Even" if x % 2 == 0 else "Odd"

# print(check(10))
# print(check(7))
# 
# 
# 8.
# Lambda for largest of two
# largest = lambda a, b: a if a > b else b

# print(largest(10, 25))
# 
# 
# 9.
# Lambda for smallest
# smallest = lambda a, b: a if a < b else b

# print(smallest(10, 25))
# 
# 
# 10.
# Lambda with String 
# length = lambda text: len(text)

# print(length("Python"))
# 
# 
# 11.
# Lambda to reverse string
# reverse = lambda text: text[::-1]

# print(reverse("Python"))
# 
# 
# 12.
# Lambda for Palindrome 
# palindrome = lambda text: text == text[::-1]

# print(palindrome("madam"))
# print(palindrome("python"))
# 
# 
# 13.
# Lambda with list 
# square = lambda x: x * x

# lst = [1, 2, 3, 4, 5]

# for i in lst:
#     print(square(i))
# 
# 
# 14.
# Lambda + map()
# lst = [1, 2, 3, 4, 5]

# result = map(lambda x: x * x, lst)

# print(list(result))
# 
# 
# without Lambda
# def square(x):
#     return x * x

# lst = [1, 2, 3, 4, 5]

# result = map(square, lst)

# print(list(result))
# 
# 
# 15.
# Lambda + filter()
# lst = [1, 2, 3, 4, 5, 6]

# result = filter(lambda x: x % 2 == 0, lst)

# print(list(result))
# 
# 
# 16.
# filter odd numbers
# lst = [1, 2, 3, 4, 5, 6, 7]

# result = filter(lambda x: x % 2 != 0, lst)

# print(list(result))
# 
# 
# 17.
# Lambda with sorted()
# sort by marks
# students = [
#     ("Rahul", 85),
#     ("Amit", 92),
#     ("Anshul", 78)
# ]

# students.sort(key=lambda x: x[1])

# print(students)
# 
# 
# 18.
# Sort in descending order
# students = [
#     ("Rahul", 85),
#     ("Amit", 92),
#     ("Anshul", 78)
# ]

# students.sort(key=lambda x: x[1], reverse=True)

# print(students)
# 
# 
# 19.
# Sort Strings by length
# words = ["python", "java", "c", "javascript"]

# words.sort(key=lambda x: len(x))

# print(words)
# 
# 
# 20.
# Sort Dictionary by Values
# marks = {
#     "Rahul": 85,
#     "Amit": 92,
#     "Anshul": 78
# }

# result = sorted(marks.items(), key=lambda x: x[1])

# print(result)
# 
# 
# 21. 
# Lambda + reduce()
# from functools import reduce

# lst = [1, 2, 3, 4]

# result = reduce(lambda a, b: a + b, lst)

# print(result)
# 
# 
# 22.
# Product of list 
# from functools import reduce

# lst = [1, 2, 3, 4, 5]

# result = reduce(lambda a, b: a * b, lst)

# print(result)
# 
# 
# 23.
# Lambda + map() + filter() 
# lst = [1, 2, 3, 4, 5, 6]

# even = filter(lambda x: x % 2 == 0, lst)

# square = map(lambda x: x * x, even)

# print(list(square))
# 
# 
# 24.
# Lambda with max()
# 
# 
# students = [
#     ("Rahul", 85),
#     ("Amit", 92),
#     ("Anshul", 78)
# ]

# result = max(students, key=lambda x: x[1])

# print(result)
# 
# 
# 25.
# Lambda with min()
# students = [
#     ("Rahul", 85),
#     ("Amit", 92),
#     ("Anshul", 78)
# ]

# result = min(students, key=lambda x: x[1])

# print(result)
# 
# 
# 26.
# Lambda with dictionary
# d = {
#     "a": 10,
#     "b": 30,
#     "c": 20
# }

# result = max(d, key=lambda x: d[x])

# print(result)
# 
# 
# 27.
# Lambda with list of dictionary
# students = [
#     {"name": "Rahul", "marks": 85},
#     {"name": "Amit", "marks": 92},
#     {"name": "Anshul", "marks": 78}
# ]

# students.sort(key=lambda x: x["marks"])

# print(students)
# 
# 
# 28.
# Multiple condition
# check = lambda x: "Positive Even" if x > 0 and x % 2 == 0 else "Other"

# print(check(10))
# print(check(-5))
# 
# 
# 29.
# Lambda returning a tuple
# operation = lambda a, b: (a + b, a - b, a * b)

# print(operation(10, 5))
# 
# 
# 30.
# Lambda Factory
# def multiplier(n):
#     return lambda x: x * n

# double = multiplier(2)
# triple = multiplier(3)

# print(double(10))
# print(triple(10))
# 
# 
# Pyhton map()
# 1. What is map()?
# map() is used to apply a function to every element of an iterable such as a list, tuple, etc.
# 
# 
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
# 
# 
# 10.
#  Convert Strings to Integers
# lst = ["10", "20", "30", "40"]

# result = map(int, lst)

# print(list(result))
# 
# 
# 11.
# Convert Strings to upppercase
# words = ["python", "java", "c++"]

# result = map(str.upper, words)

# print(list(result))
# 
# 
# 12.
# Convert Strings to lowercase
# words = ["PYTHON", "JAVA", "C++"]

# result = map(str.lower, words)

# print(list(result))
# 
# 
# 13.
#  Find length of every String
# words = ["cat", "python", "java", "javascript"]

# result = map(len, words)

# print(list(result))
# 
# 
# 14.
# Convert Celsius to Fahrenheit
# celsius = [0, 10, 20, 30, 40]

# result = map(lambda c: (c * 9/5) + 32, celsius)

# print(list(result))
# 
# 
# 15.
# Even or Odd
# lst = [1, 2, 3, 4, 5]

# result = map(
#     lambda x: "Even" if x % 2 == 0 else "Odd",
#     lst
# )

# print(list(result))
# 
# 
# 16.
# Positive or negative
# lst = [-5, 10, -2, 7, 0]

# result = map(
#     lambda x: "Positive" if x > 0 else "Negative",
#     lst
# )

# print(list(result))
# 
# 
# Better version
# lst = [-5, 10, -2, 7, 0]

# result = map(
#     lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero",
#     lst
# )

# print(list(result))
# 
# 
# 17.
#  Add two list
# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]

# result = map(lambda x, y: x + y, a, b)

# print(list(result))
# 
# 
# 18.
# Multiply two list
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]

# result = map(lambda x, y: x * y, a, b)

# print(list(result))
# 
# 
# 19.
# Add three lists 
# a = [1, 2, 3]
# b = [10, 20, 30]
# c = [100, 200, 300]

# result = map(lambda x, y, z: x + y + z, a, b, c)

# print(list(result))
# 
# 
# 20.
# map() with tuple
# t = (1, 2, 3, 4)

# result = map(lambda x: x * 10, t)

# print(tuple(result))
# 
# 
# New topic
# filter()
# filter is used to remove those elements from the collection which satisfy the given condition.
# Syntax
# filter(function, iterable)
# 
# 
# Parameters:
# function → condition check karega
# iterable → list, tuple, set, etc.
# 
# 
# 1.
# Simple Example
# numbers = [1, 2, 3, 4, 5, 6]

# def even(num):
#     return num % 2 == 0

# result = filter(even, numbers)

# print(list(result))
# 
# 
# 2.
# filter with lambda
# numbers = [1, 2, 3, 4, 5, 6]

# result = filter(lambda x: x % 2 == 0, numbers)

# print(list(result))
# 
# 
# 3.
# Odd numbers
# numbers = [1, 2, 3, 4, 5, 6, 7]

# result = filter(lambda x: x % 2 != 0, numbers)

# print(list(result))
# 
# 
# 4.
# Numbers greater than 10
# numbers = [5, 12, 8, 20, 3, 15]

# result = filter(lambda x: x > 10, numbers)

# print(list(result))
# 
# 
# 5.
# Positive numbers
# numbers = [-5, 10, -2, 8, -1, 20]

# result = filter(lambda x: x > 0, numbers)

# print(list(result))
# 
# 
# 6.
# Negative numbers
# numbers = [-5, 10, -2, 8, -1, 20]

# result = filter(lambda x: x < 0, numbers)

# print(list(result))
# 
# 
# 7.
# Filter Strings 
# names = ["Anshul", "Aman", "Raj", "Amit", "Rohit"]

# result = filter(lambda name: name.startswith("A"), names)

# print(list(result))
# 
# 
# 10.
# Srings with length














