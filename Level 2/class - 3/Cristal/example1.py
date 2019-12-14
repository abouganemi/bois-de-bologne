import os

#cette étape peut être suprimmer si on ajoute le
#chemin a la variable d'environnement de Windows
os.chdir("C:\\instantclient_18_5")

#on importe notre module d'oracle
import cx_Oracle

#on ajoute une connexion avec l'utilisateur hr,
#le mot de passe inf5180
#et le serveur/service 144.217.163.57/XE

connection = None
curs = None
curs2 = None

try:

    connection = cx_Oracle.connect("hr", "inf5180", "144.217.163.57/XE")

    print("Connected to Oracle: " + connection.version)

    #variable = input("please enter region_id ")

    rows = [
        (1000,"1000"),
        (1001, "1001"),
        (1002, "1002"),
        (1003, "1003"),
        (1004, "1004"),
        (1005, "1005"),
        (1006, "1006"),
        (1007, "1007")]

    #on crée notre requête sur la forme d'une chaine de caractères
    #sql = "select * from regions where region_id > " + variable
    #sql = "select * from regions where region_id > : id "
    #sql = "select * from regions where region_id > : id and region_name like :name"
    #sql = "select e.first_name, e.last_name, d.department_name " \
    #      "from employees e left join departments d on d.department_id=e.department_id " \
    #      "order by e.first_name"
    sql = "update regions set region_name = :rname where region_id = :rid"

    # La classe de curseur permet au code Python d'exécuter la commande
    # Oracle dans une session de base de données.

    curs = connection.cursor()
    curs.executemany("insert into regions values (:1, :2)", rows)
    connection.commit()
    curs2 = connection.cursor()
    curs2.execute("select * from regions")
    res=curs2.fetchall()
    print(res)
    #curs.prepare(sql)

    # on exécute la commande
    #curs.execute(None)
    #curs.execute(sql)
    #curs.execute(sql, rid=57, rname='South America')

    #print(curs)

    #on parcoure l’ensemble des enregistrements résultants de la requête
    #for row in curs:
    #on affiche l’enregistrement
        #print(row)
        #print(row[0])
        #print(row[1])

    #for row in curs:
    #    for element in row:
    #        print(element)

except cx_Oracle.DatabaseError as e:
    print("Failed to insert row ", e)
    print(cx_Oracle.DatabaseError)

finally:
    if curs != None:
        curs.close()
    if curs2 != None:
        curs2.close()
    if connection != None:
        #connection.commit()
        connection.close()


