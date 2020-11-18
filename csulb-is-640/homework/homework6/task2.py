from shared_functions import change_working_dir
from shared_functions import get_lines_from_text_file
from shared_functions import write_records_to_text_file
from shared_functions import get_char_frequency

def main():
    READ_FILE = 'book.txt'
    #READ_FILE = 'book2.txt' #testing a smaller file without all letters
    WRITE_FILE = 'summary.txt'
    START_ORD = ord('A')
    END_ORD = ord('Z')

    change_working_dir() # ensure the working directory is that which this script resides in
    full_text = ' '.join(get_lines_from_text_file(READ_FILE)).upper() # read the file
    char_frequency = get_char_frequency(full_text, START_ORD, END_ORD) # make the char frequency as a dict

    #check for all letters
    if len(char_frequency) < (END_ORD - START_ORD):
        char_frequency.append('\nIt doesn\'t have all letters.')
    else:
        char_frequency.append('\nIt has all letters.')

    write_records_to_text_file(WRITE_FILE, char_frequency) # write to summary.txt
    pass

if __name__ == '__main__':
    main()