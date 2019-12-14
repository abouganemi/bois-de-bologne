def inserterListeDepartmenet():
    global departement
    departement = input("Please enter the department name or EXIT when you finish : ")
    while (departement.lower() != "exit"):
        if departement.upper() in listeDepartement:
            print("The department name already exists. ", end="")
        elif departement == "":
            print("The department name could not be empty. ", end="")
        else:
            listeDepartement.append(departement.upper())
        departement = input("Please enter the department name or EXIT when you finish :  ")
    print(listeDepartement)
    print()

def insererFnameListe():
    fname = input("Please enter the employee first name : ")
    listeFname.append(fname)
    print(listeFname)
    print()

def insererLname():
    lname = input("Please enter the employee last name : ")
    listeLname.append(lname)
    print(listeLname)
    print()

def insererListeSalaire():
    strintSalaire = input("Please enter the employee salary : ")
    salaire = float(strintSalaire)
    while (salaire < 0):
        print("The salary must be a positive value. ", end="")
        strintSalaire = input("Please enter the employee salary : ")
        salaire = float(strintSalaire)
    listeSalary.append(salaire)
    print(listeSalary)
    print()

def insererDepartmenetEmployeListe():
    departementEmploye = input("Please enter department name : ")
    while (departementEmploye.upper() not in listeDepartement):
        print("The departement is not in the departements list. ", end="")
        departementEmploye = input("Please enter department name : ")
    listeDepartementEmployee.append(departementEmploye.upper())
    print(listeDepartementEmployee)
    print()

def saisirResponse():
    global reponse
    reponse = input("Do you want to enter another employee yes/no? ")
    while (reponse.upper() != "YES" and reponse.upper() != "NO"):
        print("The answer must be Yes or No. ", end="")
        reponse = input("Do you want to enter another employee yes/no? ")

def afficherStatisticTotal():
    sommeTotal = sum(listeSalary)
    print("Average Salary for ALL departments is : ", sommeTotal / len(listeSalary))
    print("Max Salary for ALL departments is : ", max(listeSalary))
    print("Min Salary for ALL departments is : ", min(listeSalary))
    print()

def afficherStatistiqueParDepartement():
    global departement
    for departement in listeDepartement:
        count = 0
        somme = 0
        maxSalaire = min(listeSalary)
        minSalaire = max(listeSalary)
        for i in range(len(listeDepartementEmployee)):
            if listeDepartementEmployee[i] == departement:
                count += 1
                somme += listeSalary[i]
                if listeSalary[i] > maxSalaire:
                    maxSalaire = listeSalary[i]
                if listeSalary[i] < minSalaire:
                    minSalaire = listeSalary[i]

        if count != 0:
            print("Average Salary for {} departments is : {}".format(departement, somme / count))
            print("Max Salary for {} departments is : {}".format(departement, maxSalaire))
            print("Min Salary for {} departments is : {}".format(departement, minSalaire))
            print()
        else:
            print("Average Salary for {} department is : Not Available".format(departement))
            print("Max Salary for {} department is : Not Available".format(departement))
            print("Min Salary for {} department is : Not Available".format(departement))
            print()


listeDepartement = []

inserterListeDepartmenet()
listeFname = []
listeLname = []
listeSalary = []
listeDepartementEmployee = []
reponse="YES"


while(reponse.upper()=="YES"):

    insererFnameListe()

    insererLname()

    insererListeSalaire()

    insererDepartmenetEmployeListe()

    saisirResponse()
print()


afficherStatisticTotal()

afficherStatistiqueParDepartement()
