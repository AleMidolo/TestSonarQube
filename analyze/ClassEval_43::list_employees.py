def list_employees(self):
    """
        Elenca tutte le informazioni sui dipendenti nel HRManagementSystem.
        :return: Un elenco di tutte le informazioni sui dipendenti, dict.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.list_employees()
        {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        """
    return {employee_id: {**{'employee_ID': employee_id}, **info} for employee_id, info in self.employees.items()}