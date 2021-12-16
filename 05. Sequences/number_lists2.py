even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

# add odd list to even
even.extend(odd)
print(even)

# sorts the new even list
even.sort()
print(even)

even.sort(reverse=True)
print(even)
