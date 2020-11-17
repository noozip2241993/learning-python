from my_functions import change_working_dir
from my_functions import text_to_sentences
from my_functions import generate_sentence_dict
from my_functions import display_dict

def calc_text_stats(list_of_sentence_dicts, display_stats=False):
    sentence_stats = list_of_sentence_dicts
    total_word_count = sum(len(sentence['words']) for sentence in sentence_stats)
    total_character_count = sum(len(sentence['text']) for sentence in sentence_stats)
    average_word_length = total_character_count / total_word_count
    average_sentence_word_count = total_word_count / len(sentence_stats)

    result = {'word count': total_word_count,
                'character count': total_character_count,
                'average word length': average_word_length,
                'average words in a sentence': average_sentence_word_count}

    if display_stats:
        display_dict(result)
    
    return result

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

    # calc statistics about the text in the file and display them
    calc_text_stats(sentence_stats, display_stats=True)

def main():
    change_working_dir() #ensure python working directory is the folder where this script resides.
    FILENAME = 'remarks.txt' # assumes same folder as this script
    WORD_OMISSIONS = None
    #WORD_OMISSIONS = ['(Applause.)', 'THE PRESIDENT:', 'AUDIENCE:', 'END']
    SENTENCE_DELIMITERS = ['  ','.\n', '\n\n']

    analyse_text_file(FILENAME, SENTENCE_DELIMITERS, WORD_OMISSIONS)

    pass

if __name__ == '__main__':
    main()