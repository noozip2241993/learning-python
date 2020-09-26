"""9.1 (Class Average: Writing Grades to a Plain Text File) Figure 3.2 presented a class
average script in which you could enter any number of grades followed by a sentinel value,
then calculate the class average. Another approach would be to read the grades from a file.
In an IPython session, write code that enables you to store any number of grades into a
grades.txt plain text file.

9.2 (Class Average: Reading Grades from a Plain Text File) In an IPython session,
write code that reads the grades from the grades.txt file you created in the previous 
exercise. Display the individual grades and their total, count and average."""

# initialization phase
all_grades = []
grade_sum = 0 # sum of grades
grade_count = 0 # number of grades entered
this_grade = 0
SENTINAL = -1
FOLDERNAME = 'wrap-up-exercises/resources/'
FILENAME = 'grades.txt'
FULLPATH = FOLDERNAME + FILENAME

# ensure the folder exists
import os
if not os.path.exists(FOLDERNAME):
    os.makedirs(FOLDERNAME)

# processing phase
# read existing grades from file, create the file if it doesn't exist
with open(FULLPATH, mode='a+') as grades_file:
    for existing_grade in grades_file:
        all_grades.append(int(existing_grade))

# get new grades via sentinal-controlled user input
while this_grade != SENTINAL:
    this_grade = int(input(f'Enter grade, {SENTINAL} to end: '))
    if this_grade != SENTINAL:
        all_grades.append(int(this_grade))

# write all_grades to file, also sum and count the grades
with open (FULLPATH, mode='w') as grades_file:
    for grade in all_grades:
        grades_file.write(f'{grade}\n')
        grade_sum += int(grade)
        grade_count += 1

# termination phase
if grade_count != 0:
    # display the average grade
    average = grade_sum / grade_count
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered')