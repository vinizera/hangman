def get_puzzle():
    """

    :return: returns a tuple containing the word[0], it's enigma[1], and it's splitted array enigma[2]
    """
    import random
    bank = ['forever 21', 'charlotte russe']
    word = random.choice(bank)

    splits = [' ' if letter == ' ' else '_' for letter in word]
    enigma = ' '.join(splits)

    return word, enigma, splits


def get_index(guess, word, in_list, off_list):

    # guess = input('your guess: ')

    # list containing the indexes of guess letters
    to_index = list()

    if guess in word:
        # why not a set?
        in_list.append(guess)
        count = 0
        for c, v in enumerate(word):
            if v == guess:
                to_index.append(c)
        #print('yeah')
    elif guess in in_list:
        print('\033[31mword already given!\033[m')
    elif guess not in word and guess not in off_list:
        off_list.append(guess)
        print('\033[31mwrong answer!\033[m')
        #print('no')
    elif guess not in word and guess in off_list:
        off_list.append(guess)
        print('\033[31mwrong answer already given!\033[m')

    # returns the index list
    return to_index


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
