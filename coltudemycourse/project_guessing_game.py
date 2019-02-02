from random import randint

while True:
    print('-------------GUESSING GAME-------------')

    random_number = randint(1,10)

    user_guess = None

    while user_guess != random_number:
        user_guess = int(input('Guess a number between 1 and 10: '))
        
        if user_guess > random_number:
            print('Too high! Try again.')
        elif user_guess < random_number:
            print('Too low! Try again.')
        else:
            print('You guessed it! You won!')  
    
    continue_playing = input('Do you want to keep playing? (y/n) ')
    if(continue_playing == 'n'):
        print('Thanks for playing. Bye!')
        break

