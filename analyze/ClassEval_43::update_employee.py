def update_employee(self, employee_id: int, employee_info: dict):
    """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: The employee's information, dict.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        True
        >>> hrManagementSystem.update_employee(2, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        False
        """
    if employee_id in self.employees:
        self.employees[employee_id].update(employee_info)
        return True
    else:
        return False