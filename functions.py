def get_puzzle():
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
    puzzle.strip()
    return puzzle
