# Employee Database Management System

A Python application that manages employee records using **SQLite** and implements full **CRUD** operations through a Data Access Object (DAO) pattern.

---

##  Project Overview

This project includes:

- A database named `employee_db.sqlite`
- A table `employee` with the following columns:
  - `id` (integer, primary key, auto-increment)
  - `name` (text)
  - `position` (text)
  - `salary` (real)
  - `hire_date` (text)

---

##  Project Files

- `employee.py` — Employee entity class
- `employee_dao.py` — DAO class with CRUD methods
- `main.py` — Test script with sample CRUD operations
- `screenshots` — Screenshot of the employee
- `README.md` — This documentation

---

##  Classes & Methods

###  `Employee` class

Represents an employee record.

**Fields:**
- `id`: int — employee ID
- `name`: str — employee name
- `position`: str — job title
- `salary`: float — monthly salary
- `hire_date`: str — date of hire (YYYY-MM-DD)

**Methods:**
- Constructor to initialize employee
- `__str__()` method for easy printing

---

###  `EmployeeDAO` class

Handles all database operations.

| Method         | Description                                  |
|----------------|----------------------------------------------|
| `insert()`     | Insert a new employee                        |
| `get_by_id()`  | Get an employee by ID                        |
| `get_all()`    | Retrieve all employees                       |
| `update()`     | Update employee details                      |
| `delete()`     | Delete an employee by ID                     |

---

##  How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/employee-database.git
   cd employee-database


## Run the project:
```bash
python main.py
```
### Sample Input/Output
```bash
MENU OPTIONS
1. Insert Employee
2. Get Employee by ID
3. Get All Employees
4. Update Employee
5. Delete Employee
6. Delete All Employees
7. Exit
Enter your choice (1,2,3,4,5,6,7): 1
Enter name: Baiastan
Enter position: data 
Enter salary: 20000
Enter hire date (YYYY-MM-DD): 04042025
```
## Screenshots
**SQLite Table**
[](https://raw.githubusercontent.com/bbzet/Employeedatabase/refs/heads/main/screenshot/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-02%20151846.png)
**Console Test Output**
[](https://raw.githubusercontent.com/bbzet/Employeedatabase/refs/heads/main/screenshot/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-02%20150748.png)
[](https://raw.githubusercontent.com/bbzet/Employeedatabase/refs/heads/main/screenshot/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-02%20150924.png)
[](https://raw.githubusercontent.com/bbzet/Employeedatabase/refs/heads/main/screenshot/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-02%20151028.png)
[](https://raw.githubusercontent.com/bbzet/Employeedatabase/refs/heads/main/screenshot/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-04-02%20151341.png)

