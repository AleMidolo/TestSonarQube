def remove_employee(self, employee_id):
    """
        从HRManagementSystem中移除员工。
        :param employee_id: 员工的ID，int类型。
        :return: 如果员工已经在HRManagementSystem中，返回True；否则，返回False。
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