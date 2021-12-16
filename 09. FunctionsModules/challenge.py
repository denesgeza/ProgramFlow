from time import get_clock_info, monotonic, perf_counter, process_time
import time

# write a program to display information on the four clocks
# check documentation for get_clock_info()

# help(get_clock_info)

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t\t\t", time.get_clock_info('perf_counter'))    
print("monotonic():\t\t\t", time.get_clock_info('monotonic'))
print("process_time():\t\t\t", time.get_clock_info('process_time'))