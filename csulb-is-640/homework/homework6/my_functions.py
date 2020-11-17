def change_working_dir(new_directory=''):
    '''
    Redefine the Python working directory given a new directory path.
    If no path is provided, this will redefine the working directory to be
    that of the file calling this function.
    '''
    # Import the os module
    import os

    # Print the current working directory
    print("Working directory was: {0}".format(os.getcwd()))

    # Get the new directory
    in_str = new_directory
    if in_str == '':
        in_str = os.path.dirname(os.path.realpath(__file__))

    # Change the current working directory
    os.chdir(in_str)

    # Print the current working directory
    print("Working directory is now: {0}".format(os.getcwd()))

def get_lines_from_text_file(file_name=''):
    in_filename = file_name
    result = []
    with open(in_filename, 'r', encoding='utf8') as text_file:
        line = text_file.readline()
        while line != '':
            result.append(line.rstrip('\n'))
            line = text_file.readline()
    result[0] = result[0].replace('\ufeff', '') #because we force encoding to 'utf8' '\ufeff' may be written to the result. This removes it.
    return result

def get_records_from_text_file(file_name='',delimiter=None):
    '''
    Given a filename and a delimiter (None by default), get_records_from_text_file returns
    a two-dimensional list containing the fields in each line of the text file.

    If the filename provided does not exist in the current working directory, returns None
    '''  
    in_filename = file_name
    in_delim = delimiter
    result = []

    try:
        with open(in_filename, 'r') as text_file:
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

def char_frequency(text=''):
    '''
    char_frequency takes in a string and returns a list of tuples each tuple providing a unique character
    in the string and the count of it's occurances within that string.
    '''
    in_str = text
    result = [(x, len([c for c in in_str if c == x])) for x in get_unique_chars(in_str)]
    return result

def remove_non_alpha(text=''):
    in_str = text
    special_chars = " ~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    numberic_chars = '1234567890'
    bad_chars = special_chars + numberic_chars
    result = [x for x in in_str if x not in bad_chars]
    return result

def get_unique_chars(text=''):
    in_str = text
    result = {x for x in in_str} #returns a set of the unique charaters in the text arg 
    return result

def get_sentences(text=''):
    import nltk.data

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    data = text
    return '\n'.join(tokenizer.tokenize(data))

def multi_split(to_split, separators):
    import re
    reg_ex = '|'.join(map(re.escape, separators))
    return re.split(reg_ex, to_split)

def text_to_sentences(text='', sentence_delimiters=[]):
    result = [line for line in multi_split(text, sentence_delimiters) if line != ''] # non-empty string lines from text to a list of sentences based on given delimiters
    result = [line.strip('\n') for line in result] # ensure no newline chars within sentences
    return result

def generate_sentence_dict(sentence='', bad_chars = ''):
    letters_and_space = ''.join(char for char in sentence if char not in bad_chars) #remove given 'bad_chars' the result should be only letters and spaces
    letter_count = len(letters_and_space.replace(' ',''))
    character_count = len(sentence)
    word_list = letters_and_space.split(' ')
    word_count = sentence.count(' ') + 1
    average_word_length = letter_count / word_count
    result = {'text': sentence,
            'letter_count': letter_count,
            'character_count': character_count,
            'words': word_list,
            'word_count': word_count,
            'ave_word_length': average_word_length}
    return result

def main():
    pass

if __name__ == '__main__':
    main()