import random

print('\033[1mhangman, the game\n\033[m')

bank = ['schutz', 'santa lolla', 'arezzo', 'forever 21', 'charlotte russe']
word = random.choice(bank)


def get_puzzle():
    puzzle = ''
    print('guess the word: ')
    for i in word:
        if i != ' ':
            puzzle += '_ '
        else:
            puzzle += ' '
    puzzle.strip()
    return puzzle


print(get_puzzle())
