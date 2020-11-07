def get_records_from_text_file(file_name='',delimiter=None):
    '''
    Given a filename and a delimiter (None by default), get_records_from_text_file returns
    a two-dimensional list containing the fields in each line of the text file.

    If the filename provided does not exist in the current working directory, returns None
    '''  
    in_filename = file_name
    read_mode = 'r'
    in_delim = delimiter
    result = []

    try:
        with open(in_filename, read_mode) as text_file:
            in_records = [line.split(in_delim) for line in text_file]
            pass
            result = in_records
    except IOError:
        # when scores.txt does not exist display an error message and stop execution
        print(f'{in_filename} does not exist. Ending execution.')
        return None
    return result

def write_records_to_text_file(file_name='log.txt', records=[]):
    in_filename = file_name
    in_records = records
    with open(in_filename, 'w') as text_file:
        for record in in_records:
            str_record = ''
            if type(record) is str:
                str_record = record
            else:
                for field in record:
                    str_record += f'{field} '
            str_record = str_record.rstrip(' ') + '\n'
            text_file.write(str_record)

    print(f'Writing to {in_filename} done.')

def get_grade_gpa(score):
    grade = None
    gpa = None
    try:
        this_score = int(score)

        if this_score >= 90:
            grade = 'A'
            gpa = 4.0
        elif this_score >= 80:
            grade = 'B'
            gpa = 3.0
        elif this_score >= 70:
            grade = 'C'
            gpa = 2.0
        elif this_score >= 60:
            grade = 'D'
            gpa = 1.0
        else:
            grade = 'F'
            gpa = 0.0
    except TypeError as error:
        print(f'{score} is not a valid score. {error}')
    finally:
        return grade, gpa

def main():
    FILENAME = 'scores.txt'
    scores_records = get_records_from_text_file(FILENAME) #read from scores.txt
    grades = []
    class_gpa = 0

    for record in scores_records:
        first_name = record[0]
        last_name = record[1]
        score = int(record[2])
        grade, gpa = get_grade_gpa(score) #determine the letter grade and gpa score for this record
        grades.append(f'{first_name} {last_name} {grade}') #add this records name and grade to the grades list
        class_gpa += gpa # add this records gpa to the class_gpa

    score_count = len(scores_records)
    class_gpa = class_gpa / score_count # find the average gpa for the class
    gpa_str = f'The class GPA is {class_gpa:.2f}'
    grades.append(gpa_str)
    write_records_to_text_file('grades.txt',grades) #write to grades.txt

main()