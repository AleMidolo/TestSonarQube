def update_employee(self, employee_id: int, employee_info: dict):
    """
        Actualiza la información de un empleado en el HRManagementSystem.
        :param employee_id: El id del empleado, int.
        :param employee_info: La información del empleado, dict.
        :return: Si el empleado ya está en el HRManagementSystem, devuelve True, de lo contrario, devuelve False.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        True
        >>> hrManagementSystem.update_employee(2, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        False

        """
    if employee_id not in self.employees:
        return False
    for key, value in employee_info.items():
        if key in self.employees[employee_id]:
            self.employees[employee_id][key] = value
    return True