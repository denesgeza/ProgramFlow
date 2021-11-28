# print all nos from 0 to 20 which are not divisible by 3 and 5
for i in range(0, 21, 1):
    if i % 5 == 0 or i % 3 == 0:
        continue
    print(i)

