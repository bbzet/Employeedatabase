from EmployeeEntity import EmployeeEntity
from EmployeeDao import EmployeeDao
import os

def main():
    dao = EmployeeDao('employeedb.sqlite')

    emp1 = EmployeeEntity(1, "Baiastan", "data", 20000, "2023-10-01")
    dao.insert(emp1)
    print("Inserted:", emp1)

    print("All Employees:")
    for emp in dao.get_all():
        print(emp)

    fetched = dao.get_by_id(86)
    print("Fetched by ID:", fetched)

    emp1_updated = EmployeeEntity(86, "Abai", "Devops", 40000, "2023-10-01")
    dao.update(emp1_updated)
    print("Updated:", dao.get_by_id(86))

    dao.delete(86)
    print("After deletion, all employees:", dao.get_all())
    dao.delete_all()


if __name__ == '__main__':

    main()




