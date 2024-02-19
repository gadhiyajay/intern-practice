import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='Jay',
                                         user='root',
                                         password='1234')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_name(Hospital_Id):
    # Fetch Hospital Name using Hospital id
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(select_query, (Hospital_Id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

def get_doctors(Hospital_Id):
    # Fetch Hospital Name using Hospital id
    try:
        hospital_name = get_hospital_name(Hospital_Id)
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from Doctor where Hospital_Id = %s"""
        cursor.execute(sql_select_query, (Hospital_Id,))
        records = cursor.fetchall()

        print("Printing Doctors of ", hospital_name, "Hospital")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Hospital Name:", hospital_name)
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting doctor's data", error)

print("Question 4:  Get List of doctors of a given Hospital Id\n")
get_doctors(2)
