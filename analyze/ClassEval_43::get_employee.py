def get_employee(self, employee_id):
    """
        从HRManagementSystem获取员工信息。
        :param employee_id: 员工的ID，int类型。
        :return: 如果员工已经在HRManagementSystem中，返回员工的信息；否则，返回False。
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.get_employee(1)
        {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}
        >>> hrManagementSystem.get_employee(2)
        False

        """
    if employee_id in self.employees:
        return self.employees[employee_id]
    else:
        return False