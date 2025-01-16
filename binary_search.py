import random
import time

# number list
min = 1
max = 100001
numbers = list(range(min, max))

# random_number
random_num = random.choice(numbers)

# start the record
start_time = time.time()

# standard search
for x in numbers: 
    if x == random_num:
        # stop the record
        end_time = time.time()

        print('The number was found.')

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")

# binary search
half_max = (max - min) // 2 

