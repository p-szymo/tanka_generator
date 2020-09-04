import requests
import json
import string
import re
import random
from pronouncing import phones_for_word, syllable_count

## call API and create a list of authors
def author_grabber(url):
#     url = "http://poetrydb.org/author"
    authors = requests.get(url)
    authors = [author for author in authors.json()['authors']]
    return authors


## call API and create a list of poem titles for each author
def title_grabber(author):
    base_url = "http://poetrydb.org/author/"
    url_addon = (author + '/title').replace(" ", "%20")
    try:
        titles = requests.get(base_url + url_addon)
        titles = [title['title'] for title in titles.json()]
    except:
        print(author)
        pass
    return titles


## call API and create a list of the lines of a poem
## convert list to a string, joining them with '\n' 
def poem_grabber(title):
    base_url = 'http://poetrydb.org/title/'
    url_addon = (title + '/lines.json').replace(" ", "%20").replace(')', '').replace(']', '').split('/', 1)[0].split('^', 1)[0]
    try:
        response = requests.get(base_url + url_addon)
        lines = response.json()[0]['lines']
        poem = " \n ".join(lines).lower()
        poem = poem.translate(str.maketrans('', '', string.punctuation)).replace(
            '  ', ' \t ').replace('—', '').replace('‘','').replace('’','')
    except:
        print(title)
        pass
    return poem


## temporarily change newline and tab characters so they don't disappear during segmentation
def lines_tabs_creator(po_dict):
    new_line = 'airplane'
    tab = 'automobile'
    for word, followers in po_dict.items():
        for i,follower in enumerate(followers):
            if follower == new_line:
                followers[i] = '\n'
            elif follower == tab:
                followers[i] = '\t'
            else:
                continue
    return po_dict


## ask the user to provide a length for the poem (in numerals)
def word_quantifier():
    while True:
        try:
            word_count = int(input("What length doth thy sweet nothings require? "))
            while word_count > 1000:
                word_count = int(input("Surely thine sweet nothings require less breadth!\nCease skylarking and present me a length of reason! "))
        except ValueError:
            print("Art thou a dullard? Enumerate!")
            continue
        else:
            break
    return word_count


## generate poetry from dictionary of words that appear in the PoetryDB's archive of poems
def tankanizer(po_dict):

    tanka = []
    line_1 = []
    line_2 = []
    line_3 = []
    line_4 = []
    line_5 = []
    
    syllables = 0
    while syllables == 0:
        first_word = random.choice(list(po_dict.keys()))
        syl_count = syllable_count(phones_for_word(first_word)[0])
        if syl_count <= 5:
            line_1.append(first_word)
            syllables += fw_syl_count
        else:
            continue
    
    while syllables < 5:
        next_word = random.choice(po_dict[line_1[-1]])
        syl_count = syllable_count(phones_for_word(next_word)[0])
        if syl_count <= (5 - syllables):
            line_1.append(next_word)
            syllables += fw_syl_count
        else:
            continue
    
    print((' ').join(line_1))
#         while syl_count
#         syllable_count < (5 - fw_syl_count)

#     while len(auto_pome) < word_count:
#         next_word = random.choice(po_dict[auto_pome[-1]])
#         auto_pome.append(next_word)
#     print('\n\n\n ' + (' ').join(auto_pome))
    
# pronunciation_list = pronouncing.phones_for_word("programming")
# pronouncing.syllable_count(pronunciation_list[0])