import os
import cx_Oracle  # oracle module import

os.chdir("C:\\instantclient_18_5")

con = None
cur = None
cur2 = None

# Connection string
try:
    con = cx_Oracle.connect("hr", "inf5180", "144.217.163.57/XE")
    # Test if connection is ok
    print("Connected to Oracle: {}".format(con.version))
    rows = [(500, "First"),
            (510, "Second"),
            (520, "Third"),
            (530, "Fourth"),
            (540, "Fith"),
            (550, "Sixth"),
            (560, "Seventh")]
    
    cur = con.cursor()
    # On cree une requete parametree d'execution multiple avec execute many
    # on passe aussi la iste d'insertions - rows en parametre
    cur.executemany("insert into regions values (:1, :2)", rows)
    con.commit()
    cur2 = con.cursor()
    cur2.execute('select * from regions')
    res = cur2.fetchall()
    print(res)

except cx_Oracle.DatabaseError as ORA:
    print("Failed select row")
    print(cx_Oracle.DatabaseError, ORA)

finally:
    # close the cursor
    if cur is not None:
        cur.close()
    if cur2 is not None:
        cur2.close()

    # close the connection
    if con is not None:
        con.close()
