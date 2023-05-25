import functions

print('\033[1mhangman, the game\033[m')

quest = functions.get_puzzle()

word = quest[0]
enigma = quest[1]
splits = quest[2]
tip = quest[3]


def get_enigma():
    print(f'guess a {tip}: {enigma}')


in_list, off_list = list(), list()

game = True
misses = 0
while game:
    from time import sleep
    if misses >= 4:
        print('YOU LOSE! leaving game...')
        sleep(3)
        break
    functions.get_hangman(misses)
    get_enigma()
    guess = input('your try: ')
    try:
        guess = guess[0].lower()
    except IndexError:
        print('\033[31mtry a letter/number\033[m')
        continue

    if guess == ' ':
        if ' ' in word:
            print('\033[31mcan\'t you see the blank spaces?\033[m')
        else:
            print('\033[31mthere is no blank spaces!\033[m')
        continue

    # list of current state of puzzle: [0]
    # boolean value to check if the try counts or not: [1]
    guess_index, doCount = functions.get_index(guess, word, in_list, off_list)

    if len(guess_index) != 0:
        for x in guess_index:
            splits[x] = guess
    elif doCount:
        misses += 1

    enigma = ' '.join(splits)

    while '_' not in enigma:
        print(enigma)
        print('YOU WIN! leaving game...')
        sleep(3)
        game = False
        break

