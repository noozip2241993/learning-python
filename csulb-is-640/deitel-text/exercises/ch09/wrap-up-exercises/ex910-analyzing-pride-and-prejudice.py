'''
9.10 (Project: Analyzing a Book from Project Gutenberg) A great source of plain text
files is the collection of over 57,000 free e-books at Project Gutenberg:
https://www.gutenberg.org

These books are out of copyright in the United States. For information about Project
Gutenberg’s Terms of Use and copyright in other countries, see:
https://www.gutenberg.org/wiki/Gutenberg:Terms_of_Use

Download the text-file version of Pride and Prejudice from Project Gutenberg
https://www.gutenberg.org/ebooks/1342

Create a script that reads Pride and Prejudice from a text file. Produce statistics about the
book, including the total word count, the total character count, the average word length,
the average sentence length, a word distribution containing frequency counts of all words,
and the top 10 longest words. 

In the “Natural Language Processing (NLP)” chapter, you’ll find lots of more sophisticated 
techniques for analyzing and comparing such texts. Each Project Gutenberg e-book begins and 
ends with some additional text, such as licensing information, which is not part of the e-book 
itself. You may want to remove that text from your copy of the book before analyzing its text.
'''
## DESIGN
# 1 read the txt file to a string object
# 2 remove non-prose characters
# 3 parse prose
# 3.1 parse words to a list
# 3.2 parse sentences to a list
# 3.3 parse paragraphs to a list
# 4 produce statistics
# 4.1 character statistics
# 4.1.1 total character count
# 4.2 word statistics
# 4.2.1 total word count
# 4.2.2 average word length
# 4.2.3 frequency count of all words
# 4.3.4 10 longest words
# 4.3 sentence statistics
# 4.3.1 average sentence length

# initialization phase
FOLDERNAME = 'ch09//wrap-up-exercises//resources//analyze-txt//'
FILENAME = 'pride-and-prejudice.txt'
BOOK_TITLE = 'PRIDE AND PREJUDICE'
START_TEXT = '*** START OF THIS PROJECT GUTENBERG EBOOK ' + BOOK_TITLE + ' ***'
END_TEXT = '*** END OF THIS PROJECT GUTENBERG EBOOK ' + BOOK_TITLE + ' ***'
ENCODING = 'utf-8'

def ensure_folder(folder_path=''):
    ''' checks whether the folder provided exists. creates it if it doesn't.'''
    import os
    # ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def analyse_file_txt(file_name, folder_path, encoding):
    END_SENTENCE = ['.','?','!']
    ABBREVIATIONS = ['Mr', 'Mrs']
    full_text = ''

    full_path = folder_path + file_name
    # ensure the folder exists
    ensure_folder(folder_path)

    # processing phase
    # read from file
    with open(full_path, mode='r', encoding=encoding) as pride:
        full_text = pride.read()

    #determine the actual book's text (as opposed to copyright text, etc)
    s_index = full_text.find(START_TEXT) + len(START_TEXT)
    e_index = full_text.find(END_TEXT)
    book_text = full_text[s_index:e_index]

    # analyse the text character by character
    '''total word count, the total character count, the average word length,
    the average sentence length, a word distribution containing frequency 
    counts of all words, and the top 10 longest words'''
    total_letters = 0
    total_char = 0

    words = []
    total_words = 0
    ave_word_len = 0

    sentences = []
    total_sentences = 0
    ave_sentence_len = 0

    paragraphs = []
    total_paragraphs = 0
    ave_paragraph_len = 0

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

    for char in book_text:
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
            if this_word == 'in':
                print() #Working on ensuring no '\n' chars in any words sentences or paragraphs
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
    print(f'Total Words: {total_words}')
    print(f'Total Sentences: {total_sentences}')
    print(f'Total Paragraphs: {total_paragraphs}')

    # write words to file
    with open (FOLDERNAME + BOOK_TITLE + ' words.txt', mode='w') as words_file:
        for word in words:
            words_file.write(f'{word}|')

    # write sentences to file
    with open (FOLDERNAME + BOOK_TITLE + ' sentences.txt', mode='w') as sentence_file:
        for sentence in sentences:
            sentence_file.write(f'{sentence}\n')

    # write paragraphs to file
    with open (FOLDERNAME + BOOK_TITLE + ' paragraphs.txt', mode='w') as paragraph_file:
        for paragraph in paragraphs:
            paragraph_file.write(f'{paragraph}\n')

def method2((file_name, folder_path, encoding):


analyse_file_txt(FILENAME, FOLDERNAME, ENCODING)