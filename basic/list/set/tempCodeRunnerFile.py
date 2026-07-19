lst = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(max(freq, key=freq.get))