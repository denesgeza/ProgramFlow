for i in range(1, 13):
    print('No. {0} squared is {1} and cubed is {2}'.format(i, i ** 2, i ** 3))
    
for i in range(1, 13):
    print('No. {0:2} squared is {1:3} and cubed is {2:4}'.format(i, i ** 2, i ** 3))
    
print('Pi is approximately {0:12}'.format(22/7))  #general format 15 decimals
print('Pi is approximately {0:12f}'.format(22/7))   #floating point --> default values is 6 decimals
print('Pi is approximately {0:12.50f}'.format(22/7)) #floating point --> 50 decimals
print('Pi is approximately {0:52.50f}'.format(22/7)) #
print('Pi is approximately {0:62.50f}'.format(22/7)) #
print('Pi is approximately {0:<72.50f}'.format(22/7)) #left align, fl point 50 decimals, max python precision
print('Pi is approximately {0:<72.54f}'.format(22/7)) #left align, fl point 54 decimals, no point more than 50f