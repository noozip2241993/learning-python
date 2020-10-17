def change_working_dir(new_directory=''):
    '''
    Redefine the Python working directory given a new directory path.
    If no path is provided, this will redefine the working directory to be
    that of the file calling this function.
    '''
    # Import the os module
    import os

    # Print the current working directory
    print("Current working directory: {0}".format(os.getcwd()))

    # Get the new directory
    in_str = new_directory
    if in_str == '':
        in_str = os.path.dirname(os.path.realpath(__file__))

    # Change the current working directory
    os.chdir(in_str)

    # Print the current working directory
    print("Current working directory: {0}".format(os.getcwd()))


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