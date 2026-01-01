def get_employee(self, employee_id):
    """
        Obtiene la información de un empleado del SistemaDeGestiónDeRRHH.
        :param employee_id: El id del empleado, int.
        :return: Si el empleado ya está en el SistemaDeGestiónDeRRHH, devuelve la información del empleado, de lo contrario, devuelve False.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.get_employee(1)
        {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        >>> hrManagementSystem.get_employee(2)
        False
        """
    if employee_id in self.employees:
        return self.employees[employee_id]
    return False