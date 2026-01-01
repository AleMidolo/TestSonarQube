def update_employee(self, employee_id: int, employee_info: dict):
    """
        एचआर प्रबंधन प्रणाली में एक कर्मचारी की जानकारी को अपडेट करें।
        :param employee_id: कर्मचारी का आईडी, int।
        :param employee_info: कर्मचारी की जानकारी, dict।
        :return: यदि कर्मचारी पहले से एचआर प्रबंधन प्रणाली में है, तो True लौटाता है, अन्यथा False लौटाता है।
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        True
        >>> hrManagementSystem.update_employee(2, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        False

        """
    if employee_id not in self.employees:
        return False
    valid_keys = ['name', 'position', 'department', 'salary']
    for key, value in employee_info.items():
        if key in valid_keys:
            self.employees[employee_id][key] = value
    return True