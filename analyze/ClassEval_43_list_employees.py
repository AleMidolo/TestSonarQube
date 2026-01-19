def list_employees(self):
    """
        List all employees' information in the HRManagementSystem.
        :return: A list of all employees' information,dict.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.list_employees()
        {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        """
    result = {}
    for employee_id, info in self.employees.items():
        result[employee_id] = info.copy()
        result[employee_id]['employee_ID'] = employee_id
    return result