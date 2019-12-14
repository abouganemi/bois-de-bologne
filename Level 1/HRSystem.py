
# Variables
deptList = []
empList = []
userInput = None


def add_dept(department):
    entryList = []
    userInput = input("Please enter the department name or EXIT when you finish: ")
    while userInput != "exit":
        if userInput:
            entryList.append(userInput)
            userInput = input("Please enter the department name or EXIT when you finish: ")
        else:
            print("The department name could not be empty. Please enter the department name or EXIT when you finish: ")
            userInput = input("Please enter the department name or EXIT when you finish: ")
    return entryList

# Assing the list return value of the function add_Dept to a list variable
deptList = add_dept(userInput)

def add_employee(employee, department):
    entryList = []
    userInput = None
    salary = 0
    department = None
    while userInput != "no":
        userInput = input("Please enter the employee first name: ")
        name = userInput.title()
        userInput = input("Please enter the employee last name: ")
        lastName = userInput.title()
        entryList.append(name + " " + lastName)
        userInput = float(input("Please enter the employee salary: "))
        while userInput < 0:
            print("The salary cannot be negative. Please enter salary again.")
            userInput = float(input("Please enter the employee salary: "))
            if float(userInput) > 0:
                break
        entryList.append(float(userInput))
        userInput = input("Please enter the employee department name: ")
        while userInput not in deptList:
            print("Department not found, please enter a correct department from the following list:\n")
            print(deptList)
            if userInput in entryList:
                break
            else:
                userInput = input("Please enter the employee department name: ")
        entryList.append(userInput)
        userInput = input("Do you want to add another employee yes/no: ")
    return entryList

empList = add_employee(userInput, deptList)

#def salary_cal(employee, department):

#print(empList)

"""count = 0
totalIT = 0
for x in range(len(empList)):
    if empList[x] == "it":
        totalIT += empList[x-1]
print(totalIT)"""
countDept = 0
totalIT = 0
maxSalary = 0
minSalary = 0
avgSalaryDept = 0
for dept in range(len(deptList)):
    for x in range(len(empList)):
        if deptList[dept] == empList[x]:
            totalIT += empList[x - 1]
            if empList[x - 1] > maxSalary:
                maxSalary = empList[x - 1]
            else:
                maxSalary = maxSalary
            if empList[x - 1] < minSalary:
                minSalary = empList[x - 1]
            else:
                minSalary = minSalary

            countDept += 1
    print("Total Salary for {} Department is: {}".format(deptList[dept].upper(), totalIT))
    print("Max Salary for {} Department is: {}".format(deptList[dept].upper(), maxSalary))
    print("Min Salary for {} Department is: {}".format(deptList[dept].upper(), minSalary))





