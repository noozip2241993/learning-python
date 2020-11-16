from my_functions import change_working_dir

def char_frequency(text=''):
    '''
    char_frequency takes in a string and returns a list of tuples each tuple providing a unique character
    in the string and the count of it's occurances within that string.
    '''
    in_str = text
    result = [(x, len([c for c in in_str if c == x])) for x in get_unique_chars(in_str)]
    return result

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

def analyse_file_txt_OLD(file_name, encoding):
    END_SENTENCE = ('.','?','!')
    END_WORD = ('.','?','!',' ')
    ABBREVIATIONS = ['Mr', 'Mrs']

    full_text = ''

    # processing phase
    # read from file
    with open(file_name, mode='r', encoding=encoding) as txt_file:
        full_text = txt_file.read()

    # analyse the text character by character
    '''total word count, the total character count, the average word length,
    the average sentence length, a word distribution containing frequency 
    counts of all words, and the top 10 longest words'''
    total_letters = 0
    total_char = 0

    words = []
    total_words = 0

    sentences = []
    total_sentences = 0

    paragraphs = []
    total_paragraphs = 0

    # loop through characters in book_text to build word, 
    # sentence and paragraph lists.
    this_word = ''
    this_sentence = ''
    this_paragraph = ''
    prev_char = ''
    prev_word = ''
    in_word = False
    in_quote = False
    end_word = False
    end_sentence = False
    end_paragraph = False

    for char in full_text:
        # is this character...
        #in a word
        if char.isalpha():
            in_word = True
        else:
            in_word = False
        
        #after a word
        if not char.isalpha() and this_word != '':
            end_word = True
        else:
            end_word = False
        
        #the start of a quote
        if char == "“":
            in_quote = True
        
        #the end of a quote
        if prev_char == "”":
            in_quote = False

        #the end of a sentence
        if (not in_quote) and (char in END_SENTENCE) and (prev_word not in ABBREVIATIONS):
            end_sentence = True
        else:
            end_sentence = False

        #the end of a paragraph
        if (char == '\n') and (prev_char in END_SENTENCE) and (this_paragraph != ''):
            end_paragraph = True
        else:
            end_paragraph = False

        # Build words, sentences and paragraphs
        if end_word:
            words.append(this_word)
            if char == '\n':
                this_sentence += this_word + ' '
            else:
                this_sentence += this_word + char
            total_words += 1
            prev_word = this_word
            this_word = ''
        
        if in_word:
            this_word += char #build a word
            total_letters += 1 #count the character
        
        if end_sentence:
            sentences.append(this_sentence)
            this_paragraph += this_sentence + char
            total_sentences += 1
            this_sentence = ''
        
        if end_paragraph:
            paragraphs.append(this_paragraph)
            total_paragraphs += 1
            this_paragraph = ''

        prev_char = char
        total_char += 1

    # termination
    print(f'Total Characters: {total_char:,}')
    print(f'Total Words: {total_words:,}')
    print(f'Total Sentences: {total_sentences:,}')
    print(f'Total Paragraphs: {total_paragraphs:,}')
    print(f'Average word length: {total_char / total_words:,.1f} characters')
    print(f'Average sentence length: {total_words / total_sentences:,.1f} words')
    print(f'Average paragraph length: {total_words / total_paragraphs:,.1f} words')
    print(f'First parapraph: {paragraphs[0]}')
    print(f'Last paragraph: {paragraphs[-1]}')

def my_split(to_split, separators):
    import re
    reg_ex = '|'.join(map(re.escape, separators))
    return re.split(reg_ex, to_split)

def my_remove(str_to_edit, characters_to_remove):
    in_str = str_to_edit
    removes = characters_to_remove

    for char in removes:
        if char == '.':
            pass
        in_str = in_str.replace(char, '')
    return in_str

def text_to_sentences(text='', sentence_delimiters=[]):
    result = [line for line in my_split(text, sentence_delimiters) if line != ''] # non-empty string lines from text to a list of sentences based on given delimiters
    result = [line.strip('\n') for line in result] # ensure no newline chars within sentences
    return result

def generate_sentence_dict(sentence='', bad_chars = ''):
    letters_and_space = ''.join(char for char in sentence if char not in bad_chars) #remove given 'bad_chars' the result should be only letters and spaces
    letter_count = len(letters_and_space.replace(' ',''))
    character_count = len(sentence)
    word_list = letters_and_space.split(' ')
    word_count = sentence.count(' ') + 1
    average_word_length = letter_count / word_count
    result = {'text': sentence,
            'letter_count': letter_count,
            'character_count': character_count,
            'words': word_list,
            'word_count': word_count,
            'ave_word_length': average_word_length}
    return result

def analyse_file_txt(file_name, sentence_delimiters, omission_list=None):
    SENTENCE_DELIMITERS = sentence_delimiters
    NON_SPACE_WHITESPACE = ['\n', '\t', '\r', '\f', '\v']
    SYMBOLS = ['~', '@', '#', '$', '%', '^', '*', '_', '-', '+', '=', '{', '[', '}', ']', '|', '<', '>', '/']
    SENT_END_PUNCT = ['!', '.', '?']
    OTHER_PUNCTUATION = ['\"', '\'', '`', '&', '(', ')', ':', ';', ',']
    BAD_CHARS = ''.join(NON_SPACE_WHITESPACE + SYMBOLS + SENT_END_PUNCT + OTHER_PUNCTUATION)

    # read the file
    full_text = ''
    with open(file_name, mode='r', encoding='utf-8') as txt_file:
        full_text = txt_file.read()

    sentences = text_to_sentences(full_text, SENTENCE_DELIMITERS) # process the file's text into a list of sentences

    # generate a list of dictionaries each holding statistics about a sentence
    sentence_stats = []
    for sentence in sentences:
        sentence_stats.append(generate_sentence_dict(sentence, BAD_CHARS))

    # generate a list of dictionaries each holding statistics about each unique word
    word_stats = []
    for sentence in sentence_stats:
        pass # TODO

    longest_sentence = sorted(sentence_stats, key=lambda dict: dict['character_count'], reverse=True)[0]['text']
    total_word_count = 0
    total_character_count = 0
    overall_average_word_length = 0
    overall_average_sentence_length = 0

    print(f'Total word count: {total_word_count}')
    print(f'Total character count: {total_character_count}')
    print(f'The average word length: {overall_average_word_length} letters')
    print(f'The average sentence length: {overall_average_sentence_length} words')
    print('All words ending in “ly”: ')
    print('10 longest words: ')
    print(f'Longest sentence: {longest_sentence}')

def main():
    change_working_dir()
    FILENAME = 'remarks.txt'
    ##WORD_OMISSIONS = ['(Applause.)', 'THE PRESIDENT:', 'AUDIENCE:', 'END']
    WORD_OMISSIONS = None
    SENTENCE_DELIMITERS = ['  ','.\n', '\n\n']
    analyse_file_txt(FILENAME, SENTENCE_DELIMITERS, WORD_OMISSIONS)

    pass

if __name__ == '__main__':
    main()