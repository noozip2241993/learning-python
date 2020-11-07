import random

MIN = 1
MAX = 6
SEED = 42

# after set the seed. it generates a fixed sequence in multiple run
# to see the difference, comment the following line and run multiple times
#random.seed(SEED)

for count in range(10):
    number = random.randint(MIN, MAX)
    print(f'random number is {number}')