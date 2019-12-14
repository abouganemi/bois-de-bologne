import os
import cx_Oracle
import matplotlib.pyplot as plt

os.chdir("C:\\instantclient_18_5")

# Connection string
connection = cx_Oracle.connect("hr", "inf5180", "144.217.163.57/XE")

sql = "SELECT job_title, avg(SALARY) " \
      "FROM EMPLOYEES E JOIN JOBS J " \
      "ON E.JOB_ID = J.JOB_ID group by JOB_TITLE"

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
plt.xlabel("Job Title")
plt.ylabel("Average Salary")
plt.title("Average Salary per Job Title")

plt.show()
