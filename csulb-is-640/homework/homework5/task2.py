from my_functions import change_working_dir
from my_functions import get_lines_from_text_file
from my_functions import write_records_to_text_file

def task2():

    change_working_dir() # Ensure that the Python working directory is the directory where this file is
    
    BOOK_FILE = 'book.txt'
    #BOOK_FILE = 'book_missing_A.txt'
    ALL_LETTERS = "It has all letters."
    NOT_ALL_LETTERS = "It doesn't have all letters."
    START_ORD = ord('A')
    END_ORD = ord('Z')

    book_lines = get_lines_from_text_file(BOOK_FILE) # Read a text file
    book_chars = ''.join(book_lines).replace(' ', '').upper() #remove spaces and make all letters uppercase
    book_chars = ''.join(sorted(book_chars)) # sort the characters

    char_freq = [0 for x in range(0, END_ORD)] #initialize a list of a length matching the ord value of the last character we are interested in, populate with values of 0

    # loop thorugh the book_chars and tally the letter counts in char_freq
    for char in book_chars:
        char_ord = ord(char)
        if char_ord in range(0, END_ORD):
            char_freq[char_ord] += 1

    # create a “summary.txt” file that has the frequency of each letter, case-insensitive, i.e., “a” and “A” are the same letter.
    #   Each line has a record of the letter and frequency. 
    result = []
    for i in range(START_ORD, END_ORD): #65 to 91 represent the ASCII ord values of 'A' thru 'Z'. Only want the counts of those characters.
        result.append((chr(i), char_freq[i]))
        
    #   The last line should be a summary to tell if the file has all 26 letters.
    if len([0 for item in result if item[1] == 0]) == 0:
        result.append(f'\n{ALL_LETTERS}') # if we don't have any letters with a count of 0 then we know we have all letters
    else:
        result.append(f'\n{NOT_ALL_LETTERS}') # otherwise there are letters with a count of 0 
    
    write_records_to_text_file('summary.txt', result)

task2()