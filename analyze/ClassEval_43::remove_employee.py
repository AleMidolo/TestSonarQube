def remove_employee(self, employee_id):
    """
        Eliminar un empleado del HRManagementSystem.
        :param employee_id: El id del empleado, int.
        :return: Si el empleado ya está en el HRManagementSystem, devuelve True, de lo contrario, devuelve False.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.remove_employee(1)
        True
        >>> hrManagementSystem.remove_employee(2)
        False
        """
    if employee_id in self.employees:
        del self.employees[employee_id]
        return True
    else:
        return False