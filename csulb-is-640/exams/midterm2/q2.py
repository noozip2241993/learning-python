START_ORD = ord('A') 
END_ORD = ord('Z')
LETTER_COUNT = 30

import random

random_letters = []
for i in range(LETTER_COUNT):
    letter = chr(random.randint(START_ORD, END_ORD)) # generate a random ord value from ord('A') to ord('Z') then cast as a character
    random_letters.append(letter)

print(sorted(random_letters, reverse=False)) #print in ascending order
print(sorted(random_letters, reverse=True)) #print in decending order