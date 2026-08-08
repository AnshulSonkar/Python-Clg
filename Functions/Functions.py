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
# def factorial
# def factorial(n):

#     f=1

#     for i in range(1,n+1):
#         f*=i

#     return f

# print(factorial(6))
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
