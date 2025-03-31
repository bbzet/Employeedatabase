import sqlite3
from EmployeeEntity import EmployeeEntity

class EmployeeDao:
    def __init__(self, database):
        self.__conn = sqlite3.connect(database)
        self.__cursor = self.__conn.cursor()

    def insert(self, employee: EmployeeEntity):
        sql = ''' INSERT INTO employee(name, position, salary, hire_date)
                  VALUES(?,?,?,?)  '''

        self.__cursor.execute(sql, (employee.get_name(), employee.get_position(), employee.get_salary(), employee.get_hire_date()))
        id = self.__cursor.lastrowid
        self.__conn.commit()

        return id

    def get_by_id(self, id):
        sql = ''' SELECT id, name, position, salary, hire_date
        FROM employee
        WHERE id = ?'''

        self.__cursor.execute(sql, (id,))
        row = self.__cursor.fetchone()
        if row:
            employee = EmployeeEntity(id = row[0], name = row[1], position = row[2], salary = row[3], hire_date = row[4])
        else:
            return None
        return employee

    def get_all(self):
        sql = ''' SELECT * 
        FROM employee'''

        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()

        for row in rows:
            print(row)

    def update(self, employee: EmployeeEntity):
        sql = ''' UPDATE employee SET name = ?,
        position = ?, salary = ?, hire_date = ?
        WHERE id = ?'''

        self.__cursor.execute(sql, (employee.get_name(), employee.get_position(), employee.get_salary(), employee.get_hire_date(), employee.get_id()))
        self.__conn.commit()
        return self.__cursor.rowcount

    def delete(self, id):
        sql = ''' DELETE FROM employee WHERE id = ?'''

        self.__cursor.execute(sql, (id,))
        self.__conn.commit()
        return self.__cursor.rowcount

    def delete_all(self):
        sql =  ''' DELETE FROM employee'''

        self.__cursor.execute(sql)
        self.__conn.commit()
        return self.__cursor.rowcount

