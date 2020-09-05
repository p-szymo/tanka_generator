import requests
import json
import string
import re
import random
from pronouncing import phones_for_word, syllable_count


def value_tester(values):
    valid = False
    for word in values:
        if phones_for_word(word):
            valid = True
            break
        else:
            continue
    return valid


def line_creator(word_dict, num_syllables, prompt=None):
    '''Input a dictionary in the format of key = current word, value = list of next words
       along with the number of words you would like to see in your generated sentence.'''
    
    line = []
    count = 0
    
    if prompt:
        while count == 0:
            try:
                start_word = random.choice(word_dict[prompt])
                count = syllable_count(phones_for_word(start_word)[0])
                if count <= num_syllables:
                    line.append(start_word)
                else:
                    count = 0
                    continue
            except IndexError:
                continue
              
    else:
        while count == 0:
            try:
                start_word = random.choice(list(word_dict.keys()))
                count = syllable_count(phones_for_word(start_word)[0])
                if count <= num_syllables:
                    line.append(start_word)
                else:
                    count = 0
                    continue
            except IndexError:
                print('initial word index error')
                count = 0
                continue

    while count < num_syllables:
#         try:
        next_word = random.choice(word_dict[line[-1]])
        if not value_tester(word_dict[next_word]):
            next_word = 'the'
        temp_count = count + syllable_count(phones_for_word(next_word)[0])
        if temp_count <= num_syllables:
            line.append(next_word)
            count += syllable_count(phones_for_word(next_word)[0])
        else:
            continue
#         except IndexError:
#             print('next word index error')
#             count = count
#             continue
            
    return line


def line_creator_DEFUNCT(word_dict, num_syllables, prompt=None):
    '''Input a dictionary in the format of key = current word, value = list of next words
       along with the number of words you would like to see in your generated sentence.'''
    
    line = []
    count = 0
    
    if prompt:
        if not value_tester(word_dict[prompt]):
            prompt = 'the'
            
        while count == 0:
            try:
                start_word = random.choice(word_dict[prompt])
                count = syllable_count(phones_for_word(start_word)[0])
                if count <= num_syllables:
                    line.append(start_word)
                else:
                    count = 0
                    continue
            except IndexError:
                continue
              
    else:
        print('into else') 
        while count == 0:
            try:
                start_word = random.choice(list(word_dict.keys()))
#                 if value_tester(word_dict[start_word]):
                    
                count = syllable_count(phones_for_word(start_word)[0])
                if count <= num_syllables:
                    line.append(start_word)
                else:
                    count = 0
                    continue
            except IndexError:
                print('initial word index error')
                count = 0
                continue

    while count < num_syllables:
        try:
            next_word = random.choice(word_dict[line[-1]])
            if not value_tester(word_dict[next_word]):
                next_word = 'the'
            temp_count = count + syllable_count(phones_for_word(next_word)[0])
            if temp_count <= num_syllables:
                line.append(next_word)
                count += syllable_count(phones_for_word(next_word)[0])
            else:
                continue
        except IndexError:
            print('next word index error')
            count = count
            continue
            
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