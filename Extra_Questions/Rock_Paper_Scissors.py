import random

lst = ["Rock", "Paper", "Scissors"]
rand_input = random.choice(lst)

user_input = input("Enter your move(Rock, Paper, Scissors)")
for i in user_input:
    if user_input not in lst:
        print("Invalid Input!")
        exit()
if user_input == rand_input:
    print(f"The User's move was :{user_input} and the computer's move was :{rand_input}")
    print("It's a draw!!")
elif user_input == "Rock" and rand_input == "Scissors":
    print(f"The User's move was :{user_input} and the computer's move was :{rand_input}")
    print("The User wins")
elif user_input == "Paper" and rand_input == "Rock":
    print(f"The User's move was :{user_input} and the computer's move was :{rand_input}")
    print("The User wins")
elif user_input == "Scissors" and rand_input == "Paper":
    print(f"The User's move was :{user_input} and the computer's move was :{rand_input}")
    print("The User wins")
else:
    print(f"The User's move was :{user_input} and the computer's move was :{rand_input}")
    print("Computer Wins!")
