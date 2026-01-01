def list_employees(self):
    """
        HRManagementSystem में सभी कर्मचारियों की जानकारी सूचीबद्ध करें।
        :return: सभी कर्मचारियों की जानकारी की एक सूची, dict।
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.list_employees()
        {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        """
    return {employee_id: {**{'employee_ID': employee_id}, **info} for employee_id, info in self.employees.items()}