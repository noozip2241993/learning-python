'''
9.6 (Class Average: Writing a Gradebook Dictionary to a JSON File) Reimplement
Exercise 9.3 using the json module to write the student information to the file in JSON
format. For this exercise, create a dictionary of student data in the following format:

    gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}

Each dictionary in the list represents one student and contains the keys 'first_name',
'last_name', 'exam1', 'exam2' and 'exam3', which map to the values representing each
student’s first name (string), last name (string) and three exam scores (integers). Output
the gradebook_dict in JSON format to the file grades.json.

9.7 (Class Average: Reading a Gradebook Dictionary from a JSON File) Reimplement
Exercise 9.4 using the json module to read the grades.json file created in the previous
exercise. Display the data in tabular format, including an additional column showing each
student’s average to the right of that student’s three exam grades and an additional row
showing the class average on each exam below that exam’s column.
'''
# initialization
import json
FOLDERNAME = 'ch09\\wrap-up-exercises\\resources\\'
FILENAME = 'gradebook.json'
FULLPATH = FOLDERNAME + FILENAME
COL_WIDTH = 15
student_keys = []
student_keys.append('first_name')
student_keys.append('last_name')
student_keys.append('exam1')
student_keys.append('exam2')
student_keys.append('exam3')
student_keys.append('student_ave')

student1dictionary = {
    student_keys[0]: 'John',
    student_keys[1]: 'Doe',
    student_keys[2]: 70,
    student_keys[3]: 80,
    student_keys[4]: 90
}

student2dictionary = {
    student_keys[0]: 'Jane',
    student_keys[1]: 'Doe',
    student_keys[2]: 90,
    student_keys[3]: 80,
    student_keys[4]: 70
}

gradebook_dict = {'students': [student1dictionary, student2dictionary]}

# processing
# write students to file, create it if it doesn't exist
with open(FULLPATH, mode='w') as gradebook:
    json.dump(gradebook_dict, gradebook)

# read students from file
with open(FULLPATH, mode='r') as gradebook:
    import pandas as pd
    df_gradebook = pd.read_json(gradebook)
students = df_gradebook.students # pd.read_json reads gradebook_dict key as an object attribute

# calculate class averages
exam1_total = 0
exam2_total = 0
exam3_total = 0
student_count = 0
for student in students:
    exam1_total += student['exam1']
    exam2_total += student['exam2']
    exam3_total += student['exam3']
    student_count += 1
exam_count = 3
exam1_ave = exam1_total / student_count
exam2_ave = exam2_total / student_count
exam3_ave = exam3_total / student_count
total_ave = (exam1_total + exam2_total + exam3_total) / (student_count * exam_count)

# termination
# print the header row(s)
headers = []
head_1 = ''
sep_row = ''
for key in student_keys:
    head_1 += f'{key:<{COL_WIDTH}}'
headers.append(head_1)
for char in head_1:
    sep_row += '-'
headers.append(sep_row)
for row in headers:
    print(row)

# print data row(s)
for student in students:
    row_str = ''
    for value in student.values():
        row_str += f'{value:<{COL_WIDTH}}'
    # calc and add the student average
    student_ave = (student[student_keys[2]] + student[student_keys[3]] + student[student_keys[4]]) / exam_count
    row_str += f'{student_ave:<{COL_WIDTH}.1f}'
    print(row_str)

#print summary row(s)
print(sep_row)
print(
    f'{"":<{COL_WIDTH}}'
    f'{"Averages":<{COL_WIDTH}}'
    f'{exam1_ave:<{COL_WIDTH}.1f}'
    f'{exam2_ave:<{COL_WIDTH}.1f}'
    f'{exam3_ave:<{COL_WIDTH}.1f}'
    f'{total_ave:<{COL_WIDTH}.1f}')