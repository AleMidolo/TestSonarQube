def add_employee(self, employee_id, name, position, department, salary):
    """
        Agrega un nuevo empleado al HRManagementSystem.
        :param employee_id: El id del empleado, int.
        :param name: El nombre del empleado, str.
        :param position: La posición del empleado, str.
        :param department: El departamento del empleado, str.
        :param salary: El salario del empleado, int.
        :return: Si el empleado ya está en el HRManagementSystem, devuelve False, de lo contrario, devuelve True.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        True
        >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        False

        """
    if employee_id in self.employees:
        return False
    else:
        self.employees[employee_id] = {'name': name, 'position': position, 'department': department, 'salary': salary}
        return True