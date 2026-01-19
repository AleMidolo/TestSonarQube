def list_employees(self):
    """
    Lista toda la información de los empleados en el HRManagementSystem.
    :return: Una lista de toda la información de los empleados, dict.
    >>> hrManagementSystem = HRManagementSystem()
    >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
    >>> hrManagementSystem.list_employees()
    {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}

    """
    result = {}
    for employee_id, employee_info in self.employees.items():
        result[employee_id] = {'employee_ID': employee_id}
        result[employee_id].update(employee_info)
    return result