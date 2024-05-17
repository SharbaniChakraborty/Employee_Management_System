import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="******",database="employee_management_sys")
c=mydb.cursor()
login = False
department_id = input("Enter department id:")
department_name = input("Enter Department Name:")

c.execute("select * from department;")
#to retrieve data
for row in c:
    if(department_id == row[0] and department_name == row[1]):
        login = True
        break

if(login):
    print("Login Successful")
else:
    print("Incorrect name or id")
