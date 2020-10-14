print("5.11 (Summarizing Letters in a String) Write a function summarize_letters that receives a string \n\
and returns a list of tuples containing the unique letters and their frequencies in the string. Test your \n\
function and display each letter with its frequency. Your function should ignore case sensitivity \n\
(that is, 'a' and 'A' are the same) and ignore spaces and punctuation. When done, write a statement that says\n\
whether the string has all the letters of the alphabet.")

def summarize_letters(text=''):
    '''
    summarize_letters takes in a string and returns a list of tuples each tuple providing a unique character
    in the string and the count of it's occurances within that string.

    Non-alphabetic characters are ignored
    '''
    in_str = text
    word = remove_non_alpha(in_str)
    result = [(x, len([c for c in word if c == x])) for x in get_unique_chars(word)]
    print(result)

    has_every_letter(in_str, verbose=True)
    return result

def has_every_letter(text='', alphabet='qwertyuiopasdfghjklzxcvbnm', verbose=False):
    in_str = text
    alpha = alphabet

    res = True
    for char in alpha:
        res = [False for x in in_str if char == x[0]]

    if verbose:
        if res:
            print(f'\'{in_str}\' contains all letters in the alphabet.')
        else:
            print(f'\'{in_str}\' does not contain all letters in the alphabet.')
    
    return res

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

summarize_letters('letters')
summarize_letters('abcdefghijklmnopqrstuvwxyz')