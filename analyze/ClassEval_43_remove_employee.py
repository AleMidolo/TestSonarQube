def remove_employee(self, employee_id):
    """
    एचआर प्रबंधन प्रणाली से एक कर्मचारी को हटाएं।
    :param employee_id: कर्मचारी का आईडी, int।
    :return: यदि कर्मचारी पहले से एचआर प्रबंधन प्रणाली में है, तो True लौटाता है, अन्यथा, False लौटाता है।
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