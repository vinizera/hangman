def get_puzzle():
    """

    :return: returns a tuple containing the word[0] and it's enigmated code[1]
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
    else:
        off_list.append(guess)
        #print('no')

    # returns the index list
    return to_index
