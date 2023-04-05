import functions

print('\033[1mhangman, the game\n\033[m')


quest = functions.get_puzzle()

word = quest[0]
enigma = quest[1]

in_list, off_list = list(), list()

print(enigma)

while True:

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

    if guess in (in_list or off_list):
        print('\033[31mword already given!\033[m')
        continue

    rest = functions.get_index(guess, word, in_list, off_list)
    print(rest)