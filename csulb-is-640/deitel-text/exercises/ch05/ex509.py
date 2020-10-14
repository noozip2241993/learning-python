print("5.9 (Palindrome Tester)\n\
A string that’s spelled identically backward and forward, like 'radar', is a palindrome.\n\
Write a function is_palindrome that takes a string and returns True if it’s a palindrome\n\
and False otherwise. Use a stack (simulated with a list as we did in Section 5.11) to help\n\
determine whether a string is a palindrome. Your function should ignore case sensitivity\n\
(that is, 'a' and 'A' are the same), spaces and punctuation.")

def is_palindrome(word='',verbose=False):
    #handle case, spaces and punctuation
    bad_chars = [' ', '.', ',', '?', '!']
    clean_word = word.lower() # eliminate case
    for char in bad_chars:
        clean_word.replace(char,'') # eliminate spaces and punctuation

    clean_word = list(clean_word)
    result = True
    for char in clean_word:
        end_char = clean_word.pop()
        if char != end_char:
            result = False

    if verbose:
        article = ' '
        if result:
            article = ' '
        else:
            article = ' not '
        print(f'{word} is{article}a palindrome.')
    
    return result

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

for word in words:
    is_palindrome(word, True)