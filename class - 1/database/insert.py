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
    curs = connection.cursor()

    sql = "UPDATE REGIONS SET region_name = :dname WHERE region_id = :deptno"
    curs.execute(sql, deptno=55, dname='ZAIER')

except cx_Oracle.DatabaseError as ORA:
    print("Failed select row")
    print(cx_Oracle.DatabaseError, ORA)

finally:
    # close the cursor
    if curs is not None:
        curs.close()

    # close the connection
    if connection is not None:
        connection.commit()
        connection.close()
