import random
import time

# number list
min = 1
max = 100001 # do I have to correct here something? 
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


# start the record
start_time = time.time()

# binary search
result = None
while result != random_num: 
    half = (max + min) // 2 
    if random_num > half:
        min = half + 1
    elif random_num < half:
        max = half - 1
    else:
        # stop the record
        end_time = time.time()
        print(f'The searched int is {half}.')
        elapsed_time = end_time - start_time
        print(f"Execution time: {elapsed_time} seconds")    
        result = half 


