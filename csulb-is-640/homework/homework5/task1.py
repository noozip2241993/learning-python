from my_functions import change_working_dir

def task1():
    '''
    Assume that a file containing a series of student scores is named “scores.txt”. It may have the following content:

    Alice 69
    Bob 89
    Cindy 79

    Write a program that calculates the number of students and the average of all the scores stored in the file and print the output:

    The class average is 79 for 3 students.

    Also write the output to a log.txt file. You should use the with

    It should handle IOError exceptions that are raised when it fails to open the file, display an error message with the detail error exception and stop. 
    For example, it happens when there is no scores.txt in the current folder.

    For the following content, it should handle any ValueError exceptions that are raised when the items
    that are read from the score field are failed to be converted to a number by printing an error message and skip the record. There could be multiple error values to be ignored. For example, the data could be:

    Alice 69
    Bob eight-seven
    Cindy 79
    David 89
    Eric abc

    For the above data, it should skip both Bob and Eric and display:

    Bad score value for Boy, ignored.
    Bad score value for Eric, ignored.
    The class average is 79 for 3 students.

    The log.txt file should have the same content as the above output.
    '''
    DATA_FILE = 'scores.txt'

    # Ensure that the Python working directory is the directory where this file is
    change_working_dir()

    # Get data from scores.txt
    #   handle IOError exceptions
    #       when scores.txt does not exist
    #       display an error message with the detailed error exceptions.
    #       stop execution
    #   handle ValueError exceptions
    #       when score can't be converted to a number
    #       display an error message 'Bad score value for ___, ignored.'
    #       skip the record
    # Calculate the number of students
    # Calculate the average of student scores
    # Print the output 'The class average is 79 for 3 students.'
    # Write the output to log.txt. use 'with' statement

task1()