from random import randint

print('...rock...')
print('...paper...')
print('...scissors...')

print('Enter Player 1 choice: ')
p1 = input()

rand_num = randint(1,4)
p2 = None

if rand_num == 1:
    p2 = 'rock'
elif rand_num == 2:
    p2 = 'paper'
else:
    p2 = 'scissors'

print('AI choice = ' + p2)

print('SHOOT!')

if p1 and p2:
    if p1 == 'rock':
        if p2 == 'scissors':
            print('Player 1 Wins!')
        elif p2 == 'paper':
            print('AI Wins!')
        elif p2 == 'rock':
            print("It\'s a drawn!")
        else:
            print('Invalid Option!')
    elif p1 == 'scissors':
        if p2 == 'scissors':
            print("It\'s a drawn!")
        elif p2 == 'paper':
            print('Player 1 Wins!')
        elif p2 == 'rock':
            print('AI Wins!')
        else:
            print('Invalid Option!')
    elif p1 == 'paper':
        if p2 == 'scissors':
            print('AI Wins!')
        elif p2 == 'paper':
            print("It\'s a drawn!")
        elif p2 == 'rock':
            print('Player 1 Wins!')
        else:
            print('Invalid Option!')
    else:
        print('Invalid Option!')
else:
    print('You didn\'t enter a choice!')
