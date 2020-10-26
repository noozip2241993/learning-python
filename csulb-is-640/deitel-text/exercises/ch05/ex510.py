print("5.10 (Anagrams)\n\
An anagram of a string is another string formed by rearranging the letters in the first. \n\
Write a script that produces all possible anagrams of a given string using only techniques \n\
that you’ve seen to this point in the book. [The itertools module provides many functions, \n\
including one that produces permutations.]")

words = ['sock', 'neat', 'march', 'zonked', 'toad', 'whisper', 'four', 'admit', 
'list', 'effect', 'guess', 'harmony', 'alluring', 'sun', 'count', 'half', 'five', 'hurried', 
'stomach', 'rush', 'refuse', 'ground', 'reject', 'heal', 'communicate', 'damaged', 'terrify', 
'flat', 'cough', 'cap', 'rock', 'pine', 'risk', 'exclusive', 'brush', 'snobbish', 'twig', 
'answer', 'pot', 'move', 'obtain', 'brown', 'fetch', 'polite', 'insidious', 'childlike', 
'front', 'grotesque', 'cup', 'clever', 'straight', 'squash', 'flawless', 'taste', 'seat', 
'minor', 'threatening', 'occur', 'disillusioned', 'cakes', 'alula', 'anana', 'civic', 'deked', 
'deled', 'dered', 'dewed', 'kaiak', 'kayak', 'lemel', 'level', 'madam', 'malam', 'minim', 
'radar', 'refer', 'rotor', 'sagas', 'samas', 'sedes', 'seles', 'semes', 'seres', 'sexes', 
'shahs', 'simis', 'siris', 'solos', 'stats', 'stets', 'stots', 'sulus', 'susus', 'tenet', 
'torot', 'araara', 'ataata', 'degged', 'denned', 'hajjah', 'hallah', 'mallam', 'marram', 
'pullup', 'redder', 'selles', 'serres', 'sesses', 'succus', 'tallat', 'terret', 'tirrit', 
'deified', 'hadedah', 'halalah', 'reifier', 'repaper', 'reviver', 'rotator', 'seities', 
'sememes', 'rotavator']


def generate_permutations(text=''):
    input_str = text

    if len(input_str)  == 0:
        return ['']

    result = []
    first_char = input_str[0]
    other_chars = input_str[1:]

    words = generate_permutations(other_chars)
    for word in words:
        for i in range(len(word) + 1):
            s = word[:i] + first_char + word[i:]
            result.append(s)
    
    return result
    
def print_list_in_rows(my_list=[], col_separator=' ', desired_row_count=10):
    '''
    Given a list object, a separating character and a number of rows
    print_list_in_rows will print that list over as many columns as necessary
    to not exceed the given number of rows. The separator character will indicate
    the breaks between columns.

    If the provided row count is greater than the number of elements in the list, 
    the list will print based on the number of elements in it instead of the given
    number of rows. 
    '''
    total_rows = desired_row_count
    input_list = my_list
    sep = col_separator

    for i, item in enumerate(input_list):
        if total_rows > len(input_list):
            total_rows = len(input_list) + 1
        
        if i % (len(input_list) // (total_rows - 1)) != 0:
            print(item, end=sep)
        else:
            print(item) 

def get_random_list_element(my_list=[]):
    '''
    Given a list object return a random element from that list.
    '''
    import random
    in_list = my_list
    return in_list[random.randint(0, len(words) - 1)]

def filter_to_dictionary_words(words=[]):
    import enchant
    raw_list = words
    dictionary = enchant.Dict('en_US')
    result = []
    for item in raw_list:
        #handle case, spaces
        item = item.lower() # eliminate case
        sub_items = item.split()# eliminate spaces

        this_result = ''
        keep_checking = True

        while keep_checking:
            for sub_item in sub_items:
                if dictionary.check(sub_item):
                    this_result += sub_item + ' '
                else:
                    keep_checking = False
                    this_result = ''
            this_result = this_result.strip()
            keep_checking = False

        if this_result != '' and len(this_result) == len(item) and this_result not in result:
            result.append(this_result)
    if len(result) == 0:
        result.append('No dictionary words')

    return result
    
def anagrams(word='', only_english=False):
    this_word = word
    if this_word == '':
        this_word = get_random_list_element(words)
    
    this_word_anagrams = generate_permutations(this_word)

    if only_english:
        this_word_anagrams = filter_to_dictionary_words(this_word_anagrams)
    
    print(f'Anagrams of: {this_word} are... {this_word_anagrams}')

anagrams('FOX')
