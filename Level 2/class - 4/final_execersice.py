import os
import cx_Oracle
import matplotlib.pyplot as plt
import re
from classes import *

os.chdir("C:\\instantclient_18_5")

connection = None
curs = None


def validate(regex, chars):
    '''
    Function to validate integers and chain of characters
    :param regex: Regular expression
    :param chars: Chain of characters to be evaluated aginst regex
    :return: Bool
    '''
    result = re.match(regex, chars)
    if result:
        return True
    else:
        return False


def insert_department():

    did = None
    dname = None
    dphone = None
    dpt = Department(did, dname, dphone)
    userInput = None  # Variable to capture the user's input

    while userInput != "no":
        while True:
            userInput = input("Please enter the department id: ")
            did = validate("^[0-9]+$", userInput)

            if did:
                dpt.did = userInput
                break
            else:
                print("Please enter a valid Number")

        while True:
            userInput = input("Please enter the department name: ")
            userInput = userInput.title()
            dname = validate("^[A-Za-z]{1,30}$", userInput)

            if dname:
                dpt.name = userInput
                break
            else:
                print("Please enter a valid Name")

        while True:
            userInput = input("Please enter the department phone number: ")
            dphone = validate("^([0-9]){3}-([0-9]){3}-([0-9]){4}$", userInput)

            if dphone:
                dpt.phone = userInput
                break
            else:
                print("Please enter a valid phone number")

        print("\n")
        print("Do you want to insert these values into the DB?: y/n ".format(
            dpt.print_info(dpt.did, dpt.name, dpt.phone)))
        userInput = input()

        if userInput == "n":
            pass
        else:
            try:
                # Connection string
                connection = cx_Oracle.connect(
                    "info33", "anypw", "144.217.163.57/XE")
                # Test if connection is ok
                print("Connected to Oracle: {}\n".format(connection.version))

                curs = connection.cursor()  # cursor
                # SQL Query
                sql = "INSERT INTO DEPARTEMENT(id, nom, telephone) \
                      VALUES(:did, :dname, :dphone)"

                curs.execute(sql, did=dpt.did, dname=dpt.name,
                             dphone=dpt.phone)
                print("Values inserted succesfully!\n")

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

        userInput = input("Do you want to add another department yes/no: ")


def insert_employee():
    # Variables for employee object
    eid = None
    last_name = None
    name = None
    salary = None
    email = None
    did = None
    post = None

    userInput = None  # Variable to capture the user's input
    emply = Employee(eid, last_name, name, salary, email, did, post)

    while userInput != "no":
        while True:
            userInput = input("Please enter the employee id: ")
            eid = validate("^[0-9]+$", userInput)

            if eid:
                emply.eid = int(userInput)
                break
            else:
                print("Please enter a valid Number")

        while True:
            userInput = input("Please enter the Employee last name: ")
            userInput = userInput.title()
            last_name = validate("^[A-Za-z]{1,30}$", userInput)

            if last_name:
                emply.last_name = userInput
                break
            else:
                print("Please enter a valid name")

        while True:
            userInput = input("Please enter the Employee name: ")
            userInput = userInput.title()
            name = validate("^[A-Za-z]{1,30}$", userInput)

            if name:
                emply.name = userInput
                break
            else:
                print("Please enter a valid name")

        while True:
            userInput = input("Please enter the Employee salary: ")
            userInput = userInput
            salary = validate("^[0-9]+(.([0-9]){2})?$", userInput)

            if salary:
                emply.salary = float(userInput)
                break
            else:
                print("Please enter a valid salary")

        while True:
            userInput = input("Please enter the Employee email: ")
            userInput = userInput
            email = validate(
                "^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$", userInput)

            if email:
                emply.email = userInput
                break
            else:
                print("Please enter a valid email")

        while True:
            userInput = input("Please enter the employee's department id: ")
            did = validate("^[0-9]+$", userInput)

            if did:
                emply.did = int(userInput)
                break
            else:
                print("Please enter a valid id")

        while True:
            userInput = input("Please enter the Employee's post: ")
            userInput = userInput.title()
            post = validate("^[A-Za-z]{1,30}$", userInput)

            if post:
                emply.post = userInput
                break
            else:
                print("Please enter a valid post")

        print("\n")
        print("Do you want to insert these values into the DB?: y/n ".format(
            emply.print_info(emply.eid, emply.last_name, emply.name,
            emply.salary, emply.email, emply.did, emply.post)))
        userInput = input()


insert_department()
# insert_employee()
