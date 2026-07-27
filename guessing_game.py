#This is number guessing game made for fun
#the game start here
import random

print('******* Hey there! Welcome to this fun guessing game!***')

def start_game():
    number_of_attempt = []
    while True:

        user_input = input('Please, choose a number: ')
        user_input = int(user_input)
        random_number = random.randint(1,10)
        
        number_of_attempt.append(user_input)
        total_number_of_attempts = len(number_of_attempt)


        if user_input > random_number:
            print("It's lower")
        elif user_input < random_number:
            print("It's higher")
        elif user_input == random_number:
            print('Got it')
            print(f'You made {total_number_of_attempts } attempts ')
            print()
            print('*** GAME OVER!! ***')
            break
        
    
start_game()
#The game ends here!!




