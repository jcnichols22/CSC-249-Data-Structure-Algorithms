#Define the class Employee.
class Employee:
    #initialize the variables.
    employeeName = ''
    IdNumber = ''
    department = ''
    jobTitle = ''

#Create an object of the class Employee.
employeeObj1 = Employee()
#Assign values to the members of the class for the object.
employeeObj1.employeeName = 'Susan Meyers'
employeeObj1.IdNumber = '47899'
employeeObj1.department = 'Accounting'
employeeObj1.jobTitle = 'Vice President'

#Create another object of the class Employee.
employeeObj2 = Employee()

#Assign values to the members of the class for the object.
employeeObj2.employeeName = 'Mark Jones'
employeeObj2.IdNumber = '39119'
employeeObj2.department = 'IT'
employeeObj2.jobTitle = 'Programmer'

#Create another object of the class Employee.
employeeObj3 = Employee()

#Assign values to the members of the class for the current object.
employeeObj3.employeeName = 'Joy Rogers'
employeeObj3.IdNumber = '81774'
employeeObj3.department = 'Manufacturing'
employeeObj3.jobTitle = 'Engineer'

#Display the details of each employee
print('Name:', employeeObj1.employeeName)
print('ID Number:', employeeObj1.IdNumber)
print('Department:', employeeObj1.department)
print('Job Title:', employeeObj1.jobTitle)
print()
print('Name:', employeeObj2.employeeName)
print('ID Number:', employeeObj2.IdNumber)
print('Department:', employeeObj2.department)
print('Job Title:', employeeObj2.jobTitle)
print()
print('Name:', employeeObj3.employeeName)
print('ID Number:', employeeObj3.IdNumber)
print('Department:', employeeObj3.department)
print('Job Title:', employeeObj3.jobTitle)