def add_employee(self, employee_id, name, position, department, salary):
    """
    将新员工添加到HRManagementSystem中。
    :param employee_id: 员工的ID，int。
    :param name: 员工的姓名，str。
    :param position: 员工的职位，str。
    :param department: 员工的部门，str。
    :param salary: 员工的薪资，int。
    :return: 如果员工已经在HRManagementSystem中，返回False，否则返回True。
    >>> hrManagementSystem = HRManagementSystem()
    >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
    True
    >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
    False

    """
    if employee_id in self.employees:
        return False
    
    self.employees[employee_id] = {
        'name': name,
        'position': position,
        'department': department,
        'salary': salary
    }
    return True