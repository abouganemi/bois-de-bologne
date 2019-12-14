import os
import cx_Oracle  # oracle module import

os.chdir("C:\\instantclient_18_5")

connection = None
curs = None

# Connection string
try:
    connection = cx_Oracle.connect("hr", "inf5180", "144.217.163.57/XE")
    # Test if connection is ok
    print("Connected to Oracle: {}".format(connection.version))

    sql = "SELECT e.first_name, e.last_name, d.department_name \
            FROM EMPLOYEES e \
            LEFT JOIN DEPARTMENTS d on d.department_id = e.department_id \
            ORDER BY department_name asc, e.first_name desc"

    curs = connection.cursor()
    curs.prepare(sql)

    # None means it will use the same statamenet from curs.prepare
    curs.execute(None)

    for row in curs:
        for element in row:
            print(element)

except cx_Oracle.DatabaseError as ORA:
    print("Failed select row")
    print(cx_Oracle.DatabaseError, ORA)

finally:
    # close the cursor
    if curs is not None:
        curs.close()

    # close the connection
    if connection is not None:
        connection.close()
