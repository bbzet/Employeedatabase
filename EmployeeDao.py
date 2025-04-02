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
        self.__cursor.execute("SELECT * FROM employee WHERE id=?", (id,))
        row = self.__cursor.fetchone()
        if row:
            return EmployeeEntity(*row)
        return f"We can' find this id {id} "

    def get_all(self):
        sql = ''' SELECT * 
        FROM employee'''

        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()

        return [EmployeeEntity(*rows) for rows in rows]

    def update(self, employee: EmployeeEntity):
        sql = ''' UPDATE employee SET name = ?,
        position = ?, salary = ?, hire_date = ?
        WHERE id = ?'''

        self.__cursor.execute(sql, (employee._name, employee._position, employee._salary, employee._hire_date, employee._id))
        self.__conn.commit()

    def delete(self, id):
        sql = ''' DELETE FROM employee WHERE id = ?'''

        self.__cursor.execute(sql, (id,))
        self.__conn.commit()

    def delete_all(self):
        sql =  ''' DELETE FROM employee'''

        self.__cursor.execute(sql)
        self.__conn.commit()

