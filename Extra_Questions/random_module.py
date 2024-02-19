import random

sum = 0
sum1 = 0
count = 0
flag = 0

while(1):

    r1 = random.randrange(1, 10)
    r2 = random.randrange(1, 10)

    sum = sum + r1
    sum1 = sum1 + r2
    count = count + 1

    print("Total score of Player 1 after turn %d is : %d" % (count, sum))

    if(sum >= 100):
        flag = 1
        break
    print("Total score of Player 2 after turn %d is : %d" % (count, sum1))

    if (sum1 >= 100):
        flag = 2
        break

if(flag == 1):
    print("Player 1 wins the game")
else:
    print("Player 2 wins the game")