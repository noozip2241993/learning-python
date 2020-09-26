'''
Calculate the mean, median and mode of the values 9, 11, 22, 34, 17, 22, 34, 22 and 40. 
Suppose the values included another 34. What problem might occur?
'''

#initialization
valA = [9, 11, 22, 34, 17, 22, 34, 22, 40]
valB = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]
mean = 0
median = 0
mode = []
myVals = valA

# processing
print(myVals)

# mean
for i in myVals:
    mean += i
mean /= len(myVals)

# median
myVals.sort()
middle_pos = len(myVals) // 2
if len(myVals) % 2 == 1:
    median = myVals[middle_pos]
else:
    m1 = myVals[middle_pos]
    m2 = myVals[middle_pos - 1]
    median = (m1 + m2) / 2

# mode
max_count = 0
for x in myVals:
    this_count = 0
    for y in myVals:
        if x == y:
            this_count += 1
    if max_count < this_count:
        max_count = this_count
        mode.clear()
        mode.append(x)
    elif max_count == this_count:
        max_count = this_count
        if x not in mode:
            mode.append(x)

# termination
print(f'Mean: {mean}')
print(f'Median: {median}')
print(f'Mode: {mode}')