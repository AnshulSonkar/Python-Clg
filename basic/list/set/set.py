# set 
# stored immutable element
# unordered
# only unique element


# s=set()
# s1={}
# print(type(s1))


# s={1,2,3,"hello"}
# print(s)


lst = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(max(freq, key=freq.get))