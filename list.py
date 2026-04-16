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


lst=[[3,2,1,8],[50,3,7,9],[2,3,7,8]]
# 
ans=[]
for i in range(len(lst)):
    temp=lst[i].copy()
    if i%2==0:
        for j in range(len(temp)):
            if temp[j]%2!=0:
                temp[j]+=1
                ans.append(temp)

            else:
                for j in range(len(lst)):
                    if temp[j]%2!=0:
                        temp[j]+=1
                        ans.append(temp)
                        print(lst)
                        print(ans)










