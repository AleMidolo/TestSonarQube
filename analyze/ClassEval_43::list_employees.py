def list_employees(self):
    """
        列出HRManagementSystem中所有员工的信息。
        :return: 所有员工信息的列表，dict。
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.list_employees()
        {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}

        """
    result = {}
    for employee_id, employee_data in self.employees.items():
        result[employee_id] = {'employee_ID': employee_id, 'name': employee_data['name'], 'position': employee_data['position'], 'department': employee_data['department'], 'salary': employee_data['salary']}
    return result