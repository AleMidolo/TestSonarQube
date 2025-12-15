class HRManagementSystem: 
    def __init__(self):
        """
        Initialize the HRManagementSystem with an attribute employees, which is an empty dictionary.
        """
        self.employees = {}

    def remove_employee(self, employee_id):
        """
        Remove an employee from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
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
    
    def update_employee(self, employee_id: int, employee_info: dict):
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: The employee's information, dict.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.update_employee(1, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        True
        >>> hrManagementSystem.update_employee(2, {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 20000})
        False
        """
        employee = self.get_employee(employee_id)
        if employee == False:
            return False
        else:
            for key, value in employee_info.items():
                if key not in employee:
                    return False
            for key, value in employee_info.items():
                employee[key] = value
            return True
    
    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.
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
    
    def list_employees(self):
        """
        List all employees' information in the HRManagementSystem.
        : return: A list of all employees' information, dict.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.list_employees()
        {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager',
            'department': 'Sales', 'salary': 100000}}
        """
        employee_data = {}
        if self.employees:
            for employee_id, employee_info in self.employees.items():
                employee_details = {}
                employee_details["employee_ID"] = employee_id
                for key, value in employee_info.items():
                    employee_details[key] = value
                employee_data[employee_id] = employee_details
        return employee_data
    
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
        if employee_id in self.employees:
            return False
        else:
            self.employees[employee_id] = {
                'name': name,
                'position': position,
                'department': department,
                'salary': salary
            }
            return True