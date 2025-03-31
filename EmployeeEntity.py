class EmployeeEntity:
    def __init__(self, id, name, position, salary, hire_date):
        self._id = id
        self._name = name
        self._position = position
        self._salary = salary
        self._hire_date = hire_date

    # Getters
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def get_salary(self):
        return self._salary

    def get_hire_date(self):
        return self._hire_date

    # Setters
    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_position(self, position):
        self._position = position

    def set_salary(self, salary):
        self._salary = salary

    def set_hire_date(self, hire_date):
        self._hire_date = hire_date

    # __str__ method
    def __str__(self):
        return f"EmployeeEntity(id={self._id}, name={self._name}, position={self._position}, salary={self._salary}, hire_date={self._hire_date})"