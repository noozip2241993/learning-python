
def anagram(word):
    if len(word) <= 1:
        return [word]
    elif len(word) == 2:
        return [word, word[1] + word[0]]
    else:
        length = len(word)
        result = []

    for index in range(length):
        head = word[index]
        rest = word[ : index] + word[index + 1 : ]

    # if the inptu is 'abc'
    # if the head is 'a', the temp 'bc', 'cb'
    # if the head is 'b', the temp 'ac', 'ca'
    temp = anagram(rest)

    for temp_word in temp:
        new_word = head + temp_word
        result.append(new_word)
        return result

print(anagram('x'))
print(anagram('xy'))
print(anagram('abc'))
print(anagram('abcd'))
print(anagram('food'))

def anagram_no_recurs(char_list=['F','O','O']):
    word = char_list
    for i in range(0, len(word)):
        for j in range(0, len(word)):
            if j != i:
                for k in range(0, len(word)):
                    if k != i and k != j:
                        print(word[i], word[j], word[k])

anagram_no_recurs()