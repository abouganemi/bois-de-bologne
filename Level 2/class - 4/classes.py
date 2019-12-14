class Department():
    '''
    Class that defines a Department characterized by:
    - did: Department ID
    - name: Name of the department
    - phone: Phone department
    '''

    def __init__(self, did, name, phone):  # Constructor
        self.did = did
        self.name = name
        self.phone = phone

    def print_info(self, did, name, phone):
        print("*" * 30)
        print("Department ID: {}\nDepartment Name: {}\nDeparment Phone: {}".format(
            self.did, self.name, self.phone))


class Employee():
    '''
    Class that defines an Employee characterized by:
    - eid: Employee ID
    - last_name: Employee's last name
    - name: Name of the employee
    - salary: Salary of the employee
    - email: Email of the employee
    - did: Department ID of the employee
    - post: Employee's post
    '''

    # Constructor
    def __init__(self, eid, last_name, name, salary, email, did, post):
        self.eid = eid
        self.last_name = last_name
        self.name = name
        self.salary = salary
        self.email = email
        self.did = did
        self.post = post

    def print_info(self, eid, last_name, name, salary, email, did, post):
        print("*" * 30)
        print("Employee ID: {}\nEmployee Last Name: {}\nEmployee Name: {}\nEmployee Salary: {}\nEmployee Email: {}\nEmployee Dept ID: {}\nEmployee Post: {} ".format(
                       self.eid, self.last_name, self.name,
                       self.salary, self.email, self.did, self.post))


