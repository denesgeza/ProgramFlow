import time
from time import time as my_timer

# print(time.gmtime(0))
# print(time.localtime(time.time()))
# print(time.time())

# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)

import random

wait_time = random.randint(1, 16)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

# strftime => string from time
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print('Your reaction time was {} seconds '.format(end_time - start_time))
