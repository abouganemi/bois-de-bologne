import os
import cx_Oracle
import matplotlib.pyplot as plt

os.chdir("C:\\instantclient_18_5")

# Connection string
connection = cx_Oracle.connect("hr", "inf5180", "144.217.163.57/XE")

sql = "SELECT department_name, count(*) " \
      "FROM employees E JOIN departments D " \
      "ON E.department_id=D.department_id GROUP BY department_name"

curs = connection.cursor()
curs.execute(sql)
departments = []
name = []

for row in curs:
    departments.append(row[0])
    name.append(row[1])

curs.close()
connection.close()

plt.bar(departments, name, color="red")
plt.xticks(departments, rotation="vertical")
plt.xlabel("Departments")
plt.ylabel("Employee Names")
plt.title("Employees per department")

plt.show()
