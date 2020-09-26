"""
9.3 (Class Average: Writing Student Records to a CSV File) An instructor teaches a
class in which each student takes three exams. The instructor would like to store this 
information in a file named grades.csv for later use. Write code that enables an instructor
to enter each student’s first name and last name as strings and the student’s three exam
grades as integers. Use the csv module to write each record into the grades.csv file. Each
record should be a single line of text in the following CSV format:
    firstname,lastname,exam1grade,exam2grade,exam3grade
    
9.4 (Class Average: Reading Student Records from a CSV File) Use the csv module to
read the grades.csv file from the previous exercise. Display the data in tabular format.

9.5 (Class Average: Creating a Grade Report from a CSV File) Modify your solution
to the preceding exercise to create a grade report that displays each student’s average to the
right of that student’s row and the class average for each exam below that exam’s column
"""

import csv

# Initialization
FOLDERNAME = 'ch09\\wrap-up-exercises\\resources\\'
FILENAME = 'grades.csv'
FULLPATH = FOLDERNAME + FILENAME
STR_COLUMNS = ['First Name', 'Last Name']
INT_COLUMNS = ['Exam1 Grade', 'Exam2 Grade', 'Exam3 Grade']
SENTINAL = -1
PRINT_COL_SPACE = 15
exam_records = []
separator_row = ''

# ensure the folder exists
import os
if not os.path.exists(FOLDERNAME):
    os.makedirs(FOLDERNAME)
if not os.path.isfile(FULLPATH):
    open(FULLPATH, mode='w+')

# Processing
# Read existing grades.csv file to exam_records, create the file if it doesn't exist
with open(FULLPATH, 'r', newline='') as existing_grades:
    reader = csv.reader(existing_grades)
    for record in reader:
        exam_records.append(record)

# Add new records to exam_records
user_input = ''
while user_input != str(SENTINAL):
    new_record = []
    for column in STR_COLUMNS:
        user_input = str(input(f'Enter {column}: '))
        new_record.append(user_input)
    for column in INT_COLUMNS:
        user_input = int(input(f'Enter {column}: '))
        new_record.append(user_input)
    exam_records.append(new_record)

    user_input = input(f'Enter {SENTINAL} to end: ')

# Write all exam_records to grades.csv file
with open(FULLPATH, mode='w', newline='') as grades:
    writer = csv.writer(grades)
    for record in exam_records:
        writer.writerow([record[0], record[1], record[2], record[3], record[4]])

# Termination
# Print exam_records to screen
with open(FULLPATH, mode='r', newline='') as grades:
    # Prepare and print headers
    head_rows = ['','']
    for column in STR_COLUMNS, INT_COLUMNS:
        for index in column:
            head_rows[0] += f'{index:<{PRINT_COL_SPACE}}'
    head_rows[0] += f'{"Average Grade":<{PRINT_COL_SPACE}}'
    for char in head_rows[0]:
        separator_row += '-'
    head_rows[1] = separator_row
    print(head_rows[0])
    print(head_rows[1])

    # Print data rows and prep summary row data
    reader = csv.reader(grades)
    records_count = 0
    exam1_total = 0
    exam2_total = 0
    exam3_total = 0
    for record in reader:
        fname, lname, exam1, exam2, exam3 = record
        record_ave = (int(exam1) + int(exam2) + int(exam3)) / 3
        records_count += 1
        exam1_total += int(exam1)
        exam2_total += int(exam2)
        exam3_total += int(exam3)

        print(
            f'{fname:<{PRINT_COL_SPACE}}'
            f'{lname:<{PRINT_COL_SPACE}}'
            f'{exam1:<{PRINT_COL_SPACE}}'
            f'{exam2:<{PRINT_COL_SPACE}}'
            f'{exam3:<{PRINT_COL_SPACE}}'
            f'{record_ave:<{PRINT_COL_SPACE}.1f}')

    exam1_ave = exam1_total / records_count
    exam2_ave = exam2_total / records_count
    exam3_ave = exam3_total / records_count
    total_ave = (exam1_total + exam2_total + exam3_total) / (records_count * 3)

    # Print summary rows
    print(separator_row)
    print(
        f'{" ":<{PRINT_COL_SPACE}}'
        f'{"Average":<{PRINT_COL_SPACE}}'
        f'{exam1_ave:<{PRINT_COL_SPACE}.1f}'
        f'{exam2_ave:<{PRINT_COL_SPACE}.1f}'
        f'{exam3_ave:<{PRINT_COL_SPACE}.1f}'
        f'{total_ave:<{PRINT_COL_SPACE}.1f}')
    