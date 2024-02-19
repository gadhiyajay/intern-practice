import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd='1234', port=3306, database='Jay')

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO student VALUES('JAY', 21)")
mycursor.execute("SELECT * FROM student")

for i in mycursor:
    print(i)

mydb.commit()