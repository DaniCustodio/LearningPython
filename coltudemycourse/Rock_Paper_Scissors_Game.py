from random import randint

player_score = 0
ai_score = 0
winning_score = 2

while player_score < winning_score and ai_score < winning_score:
    print('\nRock...')
    print('Paper...')
    print('Scissors...')
    print(f'PLAYER SCORE: {player_score} | AI SCORE: {ai_score}')

    p1 = input('Player 1, make your move: ').lower()
    
    if p1 == 'quit' or p1 == 'q':
        break
    
    while p1 != 'rock' and p1 != 'paper' and p1 != 'scissors':
        print('Please enter a valid move!')
        p1 = input('Player 1, make your move: ').lower()

    rand_num = randint(1,4)
    if rand_num == 1:
        p2 = 'rock'
    elif rand_num == 2:
        p2 = 'paper'
    else:
        p2 = 'scissors'
    print(f'The AI plays {p2}')

    if p1 == p2:
        print('It\'s a tie!')
    elif p1 == 'rock':
        if p2 == 'scissors':
            print('Player 1 Wins!')
            player_score += 1
        elif p2 == 'paper':
            print('AI Wins!')
            ai_score += 1
    elif p1 == 'scissors':
        if p2 == 'paper':
            print('Player 1 Wins!')
            player_score += 1
        elif p2 == 'rock':
            print('AI Wins!')
            ai_score += 1
    elif p1 == 'paper':
        if p2 == 'rock':
            print('Player 1 Wins!')
            player_score += 1
        elif p2 == 'scissors':
            print('AI Wins!')
            ai_score += 1
    else:
        print('Something went wrong')

print(f'\nFINAL SCORE... Player : {player_score} | AI: {ai_score}')
if player_score > ai_score:
    print('CONGRATULATIONS YOU WON!')
elif player_score == ai_score:
    print('IT\'S A TIE!')
else:
    print('ON NO! YOU LOST :(')