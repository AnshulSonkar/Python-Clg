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

