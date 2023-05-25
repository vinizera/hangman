def get_puzzle():
    """

    :return: returns a tuple containing the word[0], it's enigma[1], and it's splitted array enigma[2]
    """
    import json
    import random

    with open('wordbank.json', 'r') as file:
        data = json.load(file)
        # gets a random value from the data keys (str) and take it as a tip:
        tip = random.choice(list(data.keys()))
        # gets a random value from the selected key (int) and take it as an index:
        word = data[tip][random.randrange(len(data[tip]))]

    splits = [' ' if letter == ' ' else '_' for letter in word]
    enigma = ' '.join(splits)

    return word, enigma, splits, tip


def get_index(guess, word, in_list, off_list):

    # list containing the indexes of guess letters
    to_index = list()

    # variable to check if you count the try or not
    count = True

    if (guess in word) and (guess not in in_list):
        # why not a set?
        in_list.append(guess)
        for c, v in enumerate(word):
            if v == guess:
                to_index.append(c)
        print('\033[32mright answer!\033[m')
    elif guess in in_list:
        count = False
        print('\033[31manswer already given!\033[m')
    elif guess not in word and guess not in off_list:
        off_list.append(guess)
        print('\033[31mwrong answer!\033[m')
    elif guess not in word and guess in off_list:
        count = False
        print('\033[31mwrong answer already given!\033[m')

    # returns the index list
    return to_index, count


def get_hangman(misses):
    if misses == 0:
        print('      ____ \n'
              '     |     \n'
              '     |     \n'
              '     |     \n'
              '_____|_____')
    elif misses == 1:
        print('      ____  \n'
              '     |   O  \n'
              '     |      \n'
              '     |      \n'
              '_____|______')
    elif misses == 2:
        print('      ____  \n'
              '     |   O  \n'
              '     |   |  \n'
              '     |      \n'
              '_____|______')
    elif misses == 3:
        print('      ____  \n'
              '     |   O  \n'
              '     |  /|\ \n'
              '     |      \n'
              '_____|______')
    elif misses == 4:
        print('      ____  \n'
              '     |   O  \n'
              '     |  /|\ \n'
              '     |  / \ \n'
              '_____|______')
