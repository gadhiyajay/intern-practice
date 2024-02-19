# # # # # def acc_val(a, b):
# # # # #     pass
# # # # #     def add_min(a, b):
# # # # #         return a+b
# # # # #     add = add_min(a, b)
# # # # #     return add + 5
# # # # # x = int(input("Enter the first number"))
# # # # # y = int(input("Enter the second number"))
# # # # # res = acc_val(x,y)
# # # # # print(res)
# # # # #
# # # # res = [i for i in range(25) if i%2==0]
# # # # print(res)
# # # for arg in args:
# # #     print(arg)
# # def ex_fun(*args) -> int:
# #     """
# #     This function return the argument values that are obtained from user
# #
# #     """
# #     print(ex_fun.__annotations__)
# #     print(arg**2 for arg in args)
# #
# # ex_fun(1,2,3,4,5)
# # print(ex_fun.__doc__)
# def my_function(a, b, /, c, d):
#     print(a, b, c, d)
#
# # Call the function using positional arguments
# my_function(1, 2, 3, 4)
# qua = 10
# price = 25.56546132465
# print(f"Cost is {qua * price:.2f}")
# def make_incrementor(n):
#     return lambda x : x + n
# f = make_incrementor(45)
# print(f(0))
#
# print(f(35))
# list1 = [1,2,3,4,5,6,7,8,9,10]
# res = list(map(lambda x:x+10,list1))
# print(res)
# x = lambda a, b, c : a+b+c
# print(x(9,5, 4))
# import sys
#
# user1 = input("What's your name?")
# user2 = input("And your name?")
# user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
# user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)
#
# def compare(u1, u2):
#     if u1 == u2:
#         return("It's a tie!")
#     elif u1 == 'rock':
#         if u2 == 'scissors':
#             return("Rock wins!")
#         else:
#             return("Paper wins!")
#     elif u1 == 'scissors':
#         if u2 == 'paper':
#             return("Scissors win!")
#         else:
#             return("Rock wins!")
#     elif u1 == 'paper':
#         if u2 == 'rock':
#             return("Paper wins!")
#         else:
#             return("Scissors win!")
#     else:
#         return("Invalid input! You have not entered rock, paper or scissors, try again.")
#         sys.exit()
#
# print(compare(user1_answer, user2_answer))
name = input("Enter the name of the User")
age = int(input(f"Enter the name of {name} "))
year = 2024 - age + 100
print(f"{name} you will be of 100 in {year}")