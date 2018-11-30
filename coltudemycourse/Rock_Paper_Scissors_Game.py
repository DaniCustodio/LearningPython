print('...rock...')
print('...paper...')
print('...scissors...')

print('Enter Player 1\' choice: ')
p1 = input()

print('Enter Player 2\' choice:')
p2 = input()

print('SHOOT!')

if p1 and p2:
    if p1 == 'rock':
        if p2 == 'scissors':
            print('Player 1 Wins!')
        elif p2 == 'paper':
            print('Player 2 Wins!')
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
            print('Player 2 Wins!')
        else:
            print('Invalid Option!')
    elif p1 == 'paper':
        if p2 == 'scissors':
            print('Player 2 Wins!')
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
