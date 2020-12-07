import random
from collections import defaultdict
from pronouncing import phones_for_word, syllable_count


def countable_corpus(corpus):

    '''
    Function to convert a corpus to a Markov dictionary where all of the words
    are "countable", i.e. they appear in the CMU dictionary associated with the
    `pronouncing` package and thus their syllables and phonemes can be counted
    and utilized.

    This is necessary for generators that have syllabic constraints.


    Input
    -----
    corpus : str
        Corpus as one long string.


    Output
    ------
    text_dictionary : dict [str, list (str)]
        Markov dictionary with each (countable) word that appears in the corpus
        as keys, with each value being a list of (countable) words that follow
        that key.

    '''

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

    '''
    Function to choose a random word that is less than or equal to syllabic
    contraint (`num_syllables`).

    NOTE: uses recursion; if a RecursionError occurs, the default output is
    `'the'`.


    Input
    -----
    word_list : list (str)
        List of words to choose from.
        NOTE: list must be comprised of "syllabically countable" words.

    num_syllables : int
        Maximum number of syllables for output word.


    Output
    ------
    word : str
        Word that is less than or equal to `num_syllables`.

    count : int
        Number of syllables in output word.


    '''

    # instantiate count of iterations
    iters = 0

    # number of words in input list
    n = len(word_list)

    # randomly choose a word
    word = random.choice(word_list)

    # count number of syllables in that word
    count = syllable_count(phones_for_word(word)[0])

    # limit number of iterations to two times the length of the list
    # (given randomness, this will generally allow for each word in the list
    # to be tried)
    while iters < 2*n:

        # return word and count if syllabic constraint is satisfied
        if count <= num_syllables:
            return word, count

        # add to iterations if syllabic constraint is not satisfied and try 
        # again
        else:
            iters += 1
            continue

    # if number of iterations is exceeded, try again
    try:
        return word_grabber(word_list, num_syllables)
    # if recursion limit is met, return 'the' and its syllable count
    except RecursionError:
        return ('the', 1)


def line_creator(word_dict, num_syllables, prompt=None):

    '''
    Function to create a string of text that satisfies a syllabic contraint
    (`num_syllables`).


    Input
    -----
    word_dict : dict [str, list (str)]
        Syllabically countable Markov dictionary.

    num_syllables : int
        Target number of syllables for output string.


    Optional Input
    --------------
    prompt : str
        Word to use as key, whose value is used to randomly choose the first
        word in the line.


    Output
    ------
    line : list (str)
        List of words whose syllables add up to `num_syllables`.

    '''

    # instantiate empty list and syllable count
    line = []
    count = 0

    # define list of words using prompt
    if prompt:
        word_list = word_dict[prompt]

    # define list of words without prompt
    else:
        word_list = [word for word in list(word_dict.keys())
                     if phones_for_word(word)]

    # randomly choose first word and update count
    word, count = word_grabber(word_list, num_syllables)

    # add word to list
    line.append(word)

    # loop until syllablic constraint is met
    while count < num_syllables:

        # randomly choose following word and its syllable count
        next_word, update = word_grabber(word_dict[line[-1]],
                                         num_syllables-count)

        # add word to list
        line.append(next_word)

        # update count
        count += update

    return line


def tankanizer(word_dict, start_word=None, non_enders=None):

    '''
    Function to create a string in the tanka form, which has syllabic
    constraints of 5-7-5-7-7 syllables per line.


    Input
    -----
    word_dict : dict [str, list (str)]
        Syllabically countable Markov dictionary.


    Optional Input
    --------------
    start_word : str
        Word to use as key, whose value is used to randomly choose the first
        word in the poem.

    non_enders : list (str)
        Words to disallow from being the final word in the generated text.
        NOTE: To satisfy the syllabic constraint, this only works using (and
              replacing) monosyllabic words.


    Output
    ------
    tanka : str
        Syllabically-constrained poem as one string.

    '''

    # create first line, with optional word to start with
    line_1 = line_creator(word_dict, 5, start_word)

    # create following lines, using the last word of the previous line as the
    # prompt word for the first word in the next line
    line_2 = line_creator(word_dict, 7, line_1[-1])
    line_3 = line_creator(word_dict, 5, line_2[-1])
    line_4 = line_creator(word_dict, 7, line_3[-1])
    line_5 = line_creator(word_dict, 7, line_4[-1])

    # to prevent ending in certain (monosyllabic) words
    if non_enders:

        # look at final word
        end_word = line_5[-1]

        # replace if in the forbidden list
        if end_word in non_enders:

            # word list without certain (monosyllabic) words
            valid_enders = [word for word in word_dict[end_word] if
                            (word not in non_enders) &
                            (syllable_count(phones_for_word(word)[0]) == 1)]

            # replace with a different monosyllabic word within the previous word's list
            if valid_enders:
                line_5[-1] = word_grabber(valid_enders, 1)[0]

            # if there are no viable options within the previous word's list, then choose
            # a random monosyllabic word from the corpus's dictionary
            else:
                choices = [word for word in list(word_dict.keys()) if
                            (word not in non_enders) &
                            (syllable_count(phones_for_word(word)[0]) == 1)]
                line_5[-1] = random.choice(choices)

    # list of lists
    lines = [line_1, line_2, line_3, line_4, line_5]

    # convert each line to space-separated string
    tanka_lines = [' '.join(line) for line in lines]

    # join strings with newline characters
    tanka = '\n'.join(tanka_lines)

    return tanka
