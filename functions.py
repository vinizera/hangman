def get_puzzle():
    """

    :return: returns a tuple containing the word[0] and it's enigmated code[1]
    """
    import random
    bank = ['schutz', 'santa lolla', 'arezzo', 'forever 21', 'charlotte russe']
    word = random.choice(bank)
    puzzle = ''
    print('guess the word: ')

    for i in word:
        if i != ' ':
            puzzle += '_ '
        else:
            puzzle += ' '
    puzzle = puzzle.strip()

    return word, puzzle
