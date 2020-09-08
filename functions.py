import random
from collections import defaultdict
from pronouncing import phones_for_word, syllable_count



def countable_corpus(corpus):
    # instantiate a dictionary
    text_dictionary = defaultdict(list)

    # create Markov dictionary
    # iterate over list of each word and its subsequent word
    for current_word, next_word in zip(corpus, corpus[1:]):

        # append word to list as long as its phonemes can be counted
        if phones_for_word(next_word):
            text_dictionary[current_word].append(next_word)

        # otherwise choose a random word from the corpus whose phonemes can
        # NOTE: introduces some randomness! preventing assured reproducibility
        else:
            word = ''
            while not word:
                word = random.choice(corpus)
                if phones_for_word(word):
                    text_dictionary[current_word].append(word)
                else:
                    word = ''
                
    return text_dictionary


def word_grabber(word_list, num_syllables):
    
    iters = 0
    n = len(word_list)
    word = random.choice(word_list)
    count = syllable_count(phones_for_word(word)[0])
    while iters < 2*n:
        if count <= num_syllables:
            return word, count
        else:
            iters += 1
            continue
    
    try:
        return word_grabber(word_list, num_syllables)
    except RecursionError:
        return ('the', 1)
            

def line_creator(word_dict, num_syllables, prompt=None):
    '''Input a dictionary in the format of key = current word, value = list of next words
       along with the number of words you would like to see in your generated sentence.'''
    
    line = []
    count = 0
    
    if prompt:
        word_list = word_dict[prompt]
        
    else:
        word_list = [word for word in list(word_dict.keys()) if phones_for_word(word)]
              
    word, count = word_grabber(word_list, num_syllables)
    line.append(word)

    while count < num_syllables:
        
        next_word, update = word_grabber(word_dict[line[-1]], num_syllables-count)
        line.append(next_word)
        count += update 
            
    return line


def tankanizer(word_dict, start_word=None):

    line_1 = line_creator(word_dict, 5, start_word)
    line_2 = line_creator(word_dict, 7, line_1[-1])
    line_3 = line_creator(word_dict, 5, line_2[-1])
    line_4 = line_creator(word_dict, 7, line_3[-1])
    line_5 = line_creator(word_dict, 7, line_4[-1])
    lines = [line_1, line_2, line_3, line_4, line_5]
    tanka_lines = [(' ').join(line) for line in lines]
    tanka = '\n'.join(tanka_lines)
    
    return tanka



# def value_tester(values):
#     valid = False
#     for word in values:
#         if phones_for_word(word):
#             valid = True
#             break
#         else:
#             continue
#     return valid


# def line_creator_ORIGINAL(word_dict, num_syllables, prompt=None):
#     '''Input a dictionary in the format of key = current word, value = list of next words
#        along with the number of words you would like to see in your generated sentence.'''
    
#     line = []
#     count = 0
    
#     if prompt:
#         while count == 0:
#             try:
#                 start_word = random.choice(word_dict[prompt])
#                 count = syllable_count(phones_for_word(start_word)[0])
#                 if count <= num_syllables:
#                     line.append(start_word)
#                 else:
#                     count = 0
#                     continue
#             except IndexError:
#                 continue
              
#     else:
#         while count == 0:
#             try:
#                 start_word = random.choice(list(word_dict.keys()))
#                 count = syllable_count(phones_for_word(start_word)[0])
#                 if count <= num_syllables:
#                     line.append(start_word)
#                 else:
#                     count = 0
#                     continue
#             except IndexError:
#                 count = 0
#                 continue

#     while count < num_syllables:
        
#         next_word = random.choice(word_dict[line[-1]])
#         print(next_word)
# #         if not value_tester(word_dict[next_word]):
# #             next_word = 'the'
#         word_syll_count = syllable_count(phones_for_word(next_word)[0])
#         count += word_syll_count
#         if count <= num_syllables:
#             line.append(next_word)
#         else:
#             count -= word_syll_count
#             continue
# #         try:
# #         next_word = random.choice(word_dict[line[-1]])
# #         if not phones_for_word(next_word):
# #             next_word = 'the'
# #         print(next_word)
# #         temp_count = count + syllable_count(phones_for_word(next_word)[0])
# #         if temp_count <= num_syllables:
# #             line.append(next_word)
# #             count += syllable_count(phones_for_word(next_word)[0])
# #         else:
# #             continue
# #         except IndexError:
# #             print('next word index error')
# #             count = count
# #             continue
            
#     return line


# def line_creator_DEFUNCT(word_dict, num_syllables, prompt=None):
#     '''Input a dictionary in the format of key = current word, value = list of next words
#        along with the number of words you would like to see in your generated sentence.'''
    
#     line = []
#     count = 0
    
#     if prompt:
#         if not value_tester(word_dict[prompt]):
#             prompt = 'the'
            
#         while count == 0:
#             try:
#                 start_word = random.choice(word_dict[prompt])
#                 count = syllable_count(phones_for_word(start_word)[0])
#                 if count <= num_syllables:
#                     line.append(start_word)
#                 else:
#                     count = 0
#                     continue
#             except IndexError:
#                 continue
              
#     else:
#         print('into else') 
#         while count == 0:
#             try:
#                 start_word = random.choice(list(word_dict.keys()))
# #                 if value_tester(word_dict[start_word]):
                    
#                 count = syllable_count(phones_for_word(start_word)[0])
#                 if count <= num_syllables:
#                     line.append(start_word)
#                 else:
#                     count = 0
#                     continue
#             except IndexError:
#                 print('initial word index error')
#                 count = 0
#                 continue

#     while count < num_syllables:
#         try:
#             next_word = random.choice(word_dict[line[-1]])
#             if not value_tester(word_dict[next_word]):
#                 next_word = 'the'
#             count += syllable_count(phones_for_word(next_word)[0])
#             if count <= num_syllables:
#                 line.append(next_word)
#             else:
#                 count -= syllable_count(phones_for_word(next_word)[0])
#                 continue
#         except IndexError:
#             print('next word index error')
#             count = count
#             continue
            
#     return line