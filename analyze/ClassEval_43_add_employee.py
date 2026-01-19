def add_employee(self, employee_id, name, position, department, salary):
    """
    HRManagementSystem में एक नया कर्मचारी जोड़ें।
    :param employee_id: कर्मचारी का आईडी, int।
    :param name: कर्मचारी का नाम, str।
    :param position: कर्मचारी की स्थिति, str।
    :param department: कर्मचारी का विभाग, str।
    :param salary: कर्मचारी का वेतन, int।
    :return: यदि कर्मचारी पहले से HRManagementSystem में है, तो False लौटाता है, अन्यथा, True लौटाता है।
    >>> hrManagementSystem = HRManagementSystem()
    >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
    True
    >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
    False

    """
    if not hasattr(self, 'employees'):
        self.employees = {}
    
    if employee_id in self.employees:
        return False
    
    self.employees[employee_id] = {
        'name': name,
        'position': position,
        'department': department,
        'salary': salary
    }
    return True