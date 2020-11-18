def change_working_dir(new_directory='', verbose=False):
    '''
    Redefine the Python working directory given a new directory path.
    If no path is provided, this will redefine the working directory to be
    that of the file calling this function.
    '''
    # Import the os module
    import os

    if verbose:
        # Print the current working directory
        print("Working directory was: {0}".format(os.getcwd()))

    # Get the new directory
    in_str = new_directory
    if in_str == '':
        in_str = os.path.dirname(os.path.realpath(__file__))

    # Change the current working directory
    os.chdir(in_str)

    if verbose:
        # Print the current working directory
        print("Working directory is now: {0}".format(os.getcwd()))

def get_lines_from_text_file(file_name=''):
    in_filename = file_name
    result = []
    try:
        with open(in_filename, 'r', encoding='utf8') as text_file:
            line = text_file.readline()
            while line != '':
                result.append(line.rstrip('\n'))
                line = text_file.readline()
    except FileNotFoundError:
        print(f'{file_name} not found. Returning empty string')
        return ''
    result[0] = result[0].replace('\ufeff', '') #because we force encoding to 'utf8' '\ufeff' may be written to the result. This removes it.
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

def multi_split(to_split, separators):
    import re
    reg_ex = '|'.join(separators)
    return re.split(reg_ex, to_split)

def text_to_sentences(text='', sentence_delimiters=[]):
    result = [line for line in multi_split(text, sentence_delimiters) if line != ''] # non-empty string lines from text to a list of sentences based on given delimiters
    result = [line.strip('\n') for line in result] # ensure no newline chars within sentences
    return result

def display_dict(dictionary={}):
    [print(f"{key}: {value:{',.2f' if type(value) == float else ','}}") for key, value in dictionary.items() if dictionary]

def get_char_frequency(string, start_ord, end_ord):
    char_frequency = dict()
    for char in string:
        if ord(char) >= start_ord and ord(char) <= end_ord:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
    char_frequency = sorted(char_frequency.items(), key=lambda item: item[0])
    return char_frequency

def main():
    pass

if __name__ == '__main__':
    main()