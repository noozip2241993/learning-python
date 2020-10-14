print("(Word or Phrase to Phone-Number Generator)\n\
Just as people would enjoy knowing what word or phrase their phone number corresponds to,\n\
they might choose a word or phrase appropriate for their business and determine what phone\n\
numbers correspond to it. These are sometimes called vanity phone numbers, and various websites\n\
sell such phone numbers. Write a script similar to the one in the previous exercise that produces\n\
the possible phone number for the given seven-letter string.")

def vanity_phone(text=''):
    raw_str = text

    digit_letter_map = [
    ['0', '0', '0'],    #0 No letters
    ['1', '1', '1'],    #1 No letters
    ['A', 'B', 'C'],    #2
    ['D', 'E', 'F'],    #3
    ['G', 'H', 'I'],    #4
    ['J', 'K', 'L'],    #5
    ['M', 'N', 'O'],    #6
    ['P', 'R', 'S'],    #7
    ['T', 'U', 'V'],    #8
    ['W', 'X', 'Y']]    #9

    res = ''

    #via simple loops
    for char in raw_str:
        for i in range(0, len(digit_letter_map)):
            if char.upper() in digit_letter_map[i]:
                res += str(i) 

    return res

print(vanity_phone('speeedo'))