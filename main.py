import functions

print('\033[1mhangman, the game\033[m')


quest = functions.get_puzzle()

word = quest[0]
enigma = quest[1]
splits = quest[2]


def get_enigma():
    print(enigma)


in_list, off_list = list(), list()

game = True
misses = 0
while game:
    if misses >= 4:
        print('YOU LOSE!')
        break
    functions.get_hangman(misses)
    get_enigma()
    guess = input('guess a word: ')
    try:
        guess = guess[0].lower()
    except IndexError:
        print('\033[31mtype a letter (a-z)\033[m')
        continue

    if guess == ' ':
        if ' ' in word:
            print('\033[31mcant you see the blank spaces?\033[m')
        else:
            print('\033[31mthere is no blank spaces!\033[m')
        continue

    guess_index = functions.get_index(guess, word, in_list, off_list)

    if len(guess_index) != 0:
        for x in guess_index:
            splits[x] = guess
    else:
        misses += 1

    enigma = ' '.join(splits)

    while '_' not in enigma:
        print(enigma)
        print('YOU WIN!')
        game = False
        break

