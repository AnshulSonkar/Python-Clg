# print("hello world")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# sum = a + b

# print("Sum =", sum)


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# a = 5
# b = 10

# temp = a
# a = b
# b = temp

# print("a =", a)
# print("b =", b)


# fizzbuzz example
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


num = int(input("Enter a number: "))

even_count = 0
odd_count = 0

for i in range(1, num + 1):
    if num % i == 0:   # check factor
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("Even factors:", even_count)
print("Odd factors:", odd_count)










