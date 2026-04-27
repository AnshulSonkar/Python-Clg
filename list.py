# list properties
 # 1.mutable
 # 2.Dynamic in size
 # 3. mixed data type

# list=[1,2,3,"hello",5,7]
# # print(list)
# for i in range(len(list)):
#     print(list[i],end=" ")


# # to create empty list 
# list=[]
# list1=list()
# print(list)
# print(list1)


# Creating a list with different data types
# my_list = ["apple", 42, 3.14, True]

# # Accessing items 
# print(my_list[0])  
# print(my_list[-1])

# # Slicing 
# print(my_list[1:3]) # Output: [42, 3.14]


# lst=[7, -4, -2, 9, 0, 11, 17, 8, 19, 10]
# lst.append("hello")
# lst.insert(-4,36)
# lst1=[45,46,47]
# lst.extend(lst)
# lst+=lst1
# print(lst)


# lst=[2,3,1,4,5,2,5]
# lst_sum=0
# for i in lst:
#     lst_sum+=1

#     ans=[]
#     for i in lst:
#         ans.append(lst_sum-i)

#         print(ans)
#         print(lst)


# lst=[[3,2,1,8],[50,3,7,9],[2,3,7,8]]
# # 
# ans=[]
# for i in range(len(lst)):
#     temp=lst[i].copy()
#     if i%2==0:
#         for j in range(len(temp)):
#             if temp[j]%2!=0:
#                 temp[j]+=1
#                 ans.append(temp)

#             else:
#                 for j in range(len(lst)):
#                     if temp[j]%2!=0:
#                         temp[j]+=1
#                         ans.append(temp)
#                         print(lst)
#                         print(ans)


# Delete
# lst=[1,3,5,12,14,15,23]

# del lst [4]
# print(lst)
# lst.pop(3)
# print(lst)

# lst=[1,3,5,12,14,15,23]

# x=lst.pop(2)
# print(x)
# print(lst) 


# lst = [10, 20, 30]

# x = lst.index(30)
# print(x)


# lst1 = [1, 2]
# lst2 = [3, 4]

# lst1.extend(lst2)
# print(lst1)


# lst = [1, 2, 3]

# new_lst = lst.copy()
# print(new_lst)


# lst = [1, 2, 3, 4, 5]

# print(lst[1:4])
# print(lst[::-1])


# lst = [5, 2, 9, 1]

# print(max(lst))
# print(min(lst))


# lst = [1, 2, 3]

# print(2 in lst)
# print(5 in lst)


# lst = [1, 2, 3]

# for i in lst:
#     print(i)


# lst = [1, 2, 3, 4]

# new_lst = [x*x for x in lst]
# print(new_lst)


# lst = [1, 2, 3, 4, 5, 6]

# while lst:
#     lst.pop()
    
# print(lst)


# lst = [1, 2, 3]

# while lst:
#     lst.pop()
    
# print(lst)


# x = "hello world"

# v = 0
# c = 0

# for ch in x:
#     if ch.isalpha():
#         if ch in "aeiou":
#             v += 1
#         else:
#             c += 1

# print("Vowels:", v)
# print("Consonants:", c)


# lst = [1, 2, 2, 3, 4, 3, 5]

# new_lst = []

# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)

# print(new_lst)


lst = [10, 45, 23, 89, 12]

max_val = lst[0]

for i in lst:
    if i > max_val:
        max_val = i

print(max_val)



        



            










