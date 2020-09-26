'''
5.12 (Telephone-Number Word Generator) You should find this exercise to be entertaining. 
Standard telephone keypads contain the digits zero through nine. The numbers two through 
nine each have three letters associated with them, as shown in the following table:

Digit   Letters
2       A B C
3       D E F
4       G H I
5       J K L
6       M N O
7       P R S
8       T U V
9       W X Y

Many people find it difficult to memorize phone numbers, so they use the correspondence 
between digits and letters to develop seven-letter words (or phrases) that correspond to 
their phone numbers. For example, a person whose telephone number is 686-
2377 might use the correspondence indicated in the preceding table to develop the seven
letter word “NUMBERS.” Every seven-letter word or phrase corresponds to exactly one
seven-digit telephone number. A budding data science entrepreneur might like to reserve
the phone number 244-3282 (“BIGDATA”).

Every seven-digit phone number without 0s or 1s corresponds to many different
seven-letter words, but most of these words represent unrecognizable gibberish. A 
veterinarian with the phone number 738-2273 would be pleased to know that the number 
corresponds to the letters “PETCARE.” Write a script that, given a seven-digit number, 
generates every possible seven-letter word combination corresponding to that number. There 
are 2,187 (37) such combinations. Avoid phone numbers with the digits 0 and 1 (to which 
no letters correspond). See if your phone number corresponds to meaningful words.
'''

#initialization
digit_letter_map = [
    ['0','0','0'],      #0 No letters
    ['1','1','1'],      #1 No letters
    ['A', 'B', 'C'],    #2
    ['D', 'E', 'F'],    #3
    ['G', 'H', 'I'],    #4
    ['J', 'K', 'L'],    #5
    ['M', 'N', 'O'],    #6
    ['P', 'R', 'S'],    #7
    ['T', 'U', 'V'],    #8
    ['W', 'X', 'Y']]    #9

#phone_number = str(input('Enter the digits that make up your phone number: '))
phone_number = '6733544'
digits_phone_number = phone_number.count
digits_possible = digit_letter_map.count

#processing
relevent_maps = []

for char in phone_number:
    relevent_maps.append(digit_letter_map[int(char)])

res = [[i+j+k+l+m+n+o] 
        for i in relevent_maps[0]
        for j in relevent_maps[1]
        for k in relevent_maps[2]
        for l in relevent_maps[3]
        for m in relevent_maps[4]
        for n in relevent_maps[5]
        for o in relevent_maps[6]]

#termination
for row in res:
    print(row)