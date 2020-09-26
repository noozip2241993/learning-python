'''
9.8 (pickle Object Serialization and Deserialization) We mentioned that we prefer
to use JSON for object serialization due to the Python documentation’s stern security
warnings about pickle. However, pickle has been used to serialize objects for many years,
so you’re likely to encounter it in Python legacy code. According to the documentation,
“If you are doing your own pickle writing and reading, you’re safe (provided no one else
has access to the pickle file, of course.)”

Reimplement your solutions to Exercises 9.6– 9.7 using the pickle module’s dump function 
to serialize the dictionary into a file and its load function to deserialize the object. 
Pickle is a binary format, so this exercise requires binary files. Use the file-open mode 
'wb' to open the binary file for writing and 'rb' to open the binary file for reading. 
Function dump receives as arguments an object to serialize and a file object in which to 
write the serialized object. Function load receives the file object containing the 
serialized data and returns the original object. The Python documentation suggests the 
pickle file extension .p.
'''
# initialization
import pickle
FOLDERNAME = 'ch09\\wrap-up-exercises\\resources\\'
FILENAME = 'gradebook.p'
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
with open(FULLPATH, mode='wb') as gradebook:
    pickle.dump(gradebook_dict, gradebook)

# read students from file
with open(FULLPATH, mode='rb') as gradebook:
    import pandas as pd
    df_gradebook = pd.read_pickle(gradebook)
students = df_gradebook['students'] #pd.read_pickle reads gradebook_dict key as string attribute

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