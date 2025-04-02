from EmployeeEntity import EmployeeEntity
from EmployeeDao import EmployeeDao
import os

if __name__ == '__main__':
    dao = EmployeeDao('employeedb.sqlite')


    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    flag = True
    while flag:
        clear_console()
        print("MENU OPTIONS")
        print("1. Insert Employee")
        print("2. Get Employee by ID")
        print("3. Get All Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Delete All Employees")
        print("7. Exit")

        choice = int(input("Enter your choice (1,2,3,4,5,6,7): "))
        clear_console()


        if choice == 1:
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            employee = EmployeeEntity(name=name, position=position, salary=salary, hire_date=hire_date)
            dao.insert(employee)

        elif choice == 2:
            id = int(input("Enter id: "))
            employee = dao.get_by_id(id)
            print(employee)
        elif choice == 3:
            employees = dao.get_all()
            for employee in employees:
                print(employee)
        elif choice == 4:
            id = int(input("Enter id: "))
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            employee = EmployeeEntity(id=id, name=name, position=position, salary=salary, hire_date=hire_date)
            dao.update(employee)

        elif choice == 5:
            id = int(input("Enter id: "))
            dao.delete(id)

        elif choice == 6:
            dao.delete_all()

        else:
            flag = False




