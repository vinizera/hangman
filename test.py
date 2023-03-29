import random

print('hangman, the game')

words = ['schutz', 'santa lolla', 'arezzo', 'forever 21', 'charlotte russe']
#words_bet = ['flamengo', 'ponte preta', 'vasco da gama', 'gama', 'nautico', 'corinthians', 'athletico paranaense']

hides = [('_ '*len(i)) for i in words]
hides = [i.strip() for i in hides]

