import os
import re

# cette étape peut être suprimmer si on ajoute le
# chemin a la variable d'environnement de Windows
os.chdir("C:\\instantclient_18_5")
import cx_Oracle

# on importe notre module d'oracle
import cx_Oracle

connection = None
curs = None


def insert_category(id, name):
    global curs
    sql = "insert into categories values(:idCategorie, :nomCategorie)"
    curs = connection.cursor()
    curs.prepare(sql)
    curs.execute(None, idCategorie=id,
                 nomCategorie=name)
    connection.commit()


def insert_utilisateur(username, password, name, lastname, email, creationdate, creditnumber, phone, categoryID):
    global curs
    sql = "insert into utilisateurs values(:userName, :motPass, :prenomUtilisateur, :nomUtilisateur " \
          ", :courrielUtilisateur, to_date(:dateCreation, 'DD-MM-YYYY') " \
          ", :NumeroCredit, :telephoneUtilisateur, :idCategory)"
    curs = connection.cursor()
    curs.prepare(sql)
    curs.execute(None, userName=username,
                 motPass=password,
                 prenomUtilisateur=name,
                 nomUtilisateur=lastname,
                 courrielUtilisateur=email,
                 dateCreation=creationdate,
                 NumeroCredit=creditnumber,
                 telephoneUtilisateur=phone,
                 idCategory=categoryID)
    connection.commit()


def print_category():
    global curs
    sql = "SELECT ID, NAME FROM CATEGORIES "
    curs = connection.cursor()
    curs.prepare(sql)
    curs.execute(None)
    for row in curs:
        print(row)


def get_categories_id():
    global curs
    listIDs = []
    sql = "SELECT ID FROM CATEGORIES "
    curs = connection.cursor()
    curs.prepare(sql)
    curs.execute(None)
    for row in curs:
        listIDs.append(row[0])
    return listIDs


def print_utilisateur():
    global curs
    sql = " SELECT USERNAME, PASSWORD, NOM, PRENOM, EMAIL, CREATIONDATE, CREDIT, TELEPHONE, CATEGORYID" \
          " FROM UTILISATEURS "
    curs = connection.cursor()
    curs.prepare(sql)
    curs.execute(None)
    for row in curs:
        print(row)


messageGetValue = "Please enter {} "
messageStopGetEntries = "Do you want to enter another {} ? yes/no : "
messageWrong = "The {} have to be {}"

valueStopGetEntries = "no"
valueTypeEntryNumeric = "numeric"
valueTypeEntryString = "string"
exitOption = ""

listCategories = []


def validate(regex, value):
    result = re.match(regex, value)
    if result:
        return True
    else:
        return False


def get_entry(message_get_entry_value, message_wrong_value, pattern):
    entry = input(message_get_entry_value)
    if validate(pattern, entry):
        return entry
    else:
        print(message_wrong_value)
        return "0"


def get_exit(message_get_entry_value, message_wrong_value):
    pattern=""
    entry = input(message_get_entry_value)
    # Exit pattern return -1
    if validate(pattern, entry):
        if entry.lower() is not "yes":
            return "-1"
        else:
            return entry
    else:
        print(message_wrong_value)
        return "0"


def get_entry_category():
    while exitOption != "-1":
        while True:
            idCategory = get_entry(messageGetValue.format("the ID category: "),
                                   messageWrong.format("ID category", "a number"), "^[0-9]+$")
            if idCategory != "0":
                break

        while True:
            nameCategory = get_entry(messageGetValue.format("the Category Name: "),
                                     messageWrong.format("Category Name", "a String max 30 characters"), "^[A-Za-z]{1,30}+$")
            if nameCategory != "0":
                break

        insert_category(idCategory, nameCategory)

        while True:
            exitOption = get_exit(messageStopGetEntries.format("Category"),
                                  messageWrong.format("Exit Option", "yes or no"), "")
            if exitOption == "-1" or exitOption == "yes":
                break


def get_entry_utilisateur():
    while exitOption != "-1":
        while True:
            userName = get_entry(messageGetValue.format("the username: "),
                                 messageWrong.format("username", "a String max 30 characters"), "^[A-Za-z]{1,30}+$")
            if userName != "0":
                break

        while True:
            password = get_entry(messageGetValue.format("the Password: "),
                                 messageWrong.format("Password", "a String max 30 characters"), "")
            if password != "0":
                break

        while True:
            nom = get_entry(messageGetValue.format("the User Name: "),
                            messageWrong.format("User Name", "a String max 50 characters"), "^[A-Za-z]{1,50}+$")
            if nom != "0":
                break

        while True:
            prenom = get_entry(messageGetValue.format("the User Last Name: "),
                               messageWrong.format("User Last Name", "a String max 50 characters"), "^[A-Za-z]{1,50}+$")
            if prenom != "0":
                break

        while True:
            email = get_entry(messageGetValue.format("the User email: "),
                              messageWrong.format("User email", "formated as an email"),
                              "")
            if email != "0":
                break

        while True:
            creation = get_entry(messageGetValue.format("the Creation Date: "),
                                 messageWrong.format("Creation Date", "formated as an date"), "")
            if creation != "0":
                break

        while True:
            credit = get_entry(messageGetValue.format("the Credit Number: "),
                               messageWrong.format("Creation Date", "a number with 2 decimals"), "")
            if credit != "0":
                break

        while True:
            telephone = get_entry(messageGetValue.format("the User Telephone: "),
                                  messageWrong.format("User Telephone", "formated as a telephone number"), "")
            if telephone != "0":
                break

        while True:
            idcategory = get_entry(messageGetValue.format("the ID Category: "),
                                   messageWrong.format("ID category", "a number"), "")
            if idcategory != "0":
                if idcategory not in get_categories_id():
                    print("This ID Category does not exist. Please enter a valid ID Category: ", get_categories_id())
                else:
                    break

        while True:
            exitOption = get_exit(messageStopGetEntries.format("User"),
                                  messageWrong.format("Exit Option", "yes or no"), "")
            if exitOption == "-1" or exitOption == "yes":
                break

        insert_utilisateur(userName, password, nom, prenom, email, creation, credit, telephone, idcategory)


try:

    connection = cx_Oracle.connect("info33", "anypw", "144.217.163.57/XE")
    print("\n\n/////////Table Category////////////")
    get_entry_category()
    print_category()


    print("\n\n/////////Table utilisateur////////////")
    get_entry_utilisateur()
    print_utilisateur()


except cx_Oracle.DatabaseError as e:
    print("Failed to insert row ", e)
    print(cx_Oracle.DatabaseError)

finally:
    if curs is not None:
        curs.close()
    if connection is not None:
        connection.close()
