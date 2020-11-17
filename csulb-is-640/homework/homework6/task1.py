from my_functions import change_working_dir
from my_functions import text_to_sentences
from my_functions import generate_sentence_dict

def display_txt_file_statistics(dict_of_stats={}):
    this_word_count = dict_of_stats['word count']
    this_char_count = dict_of_stats['character count']
    ave_word_length = dict_of_stats['average word length']
    ave_words_in_sent = dict_of_stats['average words in a sentence']

    print(f'Total word count: {this_word_count}')
    print(f'Total character count: {this_char_count}')
    print(f'The average word length: {ave_word_length:.2f} letters')
    print(f'The average sentence length: {ave_words_in_sent:.2f} words')
    print('All words ending in “ly”: {ly_words}')
    print('10 longest words: ')

def calc_text_stats(list_of_sentence_dicts, display_stats=False):
    sentence_stats = list_of_sentence_dicts
    total_word_count = sum(len(sentence['words']) for sentence in sentence_stats)
    total_character_count = sum(len(sentence['text']) for sentence in sentence_stats)
    average_word_length = total_character_count / total_word_count
    average_sentence_word_count = total_word_count / len(sentence_stats)

    if display_stats:
        display_txt_file_statistics({'word count': total_word_count, 
                                    'character count': total_character_count, 
                                    'average word length': average_word_length,
                                    'average words in a sentence': average_sentence_word_count})

def analyse_file_txt(file_name, sentence_delimiters, omission_list=None):
    # read the file
    full_text = ''
    with open(file_name, mode='r', encoding='utf-8') as txt_file:
        full_text = txt_file.read()

    # process the file's text into a list of sentences
    SENTENCE_DELIMITERS = sentence_delimiters
    sentences_text = text_to_sentences(full_text, SENTENCE_DELIMITERS)

    # generate a list of dictionaries each holding statistics about a sentence
    sentence_stats = []
    NON_SPACE_WHITESPACE = ('\n', '\t', '\r', '\f', '\v')
    SYMBOLS = ('~', '@', '#', '$', '%', '^', '*', '_', '-', '+', '=', '{', '[', '}', ']', '|', '<', '>', '/')
    SENT_END_PUNCT = ('!', '.', '?')
    OTHER_PUNCTUATION = ('\"', '\'', '`', '&', '(', ')', ':', ';', ',')
    BAD_CHARS = ''.join(NON_SPACE_WHITESPACE + SYMBOLS + SENT_END_PUNCT + OTHER_PUNCTUATION)

    for sentence in sentences_text:
        sentence_stats.append(generate_sentence_dict(sentence, BAD_CHARS))

    # calc statistics about the text in the file
    calc_text_stats(sentence_stats, display_stats=True)

def main():
    change_working_dir() #ensure python working directory is the folder where this script resides.

    FILENAME = 'remarks.txt' # assumes same folder as this script
    ##WORD_OMISSIONS = ['(Applause.)', 'THE PRESIDENT:', 'AUDIENCE:', 'END']
    WORD_OMISSIONS = None
    SENTENCE_DELIMITERS = ['  ','.\n', '\n\n']

    analyse_file_txt(FILENAME, SENTENCE_DELIMITERS, WORD_OMISSIONS)

    pass

if __name__ == '__main__':
    main()