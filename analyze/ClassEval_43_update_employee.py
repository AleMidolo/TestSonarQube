def update_employee(self, employee_id: int, employee_info: dict):
    """
    更新HRManagementSystem中员工的信息。
    :param employee_id: 员工的ID，int类型。
    :param employee_info: 员工的信息，dict类型。
    :return: 如果员工已经在HRManagementSystem中，返回True，否则返回False。
    >>> hrManagementSystem = HRManagementSystem()
    >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
    >>> hrManagementSystem.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
    True
    >>> hrManagementSystem.update_employee(2, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
    False

    """
    if employee_id in self.employees:
        self.employees[employee_id] = employee_info
        return True
    else:
        return False