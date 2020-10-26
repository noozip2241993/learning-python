from my_functions import change_working_dir
from my_functions import get_records_from_text_file
from my_functions import write_records_to_text_file

def task1():
    DATA_FILE = 'scores.txt'
    #DATA_FILE = 'does_not_exist.txt'
    LOG_FILE = 'log.txt'

    change_working_dir() # Ensure that the Python working directory is the directory where this file is

    file_records = get_records_from_text_file(DATA_FILE) #IOErrors handled in function call

    if file_records != None:
        valid_records = []
        for record in file_records:
            try:
                name = str(record[0])
                score = int(record[1])
                valid_records.append([name, score])
            except ValueError: # Handle ValueErrors for bad score values
                print(f'Bad score value for {record[0]}, ignored.')
        
        student_count = len(valid_records) # Calculate the number of students
        class_ave = sum(record[1] for record in valid_records) / student_count # Calculate the average of student scores
    
        # Print the output 'The class average is 79 for 3 students.'
        print(f'The class average is {class_ave:.0f} for {student_count} students.')

        write_records_to_text_file(LOG_FILE, valid_records) # Write the output to log.txt. use 'with' statement
task1()