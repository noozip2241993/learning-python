print("5.10 (Anagrams)\n\
An anagram of a string is another string formed by rearranging the letters in the first. \n\
Write a script that produces all possible anagrams of a given string using only techniques \n\
that you’ve seen to this point in the book. [The itertools module provides many functions, \n\
including one that produces permutations.]")

import random
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

def generate_permutations(text):
    result = []
    
    return result

def print_list_in_rows(my_list=[], separator=' ', total_rows=10):
    for i, item in enumerate(my_list):
        if i % (len(my_list) // (total_rows - 1)) != 0:
            print(item, end=separator)
        else:
            print(item) 

this_word = words[random.randint(0, len(words) - 1)]
this_word_anagrams = generate_permutations(this_word)

print_list_in_rows(this_word_anagrams, '|')