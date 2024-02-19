import mysql.connector


def get_connection():
    connection = mysql.connector.connect(host="localhost", database="Jay", user="root", password="1234")
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def get_hospital_details(Hospital_Id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (Hospital_Id,))
        records = cursor.fetchall()
        print("Printing Hospital Records")
        for row in records:
            print("Hospital Id :", row[0], )
            print("Hospital Name :", row[1])
            print("Bed Count :", row[2])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


def get_doctor_detail(Doctor_Id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Doctor_Id = %s"""
        cursor.execute(select_query, (Doctor_Id,))
        records = cursor.fetchall()
        print("Printing Doctor Records")
        for row in records:
            print("Doctor ID :", row[0])
            print("Doctor Name :", row[1])
            print("Hospital ID :", row[2])
            print("Joining Date :", row[3])
            print("Speciality :", row[4])
            print("Salary :", row[5])
            print("Experience :", row[6])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


print("List of hospital and doctor details :")
get_hospital_details(2)
print("\n")
get_doctor_detail(105)
