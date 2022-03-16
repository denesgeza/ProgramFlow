import sys


def my_range(n: int):
    print('my range starts')
    start = 0
    while start < n:
        print('my_range is returning {}'.format(start))
        yield start
        start += 1
        
# big_range = my_range(5)
big_range = my_range(10000)
_ = input('line 15')
print('big_range is {} bytes'.format(sys.getsizeof(big_range)))
print(next(big_range))

# create a list containing all values of the range
big_list = [val for val in big_range]
print('big_list is {} bytes'.format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
