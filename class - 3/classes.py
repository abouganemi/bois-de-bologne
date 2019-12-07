import os
import cx_Oracle  # oracle module import
import datetime
from datetime import date
import re

os.chdir("C:\\instantclient_18_5")

connection = None
curs = None
# today = date.today().strftime("%d-%m-%Y")
today = date.today()


def insert_category(id, name):
    '''
    :param id: Category ID
    :param name: Name of the category
    :type id: int
    :type name: string
    '''
    try:
        # Connection string
        connection = cx_Oracle.connect("info33", "anypw", "144.217.163.57/XE")
        # Test if connection is ok
        print("Connected to Oracle: {}".format(connection.version))

        curs = connection.cursor()  # cursor
        sql = "INSERT INTO categories VALUES(:did, :dname)"  # SQL Query
        curs.execute(sql, did=id, dname=name)

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


def insert_user(username, password, last_name, name, email, creationdate,
                credit, phone, categoryid):

    # Connection string
    try:
        connection = cx_Oracle.connect("info33", "anypw", "144.217.163.57/XE")
        # Test if connection is ok
        print("Connected to Oracle: {}".format(connection.version))

        curs = connection.cursor()  # cursor
        # SQL Query
        sql = "INSERT INTO utilisateurs(username, password, nom, prenom, \
                email, creationdate, credit, telephone, categoryid) \
                VALUES(:dusername,:dpassword,:dlast_name,:dname, \
                    :demail, :dcreationdate, :dcredit, :dphone, :dcategoryid)"

        curs.execute(sql, dusername=username, dpassword=password,
                     dlast_name=last_name, dname=name, demail=email,
                     dcreationdate=creationdate, dcredit=credit,
                     dphone=phone, dcategoryid=categoryid)

    except cx_Oracle.DatabaseError as ORA:
        print("Failed inserting records")
        print(cx_Oracle.DatabaseError, ORA)

    finally:
        # close the cursor
        if curs is not None:
            curs.close()

        # close the connection
        if connection is not None:
            connection.commit()
            connection.close()


# insert_category(500, "Computer")

# insert_user("pepe", "pepito01$", "Abouganem", "Isaac",
#             "pepe@gmail.com", today, 10.05, "5145555557", 500)

def user_input_category():
    while True:
        input_id = input("Please insert the ID as number: ")
        id = validate_integer(input_id)

        if id:
            break
        else:
            print("Please enter a valid number.")
            continue

    while True:
        input_name = input("Please insert the category name: ")
        name = validate_string(input_name)

        if name:
            break
        else:
            print("Please enter a valid name. Cannot contains numbers")
            continue

    insert_category(input_id, input_name)


def user_input_user():
    while True:
        input_username = input("Please insert the username: ")
        username = validate_alpha_numeric(input_username)

        if username:
            break
        else:
            print("Please enter a valid username.")
            continue

    while True:
        input_password = input("Please insert a password: ")
        name = validate_string(".+[A-Za-z0-9].+", input_password)

        if name and input_password.__len__() <= 15:
            break
        else:
            print("Please enter a valid name. Cannot contains numbers")
            continue


def validate_integer(regex, characters):
    '''
    Function to validate integer
    :param characters: Chain of characters to be evaluated aginst regex
    :return: Bool
    '''
    # "^[0-9]+$"
    result = re.match(regex, characters)
    if result:
        return True
    else:
        return False


def validate_string(regex, characters):
    '''
    Function to validate integer
    :param characters: Chain of characters to be evaluated against regex
    :return: Bool
    '''
    # "^[A-Za-z]+$"
    result = re.match(regex, characters)
    if result:
        return True
    else:
        return False


def validate_alpha_numeric(regex, characters):
    '''
    Function to validate integer
    :param characters: Chain of characters to be evaluated against regex
    :return: Bool
    '''
    # "^[A-Za-z0-9]+$"
    result = re.match(regex, characters)
    if result:
        return True
    else:
        return False



