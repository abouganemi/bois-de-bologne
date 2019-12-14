import os
import cx_Oracle
import matplotlib.pyplot as plt

os.chdir("C:\\instantclient_18_5")

# Connection string
connection = cx_Oracle.connect("hr", "inf5180", "144.217.163.57/XE")

sql = "SELECT department_id, count(*) " \
      "FROM employees group by department_id"

curs = connection.cursor()
curs.execute(sql)
departments = []
name = []

for row in curs:
    departments.append(row[0])
    name.append(row[1])

curs.close()
connection.close()

plt.scatter(departments, name, marker="o", color="blue")

plt.show()
