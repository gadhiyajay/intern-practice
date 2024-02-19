#  If  salary not entered by default it should return 9000
def emp(name, salary):

   return name, salary

a = input("Enter the employee's name")
b = input("Enter the employee's salary")
if b:
   b = int(b)
else:
   b = 9000
print(emp(a, b))