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
