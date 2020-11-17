from my_functions import change_working_dir
from my_functions import text_to_sentences
from my_functions import display_dict

def generate_sentence_dict(sentence=''):
    WHITESPACE = ' \n\t\r\f\v'
    SYMBOLS = '~@#$%^*_-+={[}]|<>/'
    PUNCTUATION = '!.?"`&():;,'
    bad_chars = WHITESPACE.replace(' ','') + SYMBOLS.replace('-','') + PUNCTUATION

    letters_and_spaces = ''.join(char for char in sentence if char not in bad_chars).replace('-',' ')
    letter_count = len(letters_and_spaces.replace(' ',''))
    character_count = len(sentence)
    word_list = letters_and_spaces.split(' ')
    word_count = sentence.count(' ') + 1
    average_word_length = letter_count / word_count
    result = {'text': sentence,
            'letter_count': letter_count,
            'character_count': character_count,
            'words': word_list,
            'word_count': word_count,
            'ave_word_length': average_word_length}
    return result

def calc_text_stats(list_of_sentence_dicts, display_stats=False):
    sentence_stats = list_of_sentence_dicts

    # calc simple stats
    total_word_count = sum(len(sentence['words']) for sentence in sentence_stats)
    total_character_count = sum(len(sentence['text']) for sentence in sentence_stats)
    average_word_length = total_character_count / total_word_count
    average_sentence_word_count = total_word_count / len(sentence_stats)
    
    # determine word frequencies
    unique_words = dict()
    for sentence in sentence_stats:
        for word in sentence['words']:
            if word.lower() in unique_words:
                unique_words[word.lower()] += 1
            else:
                unique_words[word.lower()] = 1
    unique_words_by_freq = sorted(unique_words.items(), key=lambda item: item[1], reverse=True)
    
    # make a list of the ten longest words
    long_word_count = 10
    longest_words = sorted(unique_words, key=lambda k: len(k), reverse=True)[:long_word_count]
    
    # make a list of the words ending with 'ly' and their frequency in the text.
    word_ending = 'ly'
    words_by_ending = list((word, count) for word, count in unique_words_by_freq if word[-1 * len(word_ending):] == word_ending)

    #pack up the simple statistics in a dict
    simple_stats = {'Total word count': total_word_count,
                'Total character count': total_character_count,
                'The average word length': average_word_length,
                'The average sentence length (in words)': average_sentence_word_count}

    # display the required stats
    if display_stats:
        display_dict(simple_stats)
        
        print(f'\nA word distribution of all words ending in "{word_ending}"')
        [print(f'{word}: {count}') for word, count in words_by_ending]

        print(f'\nA list of the top {long_word_count} longest words in descending order:')
        print(''.join([(f'{word}, ') for word in longest_words]).rstrip(', '))
    
    return simple_stats, unique_words_by_freq, words_by_ending, longest_words

def analyse_text_file(file_name, sentence_delimiters, omission_list=None):
    # read the file
    full_text = ''
    with open(file_name, mode='r', encoding='utf-8') as txt_file:
        full_text = txt_file.read()

    # generate a list of dictionaries each holding statistics about each sentence in the text
    sentence_stats = []
    delimiters = sentence_delimiters
    for sentence in text_to_sentences(full_text, delimiters):
        sentence_stats.append(generate_sentence_dict(sentence))

    # calc statistics about the text overall then display them
    calc_text_stats(sentence_stats, display_stats=True)

def main():
    change_working_dir() #ensure python working directory is the folder where this script resides.
    FILENAME = 'remarks.txt' # assumes same folder as this script
    WORD_OMISSIONS = None
    SENTENCE_DELIMITERS = ['  ','.\n', '\n\n'] # sentences split on double spaces, '.' char at the end of the line and double spaced lines

    analyse_text_file(FILENAME, SENTENCE_DELIMITERS, WORD_OMISSIONS)

if __name__ == '__main__':
    main()