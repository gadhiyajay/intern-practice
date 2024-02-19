# USER REGISTRATION SIGN IN AND SIGN UP
from database import *
from customer import *
from bank import Bank
import random
def SignUp():
    username = input("Enter Your Username :")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username Already Taken!")
        SignUp()
    else:
        print("Username Available, Please Proceed.")
        password = input("Enter Your Password :")
        name = input("Enter Your Name :")
        age = int(input("Enter Your Age :"))
        city = input("Enter Your City :")
        while True:
            account_number = random.randint(10000000, 99999999)
            temp =  db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("YOUR ACCOUNT NUMBER :", account_number)
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()

    #SignUp()


def SignIn():
    username = input("Enter Username :")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")

    if temp:
        while True:
            password =  input(f"Welcome {username.title()} Enter your password : ")
            temp = db_query(f"SELECT password FROM customers WHERE username = '{username}';")
            if temp[0][0] == password:
                print("Signed In Successfully!")
                return username
            else:
                print("Wrong Password, Try Again!")
    else:
        print("No User Found!!!, Enter Correct Username")
        SignIn()