print("5.11 (Summarizing Letters in a String) Write a function summarize_letters that receives a string \n\
and returns a list of tuples containing the unique letters and their frequencies in the string. Test your \n\
function and display each letter with its frequency. Your function should ignore case sensitivity \n\
(that is, 'a' and 'A' are the same) and ignore spaces and punctuation. When done, write a statement that says\n\
whether the string has all the letters of the alphabet.")

def summarize_letters(text=''):
    word = text
    result = []
    for letter in word:
        if len(list(filter(lambda x:letter in x, result))) == 0:
            count = len([c for c in word if c == letter])
            letter_tuple = (letter, count)
            result.append(letter_tuple)
    return result


print(summarize_letters('letters'))