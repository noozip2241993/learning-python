from my_functions import change_working_dir

def task2():
    '''
    Read a text file named “book.txt” that may have multiple lines. Then create a “summary.txt” file that has the frequency of each letter, 
    case-insensitive, i.e., “a” and “A” are the same letter. Each line has a record of the letter and frequency. The last line should be a 
    summary to tell if the file has all 26 letters. A sample “summary.txt” is:

    A 25
    C 36
    …
    X 2
    Z 4

    It doesn’t have all letters.

    Another “book.txt” may generate the “summary.txt” as the following:

    A 25
    B 36
    …
    X 2
    Y 1
    Z 4

    It has all letters.
    '''

    # Ensure that the Python working directory is the directory where this file is
    change_working_dir()
    # Read a text file named “book.txt” that may have multiple lines.
    # create a “summary.txt” file that has the frequency of each letter, case-insensitive, i.e., “a” and “A” are the same letter.
    #   Each line has a record of the letter and frequency. 
    #   The last line should be a summary to tell if the file has all 26 letters.

task2()