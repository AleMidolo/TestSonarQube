def get_employee(self, employee_id):
    """
        एचआर प्रबंधन प्रणाली से एक कर्मचारी की जानकारी प्राप्त करें।
        :param employee_id: कर्मचारी का आईडी, int.
        :return: यदि कर्मचारी पहले से एचआर प्रबंधन प्रणाली में है, तो कर्मचारी की जानकारी लौटाता है, अन्यथा, False लौटाता है।
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