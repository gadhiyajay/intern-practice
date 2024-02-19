import random

def show_score(attempts_list):
    if not attempts_list:
        print('There is currently no best score, It\'s yours for the talking')
    else:
        print(f'The current best score is'
              f'{min(attempts_list)} attempts')

def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    attempts_list = []

    print('Hello Traveller! Welcome to the game of guesses!')
    player_name = input("Enter your name : ")
    wanna